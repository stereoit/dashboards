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
        var shit = new Config();
        console.log("Dashboard App initialized");

        Dashboards.on('reset', this.AddAll, this);
        Dashboards.on('all', this.render, this);
        Dashboards.fetch();
        console.log("Dashboards fetched");
    },

    render: function() {
        console.log("Dashboard App render");
        this.$el.html(this.dashboardsTemplate());
        return this;
    },

    doubleClick: function(){
        alert("Double clicked");
    },

    addAll: function() {
      console.log("Dashboard App addAll");
      Dashboards.each(this.addOne);
    },

    addOne: function(dashboard) {
      console.log("Dashboard App addOne");
      var view = new DashboardView({model: dashboard});
      this.$("#dashboard-list").append(view.render().el);
    },

  });

  return AppView;
});
