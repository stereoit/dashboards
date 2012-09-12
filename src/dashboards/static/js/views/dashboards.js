define([
    'jquery',
    'underscore',
    'backbone',
    'text!templates/dashboardsView.html'
    ], function ($, _, Backbone, dashboardTemplate) {
        var DashboardView = Backbone.View.extend({

            tagName: "li",

            template: _.template(dashboardTemplate),

            initilize: function(){
                this.model.on('change', this.render, this);
            },

            render: function(){
                this.$el.html(this.template(this.model.toJSON()));
            },

        });
        return  DashboardView;
    }
);
