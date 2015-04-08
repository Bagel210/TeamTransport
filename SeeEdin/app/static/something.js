var first_lat = $('#my-div').attr('data-first-lat');
var first_lng = $('#my-div').attr('data-first-lng');
var last_lat = $('#my-div').attr('data-last-lat');
var last_lng = $('#my-div').attr('data-last-lng');
var map = L.map('map').setView([55.94440, -3.18632], 13);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
var startMarker = L.AwesomeMarkers.icon({ icon: 'flag', markerColor: 'green' });
var endMarker = L.AwesomeMarkers.icon({ icon: 'flag', markerColor: 'red' });
var start = L.marker([first_lat, first_lng], { icon: startMarker }).addTo(map);
start.bindPopup("Start");
var end = L.marker([last_lat, last_lng], { icon: endMarker }).addTo(map);
end.bindPopup("End");
map.fitBounds([[first_lat, first_lng], [last_lat, last_lng]]);
//# sourceMappingURL=something.js.map