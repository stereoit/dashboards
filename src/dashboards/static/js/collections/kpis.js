define(['underscore','backbone','models/kpi'], function (_, Backbone, KPIModel){
    var KPIsCollection = Backbone.Collection.extend({
        model: KPIModel,
        url: KPI_API,
    });
    return new KPIsCollection;
});
