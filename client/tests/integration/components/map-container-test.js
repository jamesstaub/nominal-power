import Ember from 'ember';
import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';


moduleForComponent('map-container', 'Integration | Component | map container', {
  integration: true
});

test('interface responds to user actions', function(assert) {

  this.render(hbs`{{map-container}}`);

  assert.equal(this.$('h1').text().trim(), 'Enter the address of your solar installation', 'it displays initial text header');

  // fill out address and submit
  // this will call geolocation api, ideally the external API would be stubbed out
  this.$('.address-input').val('boston')

  // trigger [enter] keypress to submit address
  var e = Ember.$.Event( "keypress", { which: 13 } );
  // NOTE: this is not working, ideally would use ember native DOM helpers instead of jQuery
  this.$('.address-input').trigger(e);
  assert.equal(this.$('h1').text().trim(), 'Now use the tools to draw the shape of your solar installation', 'it updates header after address');

  this.set('drawnShape', {type:'Feature', properties: [], geometry: []})
  // expect button to appear once drawnShape is set on component
  assert.equal(this.$('.submit-btn').length, 1, 'Button appears once geometry is set');



});
