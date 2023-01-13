from ._anvil_designer import TestTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Test(TestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    search1 = 'CF 7'  # Version No
    search2 = None    #Name
    search3 =  'Out'  # interface
    kwargs ={}

    if search1:
         kwargs['Live_version_no'] = q.like('%'+ search1 + '%')
    kwargs['InUseStatus'] ='Live'
    if search2:
       kwargs["Name"] = q.like('%'+ search2 +'%')
    if search3:
         kwargs['Interfaces'] = q.like('%'+ search3 + '%') 
    print(kwargs)
#     kwargs = { 'Name': q.like('%'+'Native' +'%' ), 'Live_version_no': q.like('%'+ 'CF 8' + '%')}
             
    results = app_tables.suppported_products.search(**kwargs)
#     namevalue =  '%' + 'Alaska' + '%' # 'Alaska Native Medical Center - AC System'
#     versionvalue = '%'+'CF 8'+'%'
#     kwargs = {'Name': namevalue}
#     print(kwargs)
#     results = app_tables.suppported_products.search(q.all_of(**kwargs)) #q.like(**kwargs))
    self.repeating_panel_1.items = results
    self.text_box_1.text = len(results)
    pass 
#     if self.text_box_1.text:
#        namesearch  = '%' + self.text_box_1.text + '%'
#        searchclause = 'Name= q.like(namesearch)'
#     else:
#         searchclause = ''
#     results ={}  
#     accounts = app_tables.suppported_products.search()
#     for row in accounts:
#          if row['Account'] in searchclause:
#             results.append(row)
      
      
#     self.repeating_panel_1.items = results
#     # Any code you write here will run before the form opens.
    

#   def text_box_1_pressed_enter(self, **event_args):
#     """This method is called when the user presses Enter in this text box"""
    
#     if self.text_box_1.text:
#        namesearch  = '%' + self.text_box_1.text + '%'
#        searchclause = 'Name= q.like(namesearch)'
#     else:
#         searchclause = ''
#     results ={}  
#     accounts = app_tables.suppported_products.search()
#     for row in accounts:
#          if row['Account'] in namesearch:
#             results.append(row)
      
      


