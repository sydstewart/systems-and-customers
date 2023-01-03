from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

def multi_search(self, selecttedinusestatus2, selectedapps):
    if selecttedinusestatus2 and selectedapps  :
          locations= anvil.server.call('get_all_locations_with_two',selectedapps, selecttedinusestatus2 )
      
    elif  not selecttedinusestatus2 and selectedapps  :
          locations = anvil.server.call('get_all_locations_with_selectedapps_alone', selectedapps)
#       
    elif  selecttedinusestatus2 and not selectedapps  :
          locations = anvil.server.call('get_all_locations_with_In_Use_alone', selecttedinusestatus2)
#       
    elif  not selecttedinusestatus2 and not selectedapps: 
            locations = anvil.server.call('get_all_locations')
    
    if locations:  
          self.hits_textbox.text = len(locations)
          for location in locations:
            position = GoogleMap.LatLng(location['latitude'], location['longitude'])
            marker = GoogleMap.Marker(position=position)
            self.map.add_component(marker)
          
            marker.add_event_handler("click", self.marker_click)
            self.markers[marker] = location['Name'] + ' ' + location['InUseStatus'] + ' ' + location['Live_version_no']
            
#           print( 'got db entries')  
          def marker_click(self, sender, **event_args):
            i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
            i.open(self.map, sender)  
