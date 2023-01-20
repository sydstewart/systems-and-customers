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
# from ..Searches.four_way_search import four_way_search
from ..Stats_Tables.Application_Areas import Application_Areas
from ..Stats_Tables.Customer_Types import Customer_Types
from ..Stats_Tables.Version_Summary import Version_Summary
from ..Searches.Use_kwargs import search_using_kwargs

class systems_and_accounts(systems_and_accountsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

# Login
    anvil.users.login_with_form()
    loggedinuser =  anvil.users.get_user()['email']
#     self.loggedinuser.text = loggedinuser
    user_type = anvil.users.get_user()['user_type']

#Last Refresh of Data   
    t = app_tables.last_date_refreshed.get(dateid =1 )
    self.last_refresh_date.text= t['last_date_refreshed']
    
#-------------------------------------------------------------------------
# Loading Dropdowns
#--------------------------------------------------------------------------------
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search(tables.order_by('CFApplicationArea'))})
    inusestatus = list({(r['InUseStatus']) for r in app_tables.suppported_products.search()})
    customertype = list({(r['Customer_Type']) for r in app_tables.suppported_products.search()})
    regions= list({(r['Location_c']) for r in app_tables.suppported_products.search()})
    version_level = list({(r['Version_Level']) for r in app_tables.suppported_products.search()})
    version = list({(r['Live_version_no']) for r in app_tables.suppported_products.search(tables.order_by('Live_version_no'))})
    DB_version = list({(r['Database_Version']) for r in app_tables.suppported_products.search(tables.order_by('Database_Version'))})
    os_version = list({(r['Operating_System']) for r in app_tables.suppported_products.search(tables.order_by('Operating_System'))})
    remote_access = list({(r['Remote_Access_Available']) for r in app_tables.suppported_products.search(tables.order_by('Remote_Access_Available'))})
    accounts = list({(r['Account']) for r in app_tables.suppported_products.search(tables.order_by('Account'))})
    
    self.apparea_drop_down.items =  [(str(row['application_area']), row) for row in app_tables.application_area.search(tables.order_by('application_area'))]
    self.in_use_drop_down.items = inusestatus
    self.version_level_dropdown.items = version_level
    self.interfaces_drop_down.items = [(str(row['Interface_Type']), row) for row in app_tables.interface_types.search(tables.order_by('Interface_Type'))]
    self.app_multi_select_drop_down.items = applications
    self.region_dropdown.items = regions
    self.customer_type_dropdown.items = customertype
    self.live_version_dropdown.items = version
    self.database_version_dropdown.items = DB_version
    self.operating_system_dropdown.items = os_version
    self.access_dropdown.items = remote_access
    self.account_dropdown.items= accounts
    
    
#Initial Search             
    results = app_tables.suppported_products.search()

    self.repeating_panel_1.items = results
#Hits
    self.hits_textbox.text = len(results)
    pass 
  
#--------------------------------------------------------------------
# Changes in Fields      
#-------------------------------------------------------------------

#Application Areas      
  def apparea_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    self.app_multi_select_drop_down.selected = None
    search_using_kwargs(self)
    pass
  
  def app_multi_select_drop_down_change(self, **event_args):
    """This method is called when the selected values change"""
    self.apparea_drop_down.selected_value = None
    search_using_kwargs(self)
    pass
  
# In Use Status
  def in_use_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)

# Versions
  def live_version_dropdown_change(self, **event_args):
    """This method is called when the selected values change"""
    self.version_level_dropdown.selected_value = None
    search_using_kwargs(self)
    pass 
  def version_level_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.live_version_dropdown.selected = None
    search_using_kwargs(self)
    pass 

# interfaces
  def interfaces_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass

  def NOT_interface_chkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    search_using_kwargs(self)
    pass

#Regions
  def region_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass
  
#Customer Types
  def customer_type_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass
#Database Versions  
  def database_version_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass
#Operating Sstems  
  def operating_system_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass
# Access
  def access_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass
# Account
  def account_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass
#-------------------------------------------------------------------------  
# Navigation side bar and top bar
#---------------------------------------------------------------------------
# Application_Areas summary
  def app_group_type_button_click(self, **event_args):
    """This method is called when the button is clicked"""
     
    open_form('Stats_Tables.Application_Areas')
    pass

# Open Map top bar
  def map_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Map')
    pass

#Open Map side menu
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Map')
    pass

#Version_Summary
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Version_Summary')
    dict_versions_group = anvil.server.call('versions')
#     self.repeating_panel_1.items = dict_versions_group
    pass

# Customer_Types Summary
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Customer_Types')
    dict_customer_type_summary = anvil.server.call('customer_type__summary')
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

#version_summary  
  def version_summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Version_Summary')
    dict_versions_group = anvil.server.call('versions')
    pass
#Regional Summary
  def region_summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Regional_Summary')
    pass
#Application Group Summary
  def application_group_summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Application_Groups')
    pass


# Interface Summary
  def interface_summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Interface_Types')
    pass
#InUuse Summary  
  def In_Use_Summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.In_Use_Summary')
    pass
# Database Version Summary
  def database_version_summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Database_Version_Summary')
    pass
# OS Summary
  def OS_Summary_Button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.OS_Summary')
    pass
#Access Summary
  def access_summary_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Stats_Tables.Access_Summary')
    pass

# Logout
  def logout_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.column_panel_3.clear()
    
    anvil.users.logout()
    
    anvil.users.login_with_form()
    open_form('systems_and_accounts')
  
# Clear All Search Criieria

  def clear_search_criteria_click(self, **event_args):
    """This method is called when the button is clicked"""
#Set all fileds to None    
    self.in_use_drop_down.selected_value = None
    self.interfaces_drop_down.selected_value = None
    self.apparea_drop_down.selected_value = None
    self.version_level_dropdown.selected_value= None
    self.NOT_interface_chkbox.checked = None
    self.app_multi_select_drop_down.selected = None
    self.region_dropdown.selected_value = None
    self.customer_type_dropdown.selected_value = None
    self.live_version_dropdown.selected = None
    self.database_version_dropdown.selected_value = None
    self.operating_system_dropdown.selected_value = None
    self.access_dropdown.selected_value = None
    self.account_dropdown.selected = None
    
    #Initial Search             
    results = app_tables.suppported_products.search()

    self.repeating_panel_1.items = results
    #Hits
    self.hits_textbox.text = len(results)
    pass
    






























