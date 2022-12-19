from ._anvil_designer import Application_Area_SummaryTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Application_Area_Summary(Application_Area_SummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
#     self.repeating_panel_1.items = app_tables.application_area.search(tables.order_by('application_area'))
    # Any code you write here will run before the form opens.
    
    dfgroups =anvil.server.call('groupareas')
    self.repeating_panel_1.items = dfgroups
    
    dfinuse = anvil.server.call('groupinuse')
    self.repeating_panel_2.items = dfinuse
    
    dictssingleapp  = anvil.server.call('groupinsinleapparea')
    self.repeating_panel_3.items = dictssingleapp
    
    dictssingleapp_group  = anvil.server.call('appgrouptype')
    self.repeating_panel_4.items = dictssingleapp_group
    
  def return_to_search_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('systems_and_accounts')
    pass

