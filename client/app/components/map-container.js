import Component from '@ember/component';
import { set } from '@ember/object';
import { computed } from '@ember/object';
import { task } from 'ember-concurrency';

export default Component.extend({
  classNames: ['map-container'],

  init() {
    // initialize map defaults in boston
    this._super(...arguments);
    set(this, 'lat', 42.360081);
    set(this, 'lng', -71.058884);
    set(this, 'zoom', 12);
    set(this, 'dataSource', 'DNR');
  },

  info: computed('hasEnteredAddress', 'drawnShape', {
    // update UI based on interaction state
    get() {
      let cta;
      if(this.hasEnteredAddress) {
        cta = 'Now use the tools to draw the shape of your solar installation';
      } else {
        cta = 'Enter the address of your solar installation';
      }
      if (this.drawnShape) {
        cta = 'Calculate the nominal power for this solar installation';
      }

      return cta;
    }
  }),

  createInstallation: task(function * (){
    yield this.onCreateInstallation(this.drawnShape, this.dataSource);
  }),

  actions: {

    setMapPosition(responseData) {
      // update map position from openstreetmap geocode api response data
      if (responseData.length) {
        let result = responseData[0];
        set(this, 'lat', result.lat);
        set(this, 'lng', result.lon);
        set(this, 'zoom', 18);
        set(this, 'hasEnteredAddress', true);
        set(this, 'drawnShape', null);
      }
    },

    updateFeature(feature){
      // user has completed drawing a shape
      let geoJson = feature.layer.toGeoJSON();
      set(this, 'drawnShape', geoJson);
    },

    selectDataSource(val) {
      set(this, 'dataSource', val);
    }

  }
});
