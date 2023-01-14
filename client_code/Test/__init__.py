from ._anvil_designer import TestTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Searches.Use_kwargs import search_using_kwargs
class Test(TestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   
    applications =list({(r['CFApplicationArea']) for r in app_tables.suppported_products.search()})
    inusestatus = list({(r['InUseStatus']) for r in app_tables.suppported_products.search()})
    customertype = list({(r['Customer_Type']) for r in app_tables.suppported_products.search()})
    regions= list({(r['Location_c']) for r in app_tables.suppported_products.search()})
    version_level = list({(r['Version_Level']) for r in app_tables.suppported_products.search()})
    
    self.apparea_drop_down.items =  [(str(row['application_area']), row) for row in app_tables.application_area.search(tables.order_by('application_area'))]
    self.in_use_drop_down.items = inusestatus
    self.version_level_drop_down.items = version_level
    self.interfaces_drop_down.items = [(str(row['Interface_Type']), row) for row in app_tables.interface_types.search(tables.order_by('Interface_Type'))]

    
    search1 = self.in_use_drop_down.selected_value
    search2 = None    #Name
    search3 = self.in_use_drop_down.selected_value
    search4 = self.apparea_drop_down.selected_value
    search5 = self.version_level_drop_down.selected_value
    kwargs ={}

    if search1:
         kwargs['InUseStatus'] = search1
#     kwargs['InUseStatus'] ='Live'
    if search2:
       kwargs["Name"] = q.like('%'+ search2 +'%')
    if search3:
         kwargs['Interfaces'] = search3
    if search4:
         selectedapparea = ('%' + search4['application_area'] + '%')
         kwargs['CFApplicationArea'] = q.like('%'+ selectedapparea + '%') 
    if search5:
      kwargs['Version_Level'] = search5
             
    results = app_tables.suppported_products.search(**kwargs)

    self.repeating_panel_1.items = results
    self.text_box_1.text = len(results)
    pass 

      
      

  def apparea_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass

  def in_use_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)

  def version_level_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass

  def interfaces_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    search_using_kwargs(self)
    pass

  def NOT_interface_chkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    search_using_kwargs(self)
    pass








