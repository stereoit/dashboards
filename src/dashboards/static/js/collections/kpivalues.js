define(['underscore','backbone','models/kpivalue'], function (_, Backbone, KPIValueModel){
    var KPIValuesCollection = Backbone.Tastypie.Collection.extend({
        model: KPIValueModel,
        url: KPIVALUE_API,

    });
    return KPIValuesCollection;
});
