from ._anvil_designer import Map_Location_SearchTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Map_Location_Search(Map_Location_SearchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
#     self.search_name.text = 'London'
#     self.location_name.text = 'London'
    self.latitude  = self.longitude = None
    self.drop_down_1.items = applications =list({(r['Name']) for r in app_tables.suppported_products.search()})
    
    
  def enable_search_btn(self, **event_args):
    """This method is called when the button is clicked"""
    self.search_btn.enabled = self.search_name.text != "" and self.location_name.text != ""
    pass

  def search_for_location(self, **event_args):
    
    results = GoogleMap.geocode(address=self.location_name.text)
#     print(results)
    if not results:
        Alert(' No Location found - Edit Search Text')
    result = results[0].geometry.location
#     print(result)
    marker = GoogleMap.Marker(position=result)
    self.map.add_component(marker)
    self.map.center = result
    self.map.zoom = 11
    self.map.visible = True
    self.add_location_btn.enabled = True
    self.latitude = result.lat(marker)
    self.longitude = result.lng(result)

         

  def add_location_btn_click(self, **event_args):
    """This method is called when the button is clicked"""

    line1 = self.location_name.text
    line2 = 'Latitude = ' + str(self.latitude) 
    line3 = 'Longitude = ' + str(self.longitude)
    line4 = 'Please copy Lat and Long to CRM account'
    message = line1 +'\n' + line2 + '\n' + line3 + '\n' + '\n' + line4
    alert(message)
#     anvil.server.call('update_location',self.drop_down_1.selected_value,self.latitude ,self.longitude)
#     open_form('Map')
    pass

  def go_to_map_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Map')
    pass

  def drop_down_1_change(self, **event_args):
    self.location_name.text = self.drop_down_1.selected_value
    pass





