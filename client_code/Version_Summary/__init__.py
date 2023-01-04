from ._anvil_designer import Version_SummaryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Version_Summary(Version_SummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    dict_versions_group = anvil.server.call('versions')
    self.repeating_panel_1.items = dict_versions_group

    # Any code you write here will run before the form opens.
    
