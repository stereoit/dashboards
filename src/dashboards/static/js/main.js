//this file allws us to configure mappings to paths

require.config({
  paths: {
    jquery: 'libs/jquery/jquery-min',
    underscore: 'libs/underscore/underscore.amd',
    backbone: 'libs/backbone/backbone.amd',
    text: 'libs/require/text',
/*
    bootstrap: 'libs/bootstrap/bootstrap',
    bootstrap-collapse: 'libs/boostrap/bootstrap-collapse',
*/
  }
});

require(['views/app', ], function(AppView){
  var app_view = new AppView();
});
