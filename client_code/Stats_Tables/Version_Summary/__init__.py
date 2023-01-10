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
    dict_versions_group, version_count = anvil.server.call('versions')
    self.repeating_panel_1.items = dict_versions_group
    self.text_box_1.text = version_count
    dict_versions_summary = anvil.server.call('versions_summary')
    self.repeating_panel_2.items = dict_versions_summary
    # Any code you write here will run before the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('systems_and_accounts')
    pass

