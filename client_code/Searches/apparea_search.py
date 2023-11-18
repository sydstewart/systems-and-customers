from anvil import *
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, time , date , timedelta
 
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

def apparea_search(self, selectedapparea,selectedinusestatus):
       
    if selectedapparea and not selectedinusestatus:
        selectedapparea = ('%' + selectedapparea['application_area'] + '%')
        locations = app_tables.suppported_products.search(CFApplicationArea=q.like(selectedapparea)) #anvil.server.call('get_locations',selectedapparea)

    elif selectedapparea and  selectedinusestatus:
        selectedapparea = ('%' + selectedapparea['application_area'] + '%')
        locations = app_tables.suppported_products.search(q.all_of(CFApplicationArea=q.like(selectedapparea), InUseStatus= (selectedinusestatus))) # anvil.server.call('get_InUse_locations',selectedapparea, selecttedinusestatus )

    elif not selectedapparea and  selectedinusestatus:   
#         locations = app_tables.suppported_products.search( InUseStatus=selecttedinusestatus)
       locations = app_tables.suppported_products.search(InUseStatus=selectedinusestatus) #anvil.server.call('get_all_locations_with_In_Use_alone', selectedinusestatus) 
    else:
        locations = app_tables.suppported_products.search() #anvil.server.call('get_all_locations')
        self.hits_textbox.text = len(app_tables.suppported_products.search())

    self.hits_textbox.text = len(locations)
    for location in locations:
      position = GoogleMap.LatLng(location['latitude'], location['longitude'])
      marker = GoogleMap.Marker(position=position)
      self.map.add_component(marker)
     
      marker.add_event_handler("click", self.marker_click)
      self.markers[marker] = location['Name'] + ' ' + location['InUseStatus'] + ' ' + location['Live_version_no']
      
#     print( 'got db entries')  
    def marker_click(self, sender, **event_args):
      i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
      i.open(self.map, sender) 
   
