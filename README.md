# nominal-power
<!-- https://photovoltaic-software.com/PV-solar-energy-calculation.php -->

<!-- https://data.world/us-doe-gov/0fd3e1b2-0e53-4e37-b822-7c3e810fe78c -->

<!-- http://www.solarmango.com/faq/8 -->

<!-- http://www.greenrhinoenergy.com/solar/radiation/characteristics.php -->

### requirements
- server
  - python 3.7

- client
  - node
  - npm or yarn
  - ember cli


### to run  
- server
  - cd nominalpowerserver
  - `mkvirtualenv --python=/Library/Frameworks/Python.framework/Versions/3.7/bin/python3 <env name>`
  - `pip install -r requirements.txt`
  - start the python server on port 8000 `./manage.py runserver`

- client
  - `cd client`
  - `yarn install`
  - `ember s --proxy http://localhost:8000`

open app at http://localhost:4200

## About
This app calculates the nominal photovoltaic power for a given shape at a given location based on data from [NASA's POWER API](https://power.larc.nasa.gov/).

To use:
1. Enter an address in the US
  - address is reverse geocoded by `openstreetmap.org`
1. Draw the shape of your solar installation
1. Click Calculate

The calculation retrieves the annual average solar radiation for the given location and calculates the nominal power based on the following formula.

```
The global formula to estimate the electricity generated in output of a photovoltaic system is :
E = A * r * H * PR

E = Energy (kWh)
A = Total solar panel Area (m2)
r = solar panel yield or efficiency(%)
H = Annual average solar radiation on tilted panels (shadings not included)
PR = Performance ratio, coefficient for losses (range between 0.5 and 0.9, default value = 0.75)

```
– formula from [photovoltaic-software.com](https://photovoltaic-software.com/PV-solar-energy-calculation.php)

see `/nominalpowerserver/installations/methods.py` for implementation of this formula
