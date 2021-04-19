import React from "react";
import {
  withGoogleMap,
  withScriptjs,
  GoogleMap,
  Marker,
  GoogleApiWrapper,
} from "react-google-maps";
// styles
import useStyles from "./styles";


const google = window.google

const { compose } = require("recompose");

const { MarkerWithLabel } = require("react-google-maps/lib/components/addons/MarkerWithLabel");

    var fireIcon = {
        path: 'M2 0c1 2-2 3-2 5s2 3 2 3c-.98-1.98 2-3 2-5s-2-3-2-3zm3 3c1 2-2 3-2 5h3c.4 0 1-.5 1-2 0-2-2-3-2-3z',
        fillColor: 'red',
        fillOpacity: 0.8,
        scale: 2.5,
        strokeColor: 'black',
        strokeWeight: 1
    };

    var medicalIcon = {
        path: 'M2 0v2h-2v4h2v2h4v-2h2v-4h-2v-2h-4z',
        fillColor: 'white',
        fillOpacity: 0.8,
        scale: 2.5,
        strokeColor: 'black',
        strokeWeight: 1
    };

const BasicMap = withScriptjs(
  withGoogleMap(() => (
    <GoogleMap
      defaultZoom={12}
 
      defaultCenter={{
        lat: parseFloat( -33.865143),
        lng: parseFloat( 151.209900),
      }}
    >
 <MarkerWithLabel
      position={{ lat:  -33.865170, lng:  151.209960}}
      labelStyle={{backgroundColor: "white", fontSize: "12px", padding: "2px"}}
      defaultIcon = {{medicalIcon}}
    >
      <div>Asthma</div>
    </MarkerWithLabel>

  <Marker
    title="The marker`s title will appear as a tooltip."
    name={'SOMA'}
    position={{ lat:  -33.885170, lng:  161.209960}} />
  
   <MarkerWithLabel
      position={{ lat:  -33.875170, lng:  151.309960}}
      labelStyle={{backgroundColor: "red", fontSize: "12px", padding: "2px"}}
    >
      <div>Hazard</div>
    </MarkerWithLabel>

    
   <MarkerWithLabel
      position={{ lat:  -33.845170, lng:  151.319960}}
      labelStyle={{backgroundColor: "yellow", fontSize: "12px", padding: "2px"}}
    >
      <div>Pneumonia</div>
    </MarkerWithLabel>
  
  <Marker
    name={'Dolores park'}
    position={{ lat:  -33.965170, lng:  151.201960}} />
  
    <Marker
    title="The marker`s title will appear as a tooltip."
    name={'SOMA'}
    position={{ lat:  -33.885170, lng:  161.2099960}} />
  <Marker
    name={'Dolores park'}
    position={{ lat:  -33.975170, lng:  151.301960}} />
  
    <Marker
    title="The marker`s title will appear as a tooltip."
    name={'SOMA'}
    position={{ lat:  -33.895170, lng:  161.259960}} />
  <Marker
    name={'Dolores park'}
    position={{ lat:  -33.975170, lng:  151.291960}} />
  
    <Marker
    title="The marker`s title will appear as a tooltip."
    name={'SOMA'}
    position={{ lat:  -34.885170, lng:  163.209960}} />
  <Marker
    name={'Dolores park'}
    position={{ lat:  -33.995170, lng:  151.401960}} />
  
  
    </GoogleMap>
  )),
);

export default function DefaultMaps() {
  var classes = useStyles();

  return (
    <div className={classes.mapContainer}>
      <BasicMap
        googleMapURL="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyB7OXmzfQYua_1LEhRdqsoYzyJOPh9hGLg"
        loadingElement={<div style={{ height: "inherit", width: "inherit" }} />}
        containerElement={<div style={{ height: "100%" }} />}
        mapElement={<div style={{ height: "100%" }} />}
      />
    </div>
  );
}
