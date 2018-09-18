import Route from '@ember/routing/route';
import { set } from '@ember/object';

export default Route.extend({
  // make installation records available in the template
  setupController(controller, model) {
    this._super(controller, model);
    set(this, 'controller', controller)
  },

  actions: {
    createInstallation(geoJson, dataSource) {
      // create a new installation record from shape layer
      let installation = this.store.createRecord('installation', {
        shape: geoJson,
        data_source: dataSource
      });

      // send shape layer to api
      return installation.save()
      .then((record) =>{
        // then make api data available to the template
        set(this, 'controller.installation', installation);
      });
    }

  }
});
