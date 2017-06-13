
/*
*   photo id 를 구하는 곳
*/
var url_split = location.href.split('/');
var photo_id = url_split[url_split.length - 1];
var exif_url = '/result/data/' + photo_id;
var exif_data;
var gps_data = [];
var markers = [];

/*
*   map 설정
*/
var my_map;


// Json Data 가져오기
$.getJSON(exif_url, function(e_json){
    exif_data = e_json;
    exif_data.forEach(function(item, index, array){
        list = { lat : parseFloat(item.latitude), lng : parseFloat(item.longitude) , id: item.id};
        gps_data.push(list);
    });

    my_map = new google.maps.Map(document.getElementById('my_map'),{
        zoom: 17,
        center: {lat: 36.7989522, lng: 127.07493069999998 },
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
        zoomControl: true,
    });

    gps_data.forEach(function(item, index, array){
        markers.push(new google.maps.Marker({
            position : item,
            map : my_map,
            title: item.id.toString(),
        }));
    });

    markers.forEach(function(marker, index, array){
        marker.addListener('click', function(){
            var data = exif_data.filter(function(item, i, a){
                return item.id.toString() == marker.title;
            });

            var html_data = "<div class='exif_string' id='exif_camera_model'> Camera: " + data[0].camera_model +"</div>";
            html_data += "<div class='exif_string' id='exif_make'> Make: " + data[0].make +"</div>";
            html_data += "<div class='exif_string' id='exif_color'> Color: " + data[0].color +"</div>";
            html_data += "<div class='exif_string' id='exif_date_time'> Date Time: " + data[0].date_time +"</div>";
            html_data += "<div class='exif_string' id='exif_flash'> Flash: " + data[0].flash +"</div>";
            html_data += "<div class='exif_string' id='exif_focal_length'> Focal Length: " + data[0].focal_length +"</div>";
            html_data += "<div class='exif_string' id='exif_iso_speed'> ISO Speed: " + data[0].iso_speed +"</div>";
            html_data += "<div class='exif_string' id='exif_latitude'> Latitude: " + data[0].latitude +"</div>";
            html_data += "<div class='exif_string' id='exif_longitude'> Longitude: " + data[0].longitude +"</div>";
            html_data += "<div class='exif_string' id='exif_orientation'> Orientation: " + data[0].orientation +"</div>";

            document.getElementById('exif_info').innerHTML = html_data;
        });
    });

});