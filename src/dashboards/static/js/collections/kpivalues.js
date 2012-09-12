define(['underscore','backbone','models/kpivalue'], function (_, Backbone, KPIValueModel){
    var KPIValuesCollection = Backbone.Collection.extend({
        model: KPIValueModel,
        url: KPIVALUE_API,
    });
    return new KPIValuesCollection;
});
