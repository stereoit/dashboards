// base app
define([
  'jquery',
  'underscore',
  'backbone',
  'backbonetastypie'
], function ($, _, Backbone) {

  var AppConfig = Backbone.View.extend({
      initialize: function(){
          console.log('AppConfig initialized');
      },
  });
  return AppConfig;
})
