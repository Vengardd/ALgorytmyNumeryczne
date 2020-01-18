
function initMap() {

  var path = [
			{lat: 10.001, lng: 10.001},
      {lat: 20.001, lng: 10.002},
      {lat: 30.001, lng: 10.003}];

  var elevator = new google.maps.ElevationService;

  displayPathElevation(path, elevator);
}

function displayPathElevation(path, elevator) {

  elevator.getElevationAlongPath({
    'path': path,
    'samples': 64
  }, plotElevation);
}

function download(elevations) {

		var headers = ['lat', 'lng', 'elevation']
    
    var heights = [];
    var latlng = [];
    var lng = [];
    
    var length = 0;
    
		let csvContent = "data:text/csv;charset=utf-8,"; 
    
		for (var elevationObject of elevations) {
  		heights.push(elevationObject.elevation);
      latlng.push(elevationObject.location);
      length += 1;
    }
    
    var data = [latlng, heights]
    
    
		let row = headers.join(",");         
    csvContent += row + "\r\n";
        
    for (i = 0; i < length; i++) {
          csvContent += latlng[i]  + ',' + heights[i] + '\r\n';
    }

    var encodedUri = encodeURI(csvContent);
    var link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "my_data.csv");
    document.body.appendChild(link);

    link.click();
}

function plotElevation(elevations, status) {

  download(elevations);

}