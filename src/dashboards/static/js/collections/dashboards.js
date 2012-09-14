define(['underscore','backbone','models/dashboard'], function (_, Backbone, DashboardModel){
    var DashboardsCollection = Backbone.Tastypie.Collection.extend({
        model: DashboardModel,

        url: DASHBOARD_API,

        initialize: function(){
            console.log("DashboardsCollection initialized");
            console.log("API at "+this.url);
        },

    });
    return DashboardsCollection;
});
