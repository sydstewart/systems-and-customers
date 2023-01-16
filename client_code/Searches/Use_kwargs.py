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
#     search2 = self.text_search_box.text
    search3 = self.interfaces_drop_down.selected_value
    search4 = self.apparea_drop_down.selected_value
#     search5 = self.version_level_drop_down.selected_value
    search6 = self.NOT_interface_chkbox.checked
    search7 = self.app_multi_select_drop_down.selected
    search8 = self.region_dropdown.selected_value
    search9 = self.customer_type_dropdown.selected_value
    search10 = self.live_version_dropdown.selected   
#     search11= self.AC_Non_AC_drop_down.selected_value
    if search4:
       self.app_multi_select_drop_down.selected =None
    kwargs ={}
    if search7:
       self.apparea_drop_down.selected_value = None
   
    if search1:
#         self.text_search_box.text = None
        kwargs['InUseStatus'] = search1  #q.like('%'+ search1['InUseStatus'] + '%')
#     kwargs['InUseStatus'] ='Live'

    if search3:
#          self.text_search_box.text = None
         selectedinterface = ('%' + search3['Interface_Type'] + '%')
         kwargs['Interfaces'] = q.like('%'+ selectedinterface + '%') 
    if search4 and not search7:
#          self.text_search_box.text = None
         selectedapparea = ('%' + search4['application_area'] + '%')
         kwargs['CFApplicationArea'] = q.like('%'+ selectedapparea + '%') 
#     if search5:
# #         self.text_search_box.text = None
#         kwargs['Version_Level'] = search5
#         self.live_version_drop_down.selected = None
    if search6 == True and search3:
#          self.text_search_box.text = None
         selectedinterface = ('%' + search3['Interface_Type'] + '%')
         kwargs['Interfaces'] = q.not_(q.like('%'+ selectedinterface + '%'))
    
    if  not search4 and search7:
       kwargs['CFApplicationArea']=q.any_of(*search7)
    if search8:
#       self.text_search_box.text = None
      kwargs['Location_c'] = search8
    
    if search10:
        kwargs['Live_version_no'] = q.any_of(*search10)
#         self.version_level_drop_down.selected_value =None
        
#     if search11:
#         kwargs['AC_Non_AC'] = search11
        
#     if search2:
#           self.repeating_panel_1.items = app_tables.suppported_products.search(q.any_of(
#           Name=q.full_text_match(search2),Account= q.full_text_match(search2), \
#           Live_version_no= q.full_text_match(search2),CFApplicationArea= q.full_text_match('%' + search2 + '%')))
#           self.text_box_1.text = len(self.repeating_panel_1.items)
#     else:  
    results = app_tables.suppported_products.search(**kwargs)

    self.repeating_panel_1.items = results
    self.hits_textbox.text  = len(results)
