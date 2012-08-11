/**
 * This code periodically calls the ``update_kpi``  url to generate new values
 * for KPI objects. It parses the `poll_next` variable and reschedules the next
 * call to the url.
 */


var http = require("http");
var fetch_url = 'http://127.0.0.1:8000/update-kpis/';

( function update_kpis () {

    console.log('calling %s', fetch_url)
    http.get(fetch_url, function(response) {
        console.log(response.statusCode)
        response.on('data', function (chunk) {
            var data = JSON.parse(chunk);
            var next_poll = data['next_poll'] * 1000;
            console.log('updated kpis: ' + data['updated_kpis'] + 
                ' next_poll: ' + next_poll + 's'); 
            setTimeout(update_kpis, next_poll);
        });
    }).on('error', function(e) {
          console.log("Got error: " + e.message);
    });
})()
