from ._anvil_designer import Map_Location_SearchTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Map_Location_Search(Map_Location_SearchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def enable_search_btn(self, **event_args):
    """This method is called when the button is clicked"""
    self.search_btn.enabled = self.search_name.text != "" and self.location_name.text != ""
    pass

  def search_for_location(self, **event_args):
    results = GoogleMap.geocode(address=self.search_name.text)
    result = results[0].geometry.location
    print(result)
    pass


