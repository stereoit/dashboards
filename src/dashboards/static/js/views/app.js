define([
  'jquery',
  'underscore',
  'backbone',
  'collections/dashboards',
  'views/dashboards',
  'text!templates/dashboards.html',
  'base'
  ], function($, _, Backbone, Dashboards, DashboardView, dashboardsTemplate, Config ){
  var AppView = Backbone.View.extend({

    el: "#dashboardsapp",

    dashboardsTemplate: _.template(dashboardsTemplate),

    events: {
        "dblclick #adddashboard"  : "doubleClick"
    },

    dashboards: undefined,

    initialize: function() {
        var config = new Config();
        dashboards = new Dashboards();
        console.log("Dashboard App initialized");
        this.render();

        dashboards.on('reset', this.addAll, this);
        dashboards.fetch();
        console.log("Dashboards fetched");
    },

    render: function(event) {
        console.log("Dashboard App render", event);
        this.$el.html(this.dashboardsTemplate());
        return this;
    },

    doubleClick: function(){
        alert("Double clicked");
    },

    addAll: function() {
      console.log("Dashboard App addAll ", this);
      dashboards.each(this.addOne);
    },

    addOne: function(dashboard) {
      console.log("Dashboard App addOne");
      var view = new DashboardView({model: dashboard});
      this.$("#dashboardslist").append(view.render().el);
    },

  });

  return AppView;
});
