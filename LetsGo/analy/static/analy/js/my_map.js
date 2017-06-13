
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
        list = { lat : parseFloat(item.latitude), lng : parseFloat(item.longitude) };
        gps_data.push(list);
    });

    my_map = new google.maps.Map(document.getElementById('my_map'),{
        zoom: 17,
        center: {lat: 36.7989522, lng: 127.07493069999998 },
        scrollwheel: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        scaleControl: true,
    });

    gps_data.forEach(function(item, index, array){
        markers.push(new google.maps.Marker({
            position : item,
            map : my_map,
        }));
    });

});
