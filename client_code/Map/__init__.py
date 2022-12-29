from ._anvil_designer import MapTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..apparea_search import apparea_search
from ..multi_search import multi_search

class Map(MapTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.app_area_dropdown.items = [(str(row['application_area']), row) for row in app_tables.application_area.search(tables.order_by('application_area'))]
    inusestatus = list({(r['InUseStatus']) for r in app_tables.suppported_products.search()})
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    self.In_Use_Status_dropdown.items = inusestatus
    self.in_use_2_dropdown.items = inusestatus
    self.app_multi_select_drop_down_1.items = applications
    self.markers = {}
#     markersyd = []
#     if self.app_area_dropdown.selected_value:
#         selectedapparea =self.app_area_dropdown.selected_value
#         selectedapp = ('%' + selectedapparea  + '%')
#     else:
#     selectedapp = ('%' + 'Anticoagulation'  + '%')
#     # Any code you write here will run before the form opens.
    locations = anvil.server.call('get_all_locations' )
    self.hits_textbox.text = len(locations) 
    for location in locations:
      position = GoogleMap.LatLng(location['latitude'], location['longitude'])
      marker = GoogleMap.Marker(position=position)
      self.map.add_component(marker)
     
      marker.add_event_handler("click", self.marker_click)
      self.markers[marker] = location['Name'] + ' ' + location['InUseStatus']
      
      
#   print( 'got db entries')  
  def marker_click(self, sender, **event_args):
      i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
      i.open(self.map, sender)

#single app area search
  def app_area_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.app_multi_select_drop_down_1.selected = None
    self.in_use_2_dropdown.selected_value = None
    self.map.clear()
    selectedapparea = self.app_area_dropdown.selected_value
    selecttedinusestatus = self.In_Use_Status_dropdown.selected_value
#     print(selectedapparea['application_area'])
#     selectedapparea  = ('%' + selectedapparea['application_area'] + '%')
    apparea_search(self, selectedapparea,selecttedinusestatus)
      
      
  def In_Use_Status_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
#     self.apparea_dropdown.enabled = true
    self.app_multi_select_drop_down_1.selected = None
    self.in_use_2_dropdown.selected_value = None
    selectedapparea = self.app_area_dropdown.selected_value
    selecttedinusestatus = self.In_Use_Status_dropdown.selected_value
    self.map.clear()
    apparea_search(self, selectedapparea,selecttedinusestatus)
#     print(selectedapparea['application_area'])
#     if selectedapparea and not selecttedinusestatus:
#         selectedapp = ('%' + selectedapparea['application_area'] + '%')
#         locations= app_tables.suppported_products.search(CFApplicationArea = q.like(selectedapp))
# #         applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
# #         self.app_multi_select_drop_down.items = applications
#     elif selectedapparea and  selecttedinusestatus:
#         selectedapp = ('%' + selectedapparea['application_area'] + '%')
#         locations = app_tables.suppported_products.search(CFApplicationArea = q.like(selectedapp), InUseStatus=selecttedinusestatus)
# #         applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
# #         self.app_multi_select_drop_down.items = applications
#     elif not selectedapparea and  selecttedinusestatus:   
#         locations = app_tables.suppported_products.search( InUseStatus=selecttedinusestatus)
    
#     elif not selectedapparea and  not selecttedinusestatus:
#         locations = app_tables.suppported_products.search()
#     if locations:
#         self.hits_textbox.text = len(locations)
# #     t = app_tables.last_date_refreshed.get(dateid =1 )
# #     self.last_refresh_date.text= t['last_date_refreshed']
#         self.hits_textbox.text = len(locations)
#         for location in locations:
#           position = GoogleMap.LatLng(location['latitude'], location['longitude'])
#           marker = GoogleMap.Marker(position=position)
#           self.map.add_component(marker)
        
#           marker.add_event_handler("click", self.marker_click)
#           self.markers[marker] = location['Name'] + ' ' + location['InUseStatus']
          
# #         print( 'got db entries')  
#         def marker_click(self, sender, **event_args):
#           i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
#           i.open(self.map, sender)  
      
      
   # combinations dropdown search
  def app_multi_select_drop_down_1_change(self, **event_args):
    """This method is called when the selected values change"""
    self.app_area_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
    selectedapps = self.app_multi_select_drop_down_1.selected 
    selecttedinusestatus2 = self.in_use_2_dropdown.selected_value
    self.map.clear()
    multi_search(self, selecttedinusestatus2, selectedapps)
#     if selecttedinusestatus2 and selectedapps  :
#           locations= anvil.server.call('get_all_locations_with_two',selectedapps, selecttedinusestatus2 )
      
#     elif  not selecttedinusestatus2 and selectedapps  :
#           locations = anvil.server.call('get_all_locations_with_selectedapps_alone', selectedapps)
# #       
#     elif  selecttedinusestatus2 and not selectedapps  :
#           locations = anvil.server.call('get_all_locations_with_selecttedinusestatus2_alone', selecttedinusestatus2)
# #       
#     elif  not selecttedinusestatus2 and not selectedapps: 
#             locations = anvil.server.call('get_all_locations')
    
#     if locations:  
#           self.hits_textbox.text = len(locations)
#           for location in locations:
#             position = GoogleMap.LatLng(location['latitude'], location['longitude'])
#             marker = GoogleMap.Marker(position=position)
#             self.map.add_component(marker)
          
#             marker.add_event_handler("click", self.marker_click)
#             self.markers[marker] = location['Name'] + ' ' + location['InUseStatus']
            
# #           print( 'got db entries')  
#           def marker_click(self, sender, **event_args):
#             i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
#             i.open(self.map, sender)  
#     pass
 
      
   
  def in_use_2_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.app_area_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
    selectedapps = self.app_multi_select_drop_down_1.selected 
    selecttedinusestatus2 = self.in_use_2_dropdown.selected_value
    self.map.clear()
    multi_search(self, selecttedinusestatus2, selectedapps)
#     if selecttedinusestatus2 and selectedapps  :
#         locations= anvil.server.call('get_all_locations_with_two',selectedapps, selecttedinusestatus2 )  
              
#     elif  not selecttedinusestatus2 and selectedapps  :
#           locations = anvil.server.call('get_all_locations_with_selectedapps_alone', selectedapps)
        
#     elif  selecttedinusestatus2 and not selectedapps  :
#           locations = anvil.server.call('get_all_locations_with_selecttedinusestatus2_alone', selecttedinusestatus2)
          
#     elif  not selecttedinusestatus2 and not selectedapps: 
#             locations = anvil.server.call('get_all_locations')
    
#     if locations:
#           self.hits_textbox.text = len(locations)
#           for location in locations:
#             position = GoogleMap.LatLng(location['latitude'], location['longitude'])
#             marker = GoogleMap.Marker(position=position)
#             self.map.add_component(marker)
          
#             marker.add_event_handler("click", self.marker_click)
#             self.markers[marker] = location['Name'] + ' ' + location['InUseStatus']
            
# #           print( 'got db entries')  
#           def marker_click(self, sender, **event_args):
#             i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
#             i.open(self.map, sender)  
#           pass
       
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      


  def add_location_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Map_Location_Search')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('latLong')
    pass






