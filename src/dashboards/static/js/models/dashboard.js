define(['underscore','backbone'], function(_, Backbone){
    var DashboardModel = Backbone.Model.extend({

        initialize: function() {
            console.log("Dashboard Model initialized "+JSON.stringify(this.attributes));
        },
    });
    return DashboardModel;
});
