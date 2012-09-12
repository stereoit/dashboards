define(['underscore','backbone','models/dashboard'], function (_, Backbone, DashboardModel){
    var DashboardsCollection = Backbone.Collection.extend({
        model: DashboardModel,

        url: DASHBOARD_API,
    });
    return new DashboardsCollection;
});
