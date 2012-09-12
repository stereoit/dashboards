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
        //this.render();
    },

    render: function() {
        this.$el.html(this.dashboardsTemplate());
        return this;
    },

    doubleClick: function(){
        alert("Double clicked");
    },

    // Add all items in the **Todos** collection at once.
    addAll: function() {
      Dashboards.each(this.addOne);
    },

    // Add a single todo item to the list by creating a view for it, and
    // appending its element to the `<ul>`.
    addOne: function(dashboard) {
      var view = new DashboardView({model: dashboard});
      this.$("#dashboard-list").append(view.render().el);
    },

  });

  return AppView;
});
