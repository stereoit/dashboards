define(['underscore','backbone','models/kpi'], function (_, Backbone, KPIModel){
    var KPIsCollection = Backbone.Collection.extend({
        model: KPIModel,
        url: KPI_API,

        parse: function(data){
            return data.objects;
        },
    });
    return new KPIsCollection;
});
