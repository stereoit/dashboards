define(['jquery','underscore','backbone','models/kpi','models/colorpalette','collections/kpivalues'], function($, _, Backbone, KPI, Palette, Values){
    var DashboardModel = Backbone.Tastypie.Model.extend({

        initialize: function() {
            console.log("Dashboard Model initialized ",this);
            this.isInitialized = false;

            this.kpi = new KPI();
            this.kpi.url = this.url()+'kpi';
            this.kpi._loaded = false;

            this.palette = new Palette();
            this.palette.url = this.url()+'palette';
            this.palette._loaded = false;

            this.values = new Values();
            this.values.url = this.url()+'values';
            this.values._loaded = false;

            var self = this;
            this.kpi.fetch({success: function(model){ self.kpi._loaded = true; self.checkInitialization() } });
            this.palette.fetch({success: function() { self.palette._loaded = true; self.checkInitialization() } });
            this.values.fetch({success: function() { self.values._loaded = true; self.checkInitialization() } });
        },

        checkInitialization: function(){
            if ( ! this.kpi._loaded || ! this.palette._loaded || ! this.values._loaded ) {
                return;
            } else {

                this.kpi.off('change', this.checkInitialization);
                this.palette.off('change', this.checkInitialization);
                this.values.off('change', this.checkInitialization);

                console.log('Dashboard Model initialization complete - refreshing every ',this.kpi.get('granularity'),' seconds', this);

                this.trigger('initialized'); // view listens for this

            }
        },


    });
    return DashboardModel;
});
