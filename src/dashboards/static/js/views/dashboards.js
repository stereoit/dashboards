define([
    'jquery',
    'underscore',
    'backbone',
    ], function ($, _, Backbone) {
        var DashboardView = Backbone.View.extend({

            tagName: "li",

        });
        return  DashboardView;
    }
);
