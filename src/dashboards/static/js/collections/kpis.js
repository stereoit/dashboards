define(['underscore','backbone','models/kpi'], function (_, Backbone, KPIModel){
    var KPIsCollection = Backbone.Tastypie.Collection.extend({
        model: KPIModel,
        url: KPI_API,

        initialize: function(){
            console.log("KPI Collection initialized ");
        },

    });
    return KPIsCollection;
});
