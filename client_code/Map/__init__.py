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
    self.app_area_dropdown.items = [(str(row['application_area']), row) for row in app_tables.application_area.search(tables.order_by('application_area'))]
    inusestatus = list({(r['InUseStatus']) for r in app_tables.suppported_products.search()})
    self.In_Use_Status_dropdown.items = inusestatus
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
      
      
  print( 'got db entries')  
  def marker_click(self, sender, **event_args):
      i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
      i.open(self.map, sender)
    
#   marker.add_event_handler("click", marker_click)
  def app_area_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
#     self.app_multi_select_drop_down.selected = None
#     self.in_use_2_drop_down.selected_value = None
#     self.map = GoogleMap
    
    self.map.clear()
    selectedapp = self.app_area_dropdown.selected_value
    selectedInUse = self.In_Use_Status_dropdown.selected_value
    print(selectedInUse)
    if selectedapp is not None:
        selectedapp = ('%' + selectedapp['application_area']  + '%')
        print(selectedapp)
        locations = anvil.server.call('get_locations',selectedapp)
    elif selectedInUse is not None and selectedapp is not None:
        locations = anvil.server.call('get_InUse_locations',selectedapp, selectedInUse)
    else:
        locations = anvil.server.call('get_all_locations')
    for location in locations:
      position = GoogleMap.LatLng(location['latitude'], location['longitude'])
      marker = GoogleMap.Marker(position=position)
      self.map.add_component(marker)
     
      marker.add_event_handler("click", self.marker_click)
      self.markers[marker] = location['Name'] + ' ' + location['InUseStatus']
    self.hits_textbox.text = len(locations) 
      
  print( 'got db entries')  
  def marker_click(self, sender, **event_args):
      i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
      i.open(self.map, sender)
#     for location in locations:
#         position = GoogleMap.LatLng(location['latitude'], location['longitude'])
#         marker = GoogleMap.Marker(position=position)
#         self.map.add_component(marker)
#         self.map.clear()

#     selectedapparea = self.app_area_dropdown.selected_value
#     selecttedinusestatus = self.In_Use_Status_dropdown.selected_value
# #     print(selectedapparea['application_area'])
#     if selectedapparea: # and not selecttedinusestatus:
#         selectedapp = ('%' + selectedapparea + '%')
#         locations = app_tables.suppported_products.search(CFApplicationArea = q.like(selectedapp))
#         print(locations['Name'])
#         self.map = GoogleMap()
#         for location in locations:
#           print(location['Name'])
#           position = GoogleMap.LatLng(location['latitude'], location['longitude'])
#           marker = GoogleMap.Marker(position=position)
#           self.map.add_component(marker)
 
#           marker.add_event_handler("click", self.marker_click)
#           self.markers[marker] = location['Name']
          
#   def marker_click(self, sender, **event_args):
#       i = GoogleMap.InfoWindow(content=Label(text=self.markers[sender]))
#       i.open(self.map, sender)
        
        #         applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
#         self.app_multi_select_drop_down.items = applications
#     elif selectedapparea and  selecttedinusestatus:
#         selectedapp = ('%' + selectedapparea['application_area'] + '%')
#         self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea = q.like(selectedapp), InUseStatus=selecttedinusestatus)
#         applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
#         self.app_multi_select_drop_down.items = applications
#     elif not selectedapparea and  selecttedinusestatus:   
#         self.repeating_panel_1.items = app_tables.suppported_products.search( InUseStatus=selecttedinusestatus)
#     else:
#         self.repeating_panel_1.items = app_tables.suppported_products.search()
#         self.hits_textbox.text = len(app_tables.suppported_products.search())
#     t = app_tables.last_date_refreshed.get(dateid =1 )
#     self.last_refresh_date.text= t['last_date_refreshed']
#     self.hits_textbox.text = len(self.repeating_panel_1.items)
    
  
  def In_Use_Status_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
#     self.apparea_dropdown.enabled = true
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    selectedapparea = self.apparea_dropdown.selected_value
    selecttedinusestatus = self.In_Use_Status_dropdown.selected_value
#     print(selectedapparea['application_area'])
    if selectedapparea and not selecttedinusestatus:
        selectedapp = ('%' + selectedapparea['application_area'] + '%')
        self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea = q.like(selectedapp))
        applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
        self.app_multi_select_drop_down.items = applications
    elif selectedapparea and  selecttedinusestatus:
        selectedapp = ('%' + selectedapparea['application_area'] + '%')
        self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea = q.like(selectedapp), InUseStatus=selecttedinusestatus)
        applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
        self.app_multi_select_drop_down.items = applications
    elif not selectedapparea and  selecttedinusestatus:   
        self.repeating_panel_1.items = app_tables.suppported_products.search( InUseStatus=selecttedinusestatus)
    else:
        self.repeating_panel_1.items = app_tables.suppported_products.search()
        self.hits_textbox.text = len(app_tables.suppported_products.search())
    t = app_tables.last_date_refreshed.get(dateid =1 )
    self.last_refresh_date.text= t['last_date_refreshed']
    self.hits_textbox.text = len(self.repeating_panel_1.items)
    pass
       

  def add_location_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Map_Location_Search')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('latLong')
    pass

  def search_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.map.clear()
    
    selectedapp = self.app_area_dropdown.selected_value
    selecttedinusestatus = self.In_Use_Status_dropdown.selected_value
    if selectedapp is not None:
        selectedapp = ('%' + selectedapp['application_area']  + '%')
        locations = anvil.server.call('get_locations',selectedapp)
    
    else:
        locations = anvil.server.call('get_all_locations')
        
#     elif selecttedinusestatus is not None:
#        search_criteria = CFApplicationArea=q.like(selectedapp)+ ',' +selecttedinusestatus
#        print(search_criteria)
#     locations = anvil.server.call('get_locations',search_criteria)    
    for location in locations:
      position = GoogleMap.LatLng(location['latitude'], location['longitude'])
      marker = GoogleMap.Marker(position=position)
      self.map.add_component(marker)
     
      marker.add_event_handler("click", self.marker_click)
      self.markers[marker] = location['Name']
    pass



