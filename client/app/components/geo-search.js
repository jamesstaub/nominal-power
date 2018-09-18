import Component from '@ember/component';

export default Component.extend({
  classNames: ['geo-search'],
  actions: {
    searchAddress(query) {
      // lookup the coordinates of the address query
      let url = `https://nominatim.openstreetmap.org/search/${query}?format=json`;
      fetch(url)
      .then((response)=>{
        return response.json();
      })
      .then((data)=>{
        this.onGeoResponse(data);
      });
    }
  }
});
