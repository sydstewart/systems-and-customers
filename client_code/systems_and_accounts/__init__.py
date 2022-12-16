from ._anvil_designer import systems_and_accountsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, time , date , timedelta

class systems_and_accounts(systems_and_accountsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
#     anvil.server.call('listsystems')
    self.repeating_panel_1.items = app_tables.suppported_products.search()
    self.hits_textbox.text = len(app_tables.suppported_products.search())
    
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    inusestatus = list({(r['InUseStatus']) for r in app_tables.suppported_products.search()})
    self.app_multi_select_drop_down.items = applications
    self.In_Use_Status_dropdown.items = inusestatus
    
    self.apparea_dropdown.items = [(str(row['application_area']), row) for row in app_tables.application_area.search(tables.order_by('application_area'))]
   

    t = app_tables.last_date_refreshed.get(dateid =1 )
    self.last_refresh_date.text= t['last_date_refreshed']
#     self.app_multi_select_drop_down.items = applicsations
#     dictsapps, total_rows = anvil.server.call('listsystems')
    
  def applications_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('applications')
    pass

  def app_multi_select_drop_down_change(self, **event_args):
    """This method is called when the selected values change"""
    selectedapps = self.app_multi_select_drop_down.selected 
    self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea=q.any_of(*selectedapps))
    pass

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

  def ac_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea = q.like ('%Anticoagulation%'))
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    self.app_multi_select_drop_down.items = applications
       
    t = app_tables.last_date_refreshed.get(dateid =1 )
    self.last_refresh_date.text= t['last_date_refreshed']
    pass

  def apparea_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    selectedapparea = self.apparea_dropdown.selected_value
    print(selectedapparea['application_area'])
    selectedapp = ('%' + selectedapparea['application_area'] + '%')
    self.repeating_panel_1.items = app_tables.suppported_products.search(CFApplicationArea = q.like(selectedapp))
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    self.app_multi_select_drop_down.items = applications
       
    t = app_tables.last_date_refreshed.get(dateid =1 )
    self.last_refresh_date.text= t['last_date_refreshed']
    self.hits_textbox.text = len(self.repeating_panel_1.items)
    pass

  def In_Use_Status_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    selectedapparea = self.apparea_dropdown.selected_value
    selecttedinusestatus = self.In_Use_Status_dropdown.selected_value
    print(selectedapparea['application_area'])
    selectedapp = ('%' + selectedapparea['application_area'] + '%')
    self.repeating_panel_1.items = app_tables.suppported_products.search(q.all_of(CFApplicationArea = q.like(selectedapp), InUseStatus = selecttedinusestatus))
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    self.app_multi_select_drop_down.items = applications
       
    t = app_tables.last_date_refreshed.get(dateid =1 )
    self.last_refresh_date.text= t['last_date_refreshed']
    pass






