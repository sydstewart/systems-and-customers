from ._anvil_designer import systems_and_accountsTemplate
from anvil import *
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.users
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, time , date , timedelta
from ..Searches.four_way_search import four_way_search
from ..Stats_Tables.Application_Areas import Application_Areas
from ..Stats_Tables.Customer_Types import Customer_Types
from ..Stats_Tables.Version_Summary import Version_Summary

class systems_and_accounts(systems_and_accountsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
#     mfa_login_with_form()
    loggedinuser =  anvil.users.get_user()['email']
#     self.loggedinuser.text = loggedinuser
    user_type = anvil.users.get_user()['user_type']
#     user_type = anvil.users.get_user()['user_type']
    # Any code you write here will run before the form opens.
#     anvil.server.call('listsystems'
#     open_form('systems_and_accounts')
    self.repeating_panel_1.items = app_tables.suppported_products.search()
    self.hits_textbox.text = len(app_tables.suppported_products.search())
    
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    inusestatus = list({(r['InUseStatus']) for r in app_tables.suppported_products.search()})
    customertype = list({(r['Customer_Type']) for r in app_tables.suppported_products.search()})
    regions= list({(r['Location_c']) for r in app_tables.suppported_products.search()})
    version_level = list({(r['Version_Level']) for r in app_tables.suppported_products.search()})
    print(regions)
    print(customertype)
    self.app_multi_select_drop_down.items = applications
    self.In_Use_Status_dropdown.items = inusestatus
    self.in_use_2_drop_down.items = inusestatus
    self.region_dropdown.items = regions
    self.customer_type_dropdown.items = customertype
    self.apparea_dropdown.items = [(str(row['application_area']), row) for row in app_tables.application_area.search(tables.order_by('application_area'))]
    self.apparea_1_dropdown.items = [(str(row['application_area']), row) for row in app_tables.application_area.search(tables.order_by('application_area'))]
    self.version_level_dropdown.items = version_level
    self.interfaces_dropdown.items = [(str(row['Interface_Type']), row) for row in app_tables.interface_types.search(tables.order_by('Interface_Type'))]
    #     self.region_multi_select_drop_down.items = regions

    t = app_tables.last_date_refreshed.get(dateid =1 )
    self.last_refresh_date.text= t['last_date_refreshed']
#     self.app_multi_select_drop_down.items = applicsations
#     dictsapps, total_rows = anvil.server.call('listsystems')
  
    
  def applications_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('applications')
    pass
# combinations dropdown search
  def app_multi_select_drop_down_change(self, **event_args):
    """This method is called when the selected values change"""
    self.apparea_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
    self.apparea_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
#     self.app_multi_select_drop_down.selected = None
#     self.in_use_2_drop_down.selected_value = None
    self.apparea_1_dropdown.selected_value = None
    self.customer_type_dropdown.selected_value = None
    self.region_dropdown.selected_value = None
    self.version_level_dropdown.selected_value = None
    self.text_search_box.text = None
    self.interfaces_dropdown.selected_value = None
    
    selectedapps = self.app_multi_select_drop_down.selected
    selecttedinusestatus2 = self.in_use_2_drop_down.selected_value
    if selecttedinusestatus2 and selectedapps  :
          self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea=q.any_of(*selectedapps), InUseStatus=selecttedinusestatus2)
    elif  not selecttedinusestatus2 and selectedapps  :
          self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea=q.any_of(*selectedapps))
    elif  selecttedinusestatus2 and not selectedapps  :
          self.repeating_panel_1.items = app_tables.suppported_products.search(InUseStatus=selecttedinusestatus2)

      
    self.hits_textbox.text = len(self.repeating_panel_1.items)
    pass
# refresh data
  def refresh_data_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('listsystems')
    self.repeating_panel_1.items = app_tables.suppported_products.search()
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    self.app_multi_select_drop_down.items = applications
    self.last_refresh_date.text= str(datetime.today()) 
    t = app_tables.last_date_refreshed.get(dateid =1 )
    t['last_date_refreshed'] = str(datetime.today() )
    pass
# AC list
  def app_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea = q.like ('%Anticoagulation%'))
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    self.app_multi_select_drop_down.items = applications
       
    t = app_tables.last_date_refreshed.get(dateid =1 )
    self.last_refresh_date.text= t['last_date_refreshed']
    pass
#single app area search
  def apparea_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    selectedapparea = self.apparea_dropdown.selected_value
    selecttedinusestatus = self.In_Use_Status_dropdown.selected_value
    
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    self.apparea_1_dropdown.selected_value = None
    self.customer_type_dropdown.selected_value = None
    self.region_dropdown.selected_value = None
    self.version_level_dropdown.selected_value = None
    self.text_search_box.text = None   
    self.interfaces_dropdown.selected_value = None
    
    
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

  def In_Use_Status_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
#     self.apparea_dropdown.enabled = true
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    selectedapparea = self.apparea_dropdown.selected_value
    selecttedinusestatus = self.In_Use_Status_dropdown.selected_value

#     self.apparea_dropdown.selected_value = None
#     self.In_Use_Status_dropdown.selected_value = None
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    self.apparea_1_dropdown.selected_value = None
    self.customer_type_dropdown.selected_value = None
    self.region_dropdown.selected_value = None
    self.version_level_dropdown.selected_value = None
    self.text_search_box.text = None
    self.interfaces_dropdown.selected_value = None
    
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
       
    t = app_tables.last_date_refreshed.get(dateid =1 )
    self.last_refresh_date.text= t['last_date_refreshed']
    pass

  def pivot_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Pivot')
    pass

  def in_use_2_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    self.apparea_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
    selectedapps = self.app_multi_select_drop_down.selected 
    selecttedinusestatus2 = self.in_use_2_drop_down.selected_value
    self.apparea_1_dropdown.selected_value = None
    self.customer_type_dropdown.selected_value = None
    self.region_dropdown.selected_value = None
    self.version_level_dropdown.selected_value = None
    self.text_search_box.text = None
    self.interfaces_dropdown.selected_value = None
    
    if selecttedinusestatus2 and selectedapps  :
          self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea=q.any_of(*selectedapps), InUseStatus=selecttedinusestatus2)
    elif  not selecttedinusestatus2 and selectedapps  :
          self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea=q.any_of(*selectedapps))
    elif  selecttedinusestatus2 and not selectedapps  :
          self.repeating_panel_1.items = app_tables.suppported_products.search(InUseStatus=selecttedinusestatus2)

    
    
    
    
    
    
#     if selecttedinusestatus :
#           self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea=q.any_of(*selectedapps), InUseStatus=selecttedinusestatus)
#     else:
#           self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea=q.any_of(*selectedapps))

    self.hits_textbox.text = len(self.repeating_panel_1.items)
    pass

  def stats_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Application_Area_Summary')
    pass

  def app_group_type_button_click(self, **event_args):
    """This method is called when the button is clicked"""
     
    open_form('Stats_Tables.Application_Areas')
    pass

  def map_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Map')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Map')
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Version_Summary')
    dict_versions_group = anvil.server.call('versions')
#     self.repeating_panel_1.items = dict_versions_group
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Customer_Types')
    dict_customer_type_summary = anvil.server.call('customer_type__summary')
    pass

  def customer_type_dropdown_change(self, **event_args):
    selectedcustomertype = self.customer_type_dropdown.selected_value
    selectedregion = self.region_dropdown.selected_value
    selectedapparea_1 = self.apparea_1_dropdown.selected_value
    
    self.apparea_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    self.text_search_box.text = None
    self.interfaces_dropdown.selected_value = None
    
    if  selectedapparea_1:
          self.apparea_dropdown.selected_value = None
          self.In_Use_Status_dropdown.selected_value = None
          selectedapp = ('%' + selectedapparea_1['application_area'] + '%')
    else:
          selectedapp = selectedapparea_1
    selected_version_level= self.version_level_dropdown.selected_value
    V = selectedapp
    X = selectedregion
    Y = selected_version_level
    Z = selectedcustomertype
    four_way_search(self,V, X,Y,Z)
   

  def region_dropdown_change(self, **event_args):
    selectedcustomertype = self.customer_type_dropdown.selected_value
    selectedregion = self.region_dropdown.selected_value
    selectedapparea_1 = self.apparea_1_dropdown.selected_value
    
    self.apparea_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    self.text_search_box.text = None
    self.interfaces_dropdown.selected_value = None
    
    if  selectedapparea_1:
          selectedapp = ('%' + selectedapparea_1['application_area'] + '%')
    else:
          selectedapp = selectedapparea_1
    selected_version_level= self.version_level_dropdown.selected_value
    V = selectedapp
    X = selectedregion
    Y = selected_version_level
    Z = selectedcustomertype
    four_way_search(self,V, X,Y,Z)
   




  def apparea_1_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    selectedcustomertype = self.customer_type_dropdown.selected_value
    selectedregion = self.region_dropdown.selected_value
    selectedapparea_1 = self.apparea_1_dropdown.selected_value
    
    self.apparea_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    self.text_search_box.text = None
    self.interfaces_dropdown.selected_value = None
    
    if  selectedapparea_1:
          selectedapp = ('%' + selectedapparea_1['application_area'] + '%')
    else:
          selectedapp = selectedapparea_1
    selected_version_level= self.version_level_dropdown.selected_value
    V = selectedapp
    X = selectedregion
    Y = selected_version_level
    Z = selectedcustomertype
    four_way_search(self,V, X,Y,Z)
    pass

  def version_level_dropdown_change(self, **event_args):
    selectedcustomertype = self.customer_type_dropdown.selected_value
    selectedregion = self.region_dropdown.selected_value
    selectedapparea_1 = self.apparea_1_dropdown.selected_value
    
    self.apparea_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    self.text_search_box.text = None
    self.interfaces_dropdown.selected_value = None
    
    if  selectedapparea_1:
          selectedapp = ('%' + selectedapparea_1['application_area'] + '%')
    else:
          selectedapp = selectedapparea_1
    selected_version_level= self.version_level_dropdown.selected_value
    V = selectedapp
    X = selectedregion
    Y = selected_version_level
    Z = selectedcustomertype
    four_way_search(self,V, X,Y,Z)
   



  def application_group_summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Application_Groups')
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Regional_Summary')
    pass

  def In_Use_Summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.In_Use_Summary')
    pass

  def logout_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    
    self.column_panel_3.clear()
    
    anvil.users.logout()
    
    anvil.users.login_with_form()
    open_form('systems_and_accounts')
    pass


  def text_search_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    if self.text_search_box.text:
          self.apparea_dropdown.selected_value = None
          self.In_Use_Status_dropdown.selected_value = None
          self.app_multi_select_drop_down.selected = None
          self.in_use_2_drop_down.selected_value = None
          self.apparea_1_dropdown.selected_value = None
          self.customer_type_dropdown.selected_value = None
          self.region_dropdown.selected_value = None
          self.version_level_dropdown.selected_value = None
          self.interfaces_dropdown.selected_value = None
          phrase = self.text_search_box.text
          
          self.repeating_panel_1.items = app_tables.suppported_products.search(q.any_of(
          Name=q.full_text_match(self.text_search_box.text),Account= q.full_text_match(phrase), \
          Live_version_no= q.full_text_match(phrase)))
    else:
         self.repeating_panel_1.items = app_tables.suppported_products.search()
        
    self.hits_textbox.text = len(self.repeating_panel_1.items)
    pass

  def interfaces_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.apparea_dropdown.selected_value = None
    self.In_Use_Status_dropdown.selected_value = None
    self.app_multi_select_drop_down.selected = None
    self.in_use_2_drop_down.selected_value = None
    self.apparea_1_dropdown.selected_value = None
    self.customer_type_dropdown.selected_value = None
    self.region_dropdown.selected_value = None
    self.version_level_dropdown.selected_value = None
    self.text_search_box.text = None
    selectedinterface = self.interfaces_dropdown.selected_value
    selectedinterface = ('%' + selectedinterface['Interface_Type'] + '%')
    self.repeating_panel_1.items = app_tables.suppported_products.search(Interfaces = q.like(selectedinterface), InUseStatus= 'Live')
    self.hits_textbox.text = len(self.repeating_panel_1.items)  
    pass




























