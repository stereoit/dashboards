define(['underscore','backbone','models/collorpalette'], function (_, Backbone, ColorPaletteModel){
    var ColorPalletesCollection = Backbone.Collection.extend({
        model: ColorPaletteModel,
        url: PALETTE_API,
    });
    return new ColorPalletesCollection;
});
