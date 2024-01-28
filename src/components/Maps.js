import React from 'react'
import { GoogleMap, useJsApiLoader } from '@react-google-maps/api';

const containerStyle = {
  display: 'flex',
  flexDirection: 'row',
  width: '1000px',
  height: '500px',
  marginLeft: '50px', // Adjust the margin as needed
  border: 'solid'
};

const mapStyle = {
  flex: 1,
  minheight: '100%',
};

const otherComponentStyle = {
  flex: 1,
  // Add any additional styling for the other component
};

const center = {
  lat: 45.5,
  lng: -73.7
};

function Maps() {
  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: "AIzaSyBYWMsFh2HFK_2D4Lvf5H9_vPrKKKOz6q8"
  })

  const [map, setMap] = React.useState(null)

  const onLoad = React.useCallback(function callback(map) {
    // This is just an example of getting and using the map instance!!! don't just blindly copy!
    map.setCenter(center);
    map.setZoom(10);

    setMap(map)
  }, [])

  const onUnmount = React.useCallback(function callback(map) {
    setMap(null)
  }, [])

  return isLoaded ? (
    <div style={containerStyle}>
      <GoogleMap
        mapContainerStyle={mapStyle}
        center={center}
        zoom={10}
        onLoad={onLoad}
        onUnmount={onUnmount}
      >
        {/* Child components, such as markers, info windows, etc. */}
        <></>
      </GoogleMap>
      <div style={otherComponentStyle}>
        {/* Your other component goes here */}
      </div>
    </div>
  ) : <></>;
}


export default React.memo(Maps)