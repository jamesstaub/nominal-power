from django.contrib.gis.geos import GEOSGeometry
from collections import OrderedDict
import requests
import uuid
import json
# http://epsg.io/32118
EPSG_NY = 32118

class GeoResponse:
    """
    Instatiate with a geojson shape
    calculate selected area and nominal power
    """
    def __init__(self, installation_dict):
        geojson = installation_dict['shape']
        data_source = installation_dict['data_source']

        self.polygon = GEOSGeometry(str(geojson['geometry']))
        self.area, self.centroid = self.get_area()
        self.solar_radiation = self.get_solar_radiation(data_source)
        self.nominal_power = self.get_nominal_power()

        self.json = self.get_json_response()

    def get_area(self):
        """
        convert polygon area in degrees squared to area in square meters
        """
        coords = self.polygon.centroid.coords
        self.polygon.transform(EPSG_NY, clone=False)
        return self.polygon.area, coords

    def get_solar_radiation(self, data_source):
        """
        Request NASA POWER api to retrieve solar radiation values at given coordinates
        https://power.larc.nasa.gov/
        https://power.larc.nasa.gov/docs/v1/

        Value              Name                      Units
        SI_EF_OPTIMAL  	   Solar Irradiance Optimal  kW-hr/m^2/day

        DNR	               Direct Normal Radiation   kW-hr/m^2/day

        SI_EF_OPTIMAL_ANG  Solar Irradiance          Degrees
                           Optimal Angle
        """

        lat = str(self.centroid[1])
        lon = str(self.centroid[0])

        params = (
            ('request', 'execute'),
            ('identifier', 'SinglePoint'),
            ('parameters', 'SI_EF_TILTED_SURFACE,DNR'),
            ('userCommunity', 'SSE'),
            ('tempAverage', 'CLIMATOLOGY'),
            ('outputList', 'JSON'),
            ('lat', lat),
            ('lon', lon),
            ('user', 'DAV'),
        )

        response = requests.get('https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py', params=params)

        if response.status_code is 200:
            data = json.loads(response.content)
            direct_normal_radiation = OrderedDict(data['features'][0]['properties']['parameter'][data_source])

            #ordered dict of monthly values for kW-hr/m^2/day (not sure why list is 13 items long)
            direct_normal_radiation = [m[1] for m in direct_normal_radiation.items()][:12]
            annual_average_radiation = sum(direct_normal_radiation) / float(len(direct_normal_radiation))

            return annual_average_radiation


    def get_nominal_power(self):
        """
        https://photovoltaic-software.com/PV-solar-energy-calculation.php
        The global formula to estimate the electricity generated in output of a photovoltaic system is :

        E = A * r * H * PR

        E = Energy (kWh)
        A = Total solar panel Area (m2)
        r = solar panel yield or efficiency(%)
        H = Annual average solar radiation on tilted panels (shadings not included)
        PR = Performance ratio, coefficient for losses (range between 0.5 and 0.9, default value = 0.75)
        """

        r = 21
        A = self.area
        H = self.solar_radiation
        PR = 0.75
        return A * r * H * PR

    def get_json_response(self):
        # not actually saving records fake response with uuid
        return {
            'installation':{
                'id': uuid.uuid4().int,
                'area': self.area,
                'annual_average_radiation': self.solar_radiation,
                'nominal_power': self.nominal_power
            }
        }
