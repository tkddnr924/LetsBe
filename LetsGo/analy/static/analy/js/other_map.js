// photo id
var url_split = location.href.split('/');
var photo_id = url_split[url_split.length - 1];

// photo exif_list
var exif_url = '/result/data/' + photo_id;
var exif_data;
var gps_data = [];

// photo info
var photo_url = '/result/data/photo/';
var photo_data;
var url;

// map
var other_map;
var markers = [];

// custom control
var img_html;
var control_div;

$.getJSON(exif_url, function(e_json){
    // get exif json
    exif_data =e_json;
    exif_data.forEach(function(item, index, array){
        list = { lat : parseFloat(item.latitude), lng : parseFloat(item.longitude) , id: item.id};
        gps_data.push(list);
    });
    
    // create map
    other_map = new google.maps.Map(document.getElementById('other_map'),{
        zoom: 17,
        center: {lat: 36.7989522, lng: 127.07493069999998 },
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
        zoomControl: true,
    });
    
    // create marker
    gps_data.forEach(function(item, index, array){
        markers.push(new google.maps.Marker({
            position : item,
            map : other_map,
            title: item.id.toString(),
        }));
    });
    
    // create marker's click event
    markers.forEach(function(marker, index, array){
        marker.addListener('click', function(){
            var data = exif_data.filter(function(item, i, a){
                return item.id.toString() == marker.title;
            });
            
            if( control_div != null )
            {
                other_map.controls[google.maps.ControlPosition.TOP_LEFT].pop(control_div);
            }
            get_photo_url(marker.title);
        });
    });
});

function get_photo_url(photo_id){
    $.getJSON(photo_url+photo_id, function(p_json){
        var data = p_json;
        url = '/media/' + data.user_id + '/' + data.title;
        img_html = "<div class='col-lg-3'><img class='control_img' src='" + url + "'/></div>";
        
        control_div = document.createElement('div');
        var controlUI = document.createElement('div');
        var controlText = document.createElement('div');
        
        controlUI.className = "controlUI"
        control_div.appendChild(controlUI);
        
        controlText.innerHTML = img_html;
        
        controlUI.appendChild(controlText);
        control_div.index = 1;
        other_map.controls[google.maps.ControlPosition.TOP_LEFT].push(control_div);
    });
}