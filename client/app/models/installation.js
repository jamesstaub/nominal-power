import DS from 'ember-data';
import attr from 'ember-data/attr';

export default DS.Model.extend({
  // geoJson
  shape: attr(),

  // square meters
  area: attr('number'),

  // kw/H
  nominal_power: attr('number'),
  // string key for NASA POWER API source
  data_source: attr('string')
});
