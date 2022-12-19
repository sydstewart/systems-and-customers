from ._anvil_designer import MapTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Map(MapTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    results = GoogleMap.geocode(address="Cambridge, UK")

    m = Marker(position=results[0].geometry.location)
    map.add_component(m)
  