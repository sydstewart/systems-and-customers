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
    df =anvil.server.call('groupareas')
    
    self.repeating_panel_1.items = df