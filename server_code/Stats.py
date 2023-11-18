import anvil.users
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import pandas as pd
import numpy as np
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

#Region Summary
@anvil.server.callable
def groupareas():
# Get an iterable object with all the rows in my_table
    all_records = app_tables.suppported_products.search(InUseStatus='Live')
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'CFApplicationArea': r['CFApplicationArea'], 'Name': r['Name'], 'Account': r['Account'], 'InUse':r['InUseStatus'], 'Region':r['Location_c']}
            for r in all_records]
    
    df = pd.DataFrame.from_dict(dicts)
#     print(df)
#     group_by_region = df.groupby('Region')['Name'].count()
#     group_by_region = group_by_region.sort_values(['Region'], ascending=False)['Name']
#     print(group_by_region) 


    df = df.groupby('Region')['Name'].count() \
                             .reset_index(name='count') \
                             .sort_values(['count'], ascending=False)
    df['sumsystems'] = df['count'].sum()
    df['%'] =(df['count'] * 100)/df['sumsystems']
    df['%'] = df['%'].map('{:,.0f}'.format)    
    df['%'] = df['%'].astype(int)

    df.loc['Total', 'count']= df['count'].sum()
    df.loc['Total', '%']= df['%'].sum()
    df = df.fillna("")
    
    dictsregions = df.to_dict(orient='records')
    
    return dictsregions
  
@anvil.server.callable
def groupinuse():
# Get an iterable object with all the rows in my_table
    all_records = app_tables.suppported_products.search()
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'CFApplicationArea': r['CFApplicationArea'], 'Name': r['Name'], 'Account': r['Account'], 'InUse':r['InUseStatus'], 'Region':r['Location_c']}
            for r in all_records]
    
    df1 = pd.DataFrame.from_dict(dicts)
#     print(df)
#     group_by_region = df.groupby('Region')['Name'].count()
#     group_by_region = group_by_region.sort_values(['Region'], ascending=False)['Name']
#     print(group_by_region) 


    df1 = df1.groupby('InUse')['Name'].count() \
                             .reset_index(name='count') \
                             .sort_values(['count'], ascending=False)
    df1['sumsystems'] = df1['count'].sum()
    df1['%'] =(df1['count'] * 100)/df1['sumsystems']
    df1['%'] = df1['%'].map('{:,.0f}'.format)    
    df1['%'] = df1['%'].astype(int)
#     df.loc['Column_Total']= df.sum(numeric_only=True, axis=0)
#     df.append(pd.Series(df.sum(),name='Total'))
#     df.loc['Total', :] = df.sum().values
    df1.loc['Total', 'count']= df1['count'].sum()
    df1.loc['Total', '%']= df1['%'].sum()
    df1 = df1.fillna("")
    
    dictsinuse = df1.to_dict(orient='records')
    
    return dictsinuse
# App area groups  
@anvil.server.callable
def groupinsinleapparea():  
#   singleapps = [(str(row['application_area']), row) for row in app_tables.application_area.search(tables.order_by('application_area'))]
  singleapps = app_tables.application_area.search()
  df3 = pd.DataFrame() 
  for r  in singleapps:
#      print((r['application_area']))
     apparea1 = r['application_area']
     apparea2 = ('%' + apparea1 + '%')
#      print(apparea1)
     supported_products = app_tables.suppported_products.search(CFApplicationArea = q.like (apparea2),InUseStatus='Live')
     no_of_systems = len(supported_products)
     
     new_row = {'Application_Area': apparea1, 'Count':no_of_systems}
   
     df3 = df3.append(new_row, ignore_index=True)
     
  print(df3)
  df3.sort_values(by=['Count'], ascending=False,inplace = True)
  df3['sumsystems'] = df3['Count'].sum()
  df3['%'] =(df3['Count'] * 100)/df3['sumsystems']
  df3['%'] = df3['%'].map('{:,.1f}'.format)    
  df3['%'] = df3['%'].astype(float)
  df3['Count'] = df3['Count'].astype(int)
  df3.loc['Total', 'Count']= df3['Count'].sum()
  df3.loc['Total', '%']= df3['%'].sum()
  df3 = df3.fillna("")
  
  dictssingleapp = df3.to_dict(orient='records')
  print(dictssingleapp)
  return dictssingleapp

@anvil.server.callable
def appgrouptype():  
  app_group = list(set([(r['app_group']) for r in app_tables.application_area.search()]))
  print(app_group)
  df3 = pd.DataFrame()
  for r in app_group:
     print (r)
     appareas = app_tables.application_area.search(app_group = r)
     
     for row in appareas:
            apparea1 = row['application_area']
            print(apparea1)
            apparea2 = ('%' + apparea1 + '%')
            supported_products = app_tables.suppported_products.search(CFApplicationArea = q.like (apparea2),InUseStatus='Live')
            no_of_systems = len(supported_products)
            new_row = {'App_Group': row['app_group'], 'Count':no_of_systems}
            df3 = df3.append(new_row, ignore_index=True)
     
  print(df3)
  df3 = df3.groupby('App_Group')['Count'].sum() \
                             .reset_index(name='Count') \
                             .sort_values(['Count'], ascending=False)
  print(df3)
#   df3.sort_values(by=['Count'], ascending=False,inplace = True)
  df3['sumsystems'] = df3['Count'].sum()
  df3['%'] =(df3['Count'] * 100)/df3['sumsystems']
  df3['%'] = df3['%'].map('{:,.1f}'.format)    
  df3['%'] = df3['%'].astype(float)
  df3['Count'] = df3['Count'].astype(int)
  df3.loc['Total', 'Count']= df3['Count'].sum()
  df3.loc['Total', '%']= df3['%'].sum()
  df3 = df3.fillna("")
  print(df3)
  dictssingleapp_group = df3.to_dict(orient='records')
  print(dictssingleapp_group)
  return dictssingleapp_group
#   dictssingleapp = df3.to_dict(orient='records')
#   print(dictssingleapp)
#   return dictssingleapp
#   app_group_type = 
#   singleapps = app_tables.application_area.search()
#   df3 = pd.DataFrame() 
#   for r  in singleapps:
# #      print((r['application_area']))
#      apparea1 = r['application_area']
#      apparea2 = ('%' + apparea1 + '%')
# #      print(apparea1)
#      supported_products = app_tables.suppported_products.search(CFApplicationArea = q.like (apparea2),InUseStatus='Live')
#      no_of_systems = len(supported_products)
     
#      new_row = {'Application_Area': apparea1, 'Count':no_of_systems}
   
#      df3 = df3.append(new_row, ignore_index=True)
     
#   print(df3)
#   df3.sort_values(by=['Count'], ascending=False,inplace = True)
#   df3['sumsystems'] = df3['Count'].sum()
#   df3['%'] =(df3['Count'] * 100)/df3['sumsystems']
#   df3['%'] = df3['%'].map('{:,.1f}'.format)    
#   df3['%'] = df3['%'].astype(float)
#   df3['Count'] = df3['Count'].astype(int)
#   df3.loc['Total', 'Count']= df3['Count'].sum()
#   df3.loc['Total', '%']= df3['%'].sum()
#   df3 = df3.fillna("")
  
#   dictssingleapp = df3.to_dict(orient='records')
#   print(dictssingleapp)
#   return dictssingleapp


@anvil.server.callable
def versions():  
    all_records = app_tables.suppported_products.search(InUseStatus='Live')
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'CFApplicationArea': r['CFApplicationArea'], 'Name': r['Name'], 'Account': r['Account'], 'InUse':r['InUseStatus'], 'Region':r['Location_c'], 'Version' : r['Live_version_no']}
            for r in all_records]
    
    df = pd.DataFrame.from_dict(dicts)
#     print(df)
#     group_by_region = df.groupby('Region')['Name'].count()
#     group_by_region = group_by_region.sort_values(['Region'], ascending=False)['Name']
#     print(group_by_region) 
    print(df)

    df = df.groupby('Version')['Name'].count() \
                             .reset_index(name='count') \
                             .sort_values(['Version'], ascending=False)
    print(df['Version'])
    print(df['count'])
    df['sumsystems'] = df['count'].sum()
    df['%'] =(df['count'] * 100)/df['sumsystems']
    df['%'] = df['%'].map('{:,.2f}'.format)    
    df['%'] = df['%'].astype(float)
    df['count'] = df['count'].astype(int)
    df.loc['Total', 'count']= df['count'].sum()
    df.loc['Total', '%']= df['%'].sum()
    df = df.fillna("")
    
    dict_versions = df.to_dict(orient='records')
    
    version_count = df['Version'].count()
    
    return dict_versions, version_count
  
  
@anvil.server.callable
def versions_summary():  
    all_records = app_tables.suppported_products.search(InUseStatus='Live')
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'CFApplicationArea': r['CFApplicationArea'], 'Name': r['Name'], 'Account': r['Account'], 'InUse':r['InUseStatus'], 'Region':r['Location_c'], 'Version' : r['Live_version_no'],\
             'Version_Level': r['Version_Level']}
            for r in all_records]
    
    df = pd.DataFrame.from_dict(dicts)
    print(df)

    pivot = pd.pivot_table(data = df, 
                           index = 'Region',
                           aggfunc={'Region' : 'count', },
                           columns= 'Version_Level',
                         #  margins = True)
                          )
    print('Pivot',pivot)
#     print(df)
#     group_by_region = df.groupby('Region')['Name'].count()
#     group_by_region = group_by_region.sort_values(['Region'], ascending=False)['Name']
#     print(group_by_region) 
    
    df = df.groupby('Version_Level')['Name'].count() \
                             .reset_index(name='count') \
                             .sort_values(['Version_Level'], ascending=False)
    print(df['Version_Level'])
    print(df['count'])
    df['sumsystems'] = df['count'].sum()
    df['%'] =(df['count'] * 100)/df['sumsystems']
    df['%'] = df['%'].map('{:,.0f}'.format)    
    df['%'] = df['%'].astype(float)

    df.loc['Total', 'count']= df['count'].sum()
    df.loc['Total', '%']= df['%'].sum()
    df = df.fillna("")
    
    dict_versions_summary = df.to_dict(orient='records')
    
   
    return dict_versions_summary
  
@anvil.server.callable
def customer_type__summary():  
    all_records = app_tables.suppported_products.search(InUseStatus='Live')
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'CFApplicationArea': r['CFApplicationArea'], 'Name': r['Name'], 'Account': r['Account'], 'InUse':r['InUseStatus'], 'Region':r['Location_c'], 'Version' : r['Live_version_no'],\
             'Version_Level': r['Version_Level'], 'Customer_Type': r['Customer_Type']}
            for r in all_records]
    
    df = pd.DataFrame.from_dict(dicts)
    print(df)

    pivot = pd.pivot_table(data = df, 
                           index = 'Region',
                           aggfunc={'Region' : 'count', },
                           columns= 'Version_Level',
                         #  margins = True)
                          )
    print('Pivot',pivot)
#     print(df)
#     group_by_region = df.groupby('Region')['Name'].count()
#     group_by_region = group_by_region.sort_values(['Region'], ascending=False)['Name']
#     print(group_by_region) 
    
    df = df.groupby('Customer_Type')['Name'].count() \
                             .reset_index(name='count') \
                             .sort_values(['Customer_Type'], ascending=False)
    print(df['Customer_Type'])
    print(df['count'])
    df['sumsystems'] = df['count'].sum()
    df['%'] =(df['count'] * 100)/df['sumsystems']
    df['%'] = df['%'].map('{:,.1f}'.format)    
    df['%'] = df['%'].astype(float)

    df.loc['Total', 'count']= df['count'].sum()
    df.loc['Total', '%']= df['%'].sum()
    df = df.fillna("")
    
    dict_customer_type_summary = df.to_dict(orient='records')
    
   
    return dict_customer_type_summary
  
#Interface Summary  
@anvil.server.callable
def group_in_single_interface():  
#   singleapps = [(str(row['application_area']), row) for row in app_tables.application_area.search(tables.order_by('application_area'))]
  singleainterface = app_tables.interface_types.search()
  df3 = pd.DataFrame() 
  for r  in singleainterface:
#      print((r['application_area']))
     Interface1 = r['Interface_Type']
     Interface2 = ('%' + Interface1  + '%')
 
     supported_products = app_tables.suppported_products.search(Interfaces = q.like (Interface2),InUseStatus='Live')
     no_of_systems = len(supported_products)
     
     new_row = {'Interface_Type': Interface1, 'Count':no_of_systems}
   
     df3 = df3.append(new_row, ignore_index=True)
     
  print(df3)
  df3.sort_values(by=['Count'], ascending=False,inplace = True)
  df3['sumsystems'] = df3['Count'].sum()
  df3['%'] =(df3['Count'] * 100)/df3['sumsystems']
  df3['%'] = df3['%'].map('{:,.2f}'.format)    
  df3['%'] = df3['%'].astype(float)
  df3['Count'] = df3['Count'].astype(int)
  df3.loc['Total', 'Count']= df3['Count'].sum()
  df3.loc['Total', '%']= df3['%'].sum()
  df3 = df3.fillna("")
  
  dictinterfaces = df3.to_dict(orient='records')
 
  return dictinterfaces 


#Database Summary  
@anvil.server.callable
def database_summary():
# Get an iterable object with all the rows in my_table
    all_records = app_tables.suppported_products.search(InUseStatus='Live')
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'Database_Version': r['Database_Version'], 'Account': r['Account']}
            for r in all_records]
    
    df = pd.DataFrame.from_dict(dicts)
#     print(df)
#     group_by_region = df.groupby('Region')['Name'].count()
#     group_by_region = group_by_region.sort_values(['Region'], ascending=False)['Name']
#     print(group_by_region) 


    df = df.groupby('Database_Version')['Account'].count() \
                             .reset_index(name='count') \
                             .sort_values(['count'], ascending=False)
    df['sumsystems'] = df['count'].sum()
    df['%'] =(df['count'] * 100)/df['sumsystems']
#     df['%'] = df['%'].map('{:,.1f}'.format)    
#     df['%'] = (df['%'].astype(float)) 
#     df['%'] = df['%'].round(2)
    df['%'] = np.round(df['%'], decimals = 2)
    df.loc['Total', 'count']= df['count'].sum()
    df.loc['Total', '%']= df['%'].sum()
    df = df.fillna("")
    print(df)
    dictsdatabases = df.to_dict(orient='records')
    print(dictsdatabases)
    return dictsdatabases
  
#OS Summary  
@anvil.server.callable
def OS_summary():
# Get an iterable object with all the rows in my_table
    all_records = app_tables.suppported_products.search(InUseStatus='Live')
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'Operating_System': r['Operating_System'], 'Account': r['Account']}
            for r in all_records]
    
    df = pd.DataFrame.from_dict(dicts)
#     print(df)
#     group_by_region = df.groupby('Region')['Name'].count()
#     group_by_region = group_by_region.sort_values(['Region'], ascending=False)['Name']
#     print(group_by_region) 


    df = df.groupby('Operating_System')['Account'].count() \
                             .reset_index(name='count') \
                             .sort_values(['count'], ascending=False)
    df['sumsystems'] = df['count'].sum()
    df['%'] =(df['count'] * 100)/df['sumsystems']
#     df['%'] = df['%'].map('{:,.1f}'.format)    
#     df['%'] = (df['%'].astype(float)) 
#     df['%'] = df['%'].round(2)
    df['%'] = np.round(df['%'], decimals = 2)
    df.loc['Total', 'count']= df['count'].sum()
    df.loc['Total', '%']= df['%'].sum()
    df = df.fillna("")
    print(df)
    dictsOS = df.to_dict(orient='records')
    print(dictsOS)
    return dictsOS
  
  
  #Access  Summary  
@anvil.server.callable
def Access_summary():
# Get an iterable object with all the rows in my_table
    all_records = app_tables.suppported_products.search(InUseStatus='Live')
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'Remote_Access_Available': r['Remote_Access_Available'], 'Account': r['Account']}
            for r in all_records]
    
    df = pd.DataFrame.from_dict(dicts)
#     print(df)
#     group_by_region = df.groupby('Region')['Name'].count()
#     group_by_region = group_by_region.sort_values(['Region'], ascending=False)['Name']
#     print(group_by_region) 


    df = df.groupby('Remote_Access_Available')['Account'].count() \
                             .reset_index(name='count') \
                             .sort_values(['count'], ascending=False)
    df['sumsystems'] = df['count'].sum()
    df['%'] =(df['count'] * 100)/df['sumsystems']
#     df['%'] = df['%'].map('{:,.1f}'.format)    
#     df['%'] = (df['%'].astype(float)) 
#     df['%'] = df['%'].round(2)
    df['%'] = np.round(df['%'], decimals = 2)
    df.loc['Total', 'count']= df['count'].sum()
    df.loc['Total', '%']= df['%'].sum()
    df = df.fillna("")
    print(df)
    dictsAccess = df.to_dict(orient='records')
    print(dictsAccess)
    return dictsAccess
