from ._anvil_designer import systems_and_accountsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class systems_and_accounts(systems_and_accountsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
#     anvil.server.call('listsystems')
    self.repeating_panel_1.items = app_tables.suppported_products.search()
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    self.app_multi_select_drop_down.items = applications
    
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
    self.last_refresh_date.text 
    pass



