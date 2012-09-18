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
                this.model.on('initialized', this.modelInitialized, this);
            },

            modelInitialized: function (){
                console.log('Dashboard View - model fully initilized');
                this.model.on('change', this.render, this);
                this.render();
            },

            render: function(){
                console.log("Dashboard View render()",this.model.toJSON());
                var data = this.model.toJSON();
                data.kpi = this.model.kpi.toJSON();
                data.palette = this.model.palette.toJSON();
                data.values = this.model.values.toJSON();
                this.$el.html(this.template(data));
                return this;
            },

        });
        return  DashboardView;
    }
);
