import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import pandas
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
    
    df = pandas.DataFrame.from_dict(dicts)
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
  
    
    dictsregions = df.to_dict(orient='records')
    
    return dictsregions