define(['underscore','backbone'], function(_, Backbone){
    var KPIModel = Backbone.Tastypie.Model.extend({

        initialize: function () {
            console.log("KPI Model initialized ", this.attributes);
        },
    });
    return KPIModel;
});
