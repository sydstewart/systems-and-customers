from ._anvil_designer import PivotTemplate
from anvil import *
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Pivot(PivotTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    records = app_tables.suppported_products.search()
    self.pivot_1.data_items = [dict(list(r)) for r in records]
    # Any code you write here will run before the form opens.
    
