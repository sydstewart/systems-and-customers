from ._anvil_designer import Regional_SummaryTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Regional_Summary(Regional_SummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    dfgroups =anvil.server.call('groupareas')
    self.repeating_panel_1.items = dfgroups
    # Any code you write here will run before the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('systems_and_accounts')
    pass

