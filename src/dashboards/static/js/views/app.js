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

    initialize: function() {
        console.log("Dashboard App initialized");
        this.config = new Config();
        this.dashboards = new Dashboards();

        this.dashboards.on('reset', this.addAll, this);
        this.dashboards.fetch();
        console.log("Dashboards fetched");
        this.render();
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
      this.dashboards.each(this.addOne);
    },

    addOne: function(dashboard) {
      console.log("Dashboard App addOne");
      var view = new DashboardView({model: dashboard});
      this.$("#dashboardslist").append(view.render().el);
    },

  });

  return AppView;
});
