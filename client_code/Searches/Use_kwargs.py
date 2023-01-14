import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .Searches import Module1
#
#    Module1.say_hello()
#

def search_using_kwargs(self):
      
    search1 = self.in_use_drop_down.selected_value
    search2 = None    #Name
    search3 = self.interfaces_drop_down.selected_value
    search4 = self.apparea_drop_down.selected_value
    search5 = self.version_level_drop_down.selected_value
    search6 = self.NOT_interface_chkbox
    kwargs ={}

    if search1:
        kwargs['InUseStatus'] = search1  #q.like('%'+ search1['InUseStatus'] + '%')
#     kwargs['InUseStatus'] ='Live'
    if search2:
       kwargs["Name"] = q.like('%'+ search2 +'%')
    if search3:
         selectedinterface = ('%' + search3['Interface_Type'] + '%')
         kwargs['Interfaces'] = q.like('%'+ selectedinterface + '%') 
    if search4:
         selectedapparea = ('%' + search4['application_area'] + '%')
         kwargs['CFApplicationArea'] = q.like('%'+ selectedapparea + '%') 
    if search5:
        kwargs['Version_Level'] = search5
    if search6 == True:
       
            selectedinterface = ('%' + search3['Interface_Type'] + '%')
            kwargs['Interfaces'] = q.not_(q.like('%'+ selectedinterface + '%'))

             
    results = app_tables.suppported_products.search(**kwargs)
#     namevalue =  '%' + 'Alaska' + '%' # 'Alaska Native Medical Center - AC System'
#     versionvalue = '%'+'CF 8'+'%'
#     kwargs = {'Name': namevalue}
#     print(kwargs)
#     results = app_tables.suppported_products.search(q.all_of(**kwargs)) #q.like(**kwargs))
    self.repeating_panel_1.items = results
    self.text_box_1.text = len(results)
