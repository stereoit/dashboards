define(['jquery','underscore','backbone','models/kpi','models/colorpalette','collections/kpivalues'], function($, _, Backbone, KPI, Palette, Values){
    var DashboardModel = Backbone.Tastypie.Model.extend({

        initialize: function() {
            console.log("Dashboard Model initialized ",this);
            this.isInitialized = false;

            this.kpi = new KPI();
            this.kpi.url = this.url()+'kpi';
            this.kpi.on('change', this.checkInitilization, this);

            this.palette = new Palette();
            this.palette.url = this.url()+'palette';
            this.palette.on('change', this.checkInitilization, this);

            this.values = new Values();
            this.values.url = this.url()+'values';
            this.values.on('change', this.checkInitilization, this);

            this.kpi.fetch();
            this.palette.fetch();
            this.values.fetch();
        },

        checkInitilization: function(){
            console.log('Dashboard Model checkInitilization');
            if (typeof this.kpi === "undefined" || typeof this.palette === "undefined" || typeof this.values  === "undefined" ) {
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

        toJSON: function(options){
            return $.extend( 
                    {},
                    //Backbone.Tastypie.Model.prototype.toJSON.call(this, options),
                    //this.kpi.toJSON(),
                    //this.palette.toJSON(),
                    this.values.toJSON()
                    );
        },

    });
    return DashboardModel;
});
