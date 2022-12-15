from ._anvil_designer import systems_and_accountsTemplate
from anvil import *
import anvil.server

class systems_and_accounts(systems_and_accountsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    applicsations = anvil.server.call('listsystems')
    self.app_multi_select_drop_down.items = anvil.server.call('listsystems')

    self.repeating_panel_1.items = anvil.server.call('listsystems')

  def applications_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('applications')
    pass

