import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import pandas as pd
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


@anvil.server.callable
def groupareas():
# Get an iterable object with all the rows in my_table
    all_records = app_tables.suppported_products.search()
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