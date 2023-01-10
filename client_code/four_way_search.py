import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

def four_way_search(self, V, X, Y, Z):
    selectedcustomertype = self.customer_type_dropdown.selected_value
    selectedregion = self.region_dropdown.selected_value
    selectedapparea_1 = self.apparea_1_dropdown.selected_value
    if  selectedapparea_1:
          selectedapp = ('%' + selectedapparea_1['application_area'] + '%')
    else:
          selectedapp = selectedapparea_1
    selected_version_level= self.version_level_dropdown.selected_value
    V = selectedapp
    X = selectedregion
    Y = selected_version_level
    Z = selectedcustomertype
    print(V, X, Y ,Z)
#     results = anvil.server.call('four_way_search',selectedapp, selectedregion, selected_version_level, selectedcustomertype)
    
    if V and X and Y and Z:
       results = app_tables.suppported_products.search(CFApplicationArea = q.like(V ),Location_c = X,Version_Level= Y, Customer_Type = Z, InUseStatus= 'Live')
        
    elif   V and not X and not Y and not Z:
       results = app_tables.suppported_products.search(CFApplicationArea = q.like(V ), InUseStatus= 'Live')
    elif  not  V and X and not Y and not Z:    
        results = app_tables.suppported_products.search( Location_c = X,  InUseStatus= 'Live')
    elif  not  V and not X and Y and not Z:    
        results = app_tables.suppported_products.search(Version_Level= Y,  InUseStatus= 'Live')
    elif  not  V and not X and not Y and  Z:    
        results = app_tables.suppported_products.search(Customer_Type = Z,  InUseStatus= 'Live')
    
    elif   V and X and not Y and not Z:
       results = app_tables.suppported_products.search(CFApplicationArea = q.like(V ), Location_c = X, InUseStatus= 'Live')
    elif   V and not X and Y and not Z:
       results = app_tables.suppported_products.search(CFApplicationArea = q.like(V ), Version_Level= Y, InUseStatus= 'Live')
    elif   V and not X and not Y and  Z:
       results = app_tables.suppported_products.search(CFApplicationArea = q.like(V ), Customer_Type = Z, InUseStatus= 'Live')
    elif   not V and X and  Y and not Z:
       results = app_tables.suppported_products.search( Location_c = X, Version_Level= Y, InUseStatus= 'Live')
    elif   not V and not X and  Y and Z:
       results = app_tables.suppported_products.search(Version_Level= Y, Customer_Type = Z, InUseStatus= 'Live')
    elif   not V and X and not Y and  Z:
       results = app_tables.suppported_products.search(Location_c = X,Customer_Type = Z, InUseStatus= 'Live')
    
    
    elif   V and X and Y and not Z:
       results = app_tables.suppported_products.search(CFApplicationArea = q.like(V ), Location_c = X, Version_Level= Y, InUseStatus= 'Live')
    elif  not  V and X and Y and Z:
       results = app_tables.suppported_products.search(Location_c = X, Version_Level= Y,Customer_Type = Z, InUseStatus= 'Live')
    elif  V and not X and Y and Z:
       results = app_tables.suppported_products.search(CFApplicationArea = q.like(V ),Version_Level= Y ,Customer_Type = Z,  InUseStatus= 'Live')
    elif  V and  X and not Y and Z:
       results = app_tables.suppported_products.search(CFApplicationArea = q.like(V ),Location_c = X ,Customer_Type = Z,  InUseStatus= 'Live')
    
    
    
    else:   
        results = app_tables.suppported_products.search(InUseStatus= 'Live')
 
    
    self.repeating_panel_1.items = results
    self.hits_textbox.text = len(self.repeating_panel_1.items)
    pass
