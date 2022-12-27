import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import plotly.express as px
import geopandas as gpd

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def update_location(location_name, latitude, longitude):
  location = app_tables.suppported_products.get(Name= location_name)
  location['latitude'] = latitude
  location['longitude'] = longitude
#   app_tables.suppported_products.add_row(Name=location_name,latitude=latitude,longitude=longitude)
  
@anvil.server.callable
def get_locations(selectedapp):
   
  return app_tables.suppported_products.search(CFApplicationArea=q.like(selectedapp))

@anvil.server.callable
def get_InUse_locations(selectedapp,selectedInUse):
   
  return app_tables.suppported_products.search(q.all_of(CFApplicationArea=q.like(selectedapp), InUseStatus= (selectedInUse)))

@anvil.server.callable
def get_all_locations():
  return app_tables.suppported_products.search()