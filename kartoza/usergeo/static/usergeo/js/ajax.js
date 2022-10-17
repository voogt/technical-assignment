$.ajax({
    type: 'GET',
    url: 'get/ajax/get_users',
    data: {},
    success: function (response){
        console.log(response)
        var map = L.map('map').setView([-26.42376054350511, 28.47690524650157], 14);
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        var count = Object.keys(response["users"]).length;

        var myIcon = L.icon({
            iconUrl: 'static/usergeo/images/marker-icon.png',
            iconSize: [40, 40]
        });

        for(var x = 0; x < count; x++){
            var marker = L.marker(
                [response["users"][x]["lat"], response["users"][x]["lon"]],
                {icon: myIcon}
            ).addTo(map);
            var username = response["users"][x]["username"];
            var first_name = response["users"][x]["first_name"];
            var phone = response["users"][x]["phone"];
            var email = response["users"][x]["email"];
            var last_name = response["users"][x]["last_name"];
            var street_addr = response["users"][x]["street_address"];
            var city = response["users"][x]["city"];
            html = "<p>User Profile</p><ul> <li>Name: "+ first_name +" "+ last_name +"</li> <li>Email: "+ email +"</li> <li>Phone: "+ phone +"</li> <li>Address: "+ street_addr +" "+ city +"</li>  </ul>";
            marker.bindPopup(html);
        }
    },
    error: function (response){
        alert("error")
        console.log(response)
    }
});

