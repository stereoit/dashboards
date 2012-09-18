define(['jquery','underscore','backbone','models/kpi','models/colorpalette','collections/kpivalues'], function($, _, Backbone, KPI, Palette, Values){
    var DashboardModel = Backbone.Tastypie.Model.extend({

        initialize: function() {
            console.log("Dashboard Model initialized ",this);
            this.isInitialized = false;

            this.kpi = new KPI();
            this.kpi.url = this.url()+'kpi';
            this.kpi._loaded = false;
            this.kpi.on('change', this.checkInitialization, this);

            this.palette = new Palette();
            this.palette.url = this.url()+'palette';
            this.palette._loaded = false;
            this.palette.on('change', this.checkInitialization, this);

            this.values = new Values();
            this.values.url = this.url()+'values';
            this.values._loaded = false;
            this.values.on('change', this.checkInitialization, this);

            var self = this;
            this.kpi.fetch({success: function(model) { self.kpi._loaded = true}});
            this.palette.fetch({success: function(model) { self.palette._loaded = true}});
            this.values.fetch({success: function(model) { self.values._loaded = true}});
        },

        checkInitialization: function(){
            console.log('Dashboard Model checkInitilization', this);
            if ( ! this.kpi._loaded || ! this.palette._loaded || ! this.values._loaded ) {
                console.log('checkInitilization did not pass');
                return;
            } else {
                console.log('Dashboard Model initilizaiton complete');

                this.kpi.off('change', this.checkInitilization);
                this.palette.off('change', this.checkInitilization);
                this.values.off('change', this.checkInitilization);


                console.log('Dashboard Model refreshing every ',this.kpi.get('granularity'),' seconds', this);

                this.isInitialized = true;   // view can also check for this attribute
                this.trigger('initialized'); // view listens for this

            }
        },


    });
    return DashboardModel;
});
