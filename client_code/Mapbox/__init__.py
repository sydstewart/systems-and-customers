from ._anvil_designer import MapboxTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import mapboxgl
import anvil.js
import anvil.http
from anvil.js.window import mapboxgl, MapboxGeocoder

class Mapbox(MapboxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.token  = "pk.eyJ1Ijoic3lkbmV5c3Rld2FydCIsImEiOiJjbGJ4aW10YzIwbjRsM3FwMzFtbmhrZ2I5In0.VOstRTDf2WwCOsCoB_VpxA"
    # Any code you write here will run before the form opens.
    anvil.server.call('get_markers')

  def mapbox_1_show(self, **event_args):
    """This method is called when the Spacer is shown on the screen"""
#     def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    #I defined my access token in the __init__
    mapboxgl.accessToken = self.token 

    #put the map in the spacer 
    self.mapbox = mapboxgl.Map({'container': anvil.js.get_dom_node(self.mapbox_1), 
                                'style': 'mapbox://styles/mapbox/streets-v11', #use the standard Mapbox style
                                'center': [0.1218, 52.2053], #center on Cambridge
                                'zoom': 11})
    
    self.marker = mapboxgl.Marker({'color': '#5a3fc0', 'draggable': True})
    self.marker.setLngLat([0.1218, 52.2053]).addTo(self.mapbox)
    locations = anvil.server.call('get_markers')
    for location in locations:
        print(location['coordinates'])
        print(location['placename'])
        lnglat = str(location['coordinates'])
        print(lnglat)
        self.marker.setLngLat(lnglat).addTo(self.mapbox)
        
    self.geocoder = MapboxGeocoder({'accessToken': mapboxgl.accessToken,
                                    'marker': False}) #we've already added a marker
    self.mapbox.addControl(self.geocoder)
     
#     self.mapbox.addControl(self.)
 
    self.geocoder.on('result', self.add_marker)
   
  def add_marker(self, result):
    print(result)
    #get the [longitude, latitude] coordinates from the JS object returned from 'result'
    lnglat = result['result']['geometry']['coordinates']
    placename = result['result']['place_name_en-GB']
    print(lnglat)
    print(placename)
    self.marker.setLngLat(lnglat).addTo(self.mapbox)
    anvil.server.call('save_geo', placename, lnglat)
#     self.marker.setLngLat([lnglat])
     







