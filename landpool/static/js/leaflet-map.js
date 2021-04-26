// var map declear
var map = L.map('map', {
    zoomControl: false
}).setView([28.1392,83.85335], 18);
var scale = L.control.scale().addTo(map); //scale contorl of the map

// base layer (tilelayer as a variable)
var osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 25,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var Satellite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; Esri &mdash; Source: Esri,',
    minZoom: 1,
    maxZoom: 17,
}).addTo(map);

var watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    subdomains: 'abcd',
    minZoom: 1,
    maxZoom: 19,
    ext: 'jpg'
});

var mapBox = L.tileLayer('https://api.tiles.mapbox.com/styles/v1/{username}/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    username: 'iamtekson',
    id: 'cjwhym7s70tae1co8zf17a3r5',
    accessToken: 'pk.eyJ1IjoiaWFtdGVrc29uIiwiYSI6ImNqdjV4YzI4YjB0aXk0ZHBtNnVnNWxlM20ifQ.FjQJyCTodXASYtOK8IrLQA'
});

var baselayer = {
    "Open Street Map": osm,
    "Satellite Imagery": Satellite,
    "Water Color": watercolor,
    "mapBox map": mapBox,
}

// default popup features
function popupContents(e){
    $('#sidebar-layer-control').slideDown();
    $('.sidebar-header h5').html('<h5>Information about the feature</h5>');
    $('.sidebar-layer-control-main-body').hide();
    $('.lat').show().html('<b>Latitude : </b>'+ e.latlng.lat);
    $('.long').show().html('<b>longitude : </b>' + e.latlng.lng);
    $('.sidebar-info').show();
    $('#sidebar-layer-control .btn-info').show();
}
