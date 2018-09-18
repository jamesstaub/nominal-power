import RESTAdapter from 'ember-data/adapters/rest';

export default RESTAdapter.extend({
  namespace: 'api',
  host: 'http://localhost:8000',

  buildURL() {
    // Django likes trailing slashes
    return this._super(...arguments) + '/';
  },

});
