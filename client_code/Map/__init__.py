from ._anvil_designer import MapTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Map(MapTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.markers = {}
    # Any code you write here will run before the form opens.
    locations = anvil.server.call('get_locations')
    for location in locations:
      position = GoogleMap.LatLng(location['latitude'], location['longitude'])
      marker = GoogleMap.Marker(position=position)
      self.map.add_component(marker)
      
      marker.add_event_handler("click", self.marker_click)
      self.markers[marker] = location['location_name']
  print( 'got db entries')  
  def marker_click(self, sender, **event_args):
      i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
      i.open(self.map, sender)
    
#   marker.add_event_handler("click", marker_click)
      


  def add_location_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Map_Location_Search')
    pass

