//this file allws us to configure mappings to paths

require.config({
  paths: {
    jquery: 'libs/jquery/jquery-min',
    underscore: 'libs/underscore/underscore.amd',
    backbone: 'libs/backbone/backbone.amd',
    backbonetastypie: 'libs/backbone/backbone-tastypie',
    text: 'libs/require/text',
    base: 'base',
/*
    bootstrap: 'libs/bootstrap/bootstrap',
    bootstrap-collapse: 'libs/boostrap/bootstrap-collapse',
*/
  }
});

require(['views/app', ], function(AppView){
  console.log(KPI_API);
  console.log(KPIVALUE_API);
  console.log(PALETTE_API);
  console.log(DASHBOARD_API);
  var app_view = new AppView();
});
