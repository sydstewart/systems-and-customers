from ._anvil_designer import Customer_TypesTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Customer_Types(Customer_TypesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    dict_customer_type_group = anvil.server.call('customer_type__summary')
    self.repeating_panel_1.items = dict_customer_type_group
    # Any code you write here will run before the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('systems_and_accounts')
    pass

