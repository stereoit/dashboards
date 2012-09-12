define([
    'jquery',
    'underscore',
    'backbone',
    'text!templates/dashboardsView.html'
    ], function ($, _, Backbone, dashboardTemplate) {
        var DashboardView = Backbone.View.extend({

            tagName: "div",

            className: "row span4 shadowed",

            template: _.template(dashboardTemplate),

            initialize: function(){
                console.log('Dashboard view intialized ', this.model);
                this.model.on('change', this.render, this);
            },

            render: function(){
                this.$el.html(this.template(this.model.toJSON()));
                console.log("DashboardView render ", this.$el.html());
                return this;
            },

        });
        return  DashboardView;
    }
);
