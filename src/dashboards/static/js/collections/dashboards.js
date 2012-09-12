define(['underscore','backbone','models/dashboard'], function (_, Backbone, DashboardModel){
    var DashboardsCollection = Backbone.Collection.extend({
        model: DashboardModel,

        url: DASHBOARD_API,

        initialize: function(){
            console.log("DashboardsCollection initialized");
            console.log("API at "+this.url);
        },

        parse: function(data){
            console.log('SHIT '+JSON.stringify(data));
            return data.objects;
        },
    });
    return DashboardsCollection;
});
