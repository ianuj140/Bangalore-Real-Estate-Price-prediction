function getBathValue() {
    var list_of_Bathrooms = document.getElementsByName("bath");
    for (var i in list_of_Bathrooms) {
        if (list_of_Bathrooms[i].checked) {
            return parseInt(i) + 1;       //indexing in an array starts from 0;
        }
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    var list_of_BHK = document.getElementsByName("bhk");
    for (var i in list_of_BHK) {
        if (list_of_BHK[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}

function get_estimated_price() {
    var sqft = document.getElementById("sqft_id");
    var location = document.getElementById("location_id");
    var bhk = getBHKValue();
    var bath = getBathValue();
    var estprice = document.getElementById("estimate_price_id")
    var url = "http://127.0.0.1:5000/predict_home_price"; 
    
    $.post(url, {
        totalsqft: parseFloat(sqft.value),
        location: location.value,
        bhk: bhk,
        bath: bath,
     }, function (data) {
         estprice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
    });
}

function populate() {
    var url = "http://127.0.0.1:5000/get_location_names"; 
    $.get(url, function (data) {
        if (data) {
            var locations = data.locations;
            $('#location_id').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#location_id').append(opt);
            }
        }
    });
}
window.onload = populate;