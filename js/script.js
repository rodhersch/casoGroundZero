var loc={lat:-33.43323,lng:-70.65861};
const getLocations = () => {
    fetch('https://www.datos.gov.co/resource/g373-n3yy.json')
    .then(response => response.json())
    .then(locations => {
        let locationsInfo = []
        
        locations.forEach(location => {
            let locationData = {
                position:{lat:location.punto.coordinates[1],lng:location.punto.coordinates[0]},
                name:location.nombre_sede                
            }
            locationsInfo.push(locationData)
           
        })
     
        dibujarMapa2(loc, locationsInfo)
    })
}



const dibujarMapa2 = (loc, locationsInfo) => {
    let map = new google.maps.Map(document.getElementById('map'),{
         zoom: 4,
         center: loc
     })
 
     let marker = new google.maps.Marker({
         position: loc,
         title: 'Casa Central'
     })
     marker.setMap(map)
 
     let markers = locationsInfo.map(place => {
         return new google.maps.Marker({
             position: place.position,
             map: map,
             title: place.name
         })
     })
 }
window.addEventListener('load',getLocations)