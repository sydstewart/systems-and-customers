import anvil.secrets
import anvil.server
import pymysql
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
def connect():
  connection = pymysql.connect(host='51.141.236.29',
                               port=3306,
                               user='CRMReadOnly',
                               password=anvil.secrets.get_secret('crm pass'),
                               database = 'infoathand',
                               cursorclass=pymysql.cursors.DictCursor)
  return connection

@anvil.server.callable
def listsystems():
  conn = connect()
  with conn.cursor() as cur:
   cur.execute(
                "SELECT `t0`.`name`,   `t0`.`id`,   `account`.`name` `account`,   `t0`.`account_id`, `account._cstm`.`Dawn_Country` `account.Dawn_Country`, \
                `_cstm`.`CFApplicationArea` `CFApplicationArea`, \
                `_cstm`.`InUseStatus` `InUseStatus`, \
                `account`.`shipping_address_country` `account.shipping_address_country`, \
                `account._cstm`.`location_c` `account.location_c`, \
                `_cstm`.`Interface_Inbound_INR` `Interface_Inbound_INR`, \
                `_cstm`.`Interface_Bidirectional_SystmOne` `Interface_Bidirectional_SystmOne`, \
                `_cstm`.`Interface_Inbound_ADT` `Interface_Inbound_ADT`, \
                `_cstm`.`Interface_Inbound_Demographics` `Interface_Inbound_Demographics`, \
                `_cstm`.`Interface_Inbound_Medications` `Interface_Inbound_Medications`, \
                `_cstm`.`Outbound_Billing_Interface` `Outbound_Billing_Interface`, \
                `_cstm`.`Interface_Outbound_Dosing` `Interface_Outbound_Dosing`, \
                `_cstm`.`Interface_Outbound_PDF` `Interface_Outbound_PDF`, \
                `_cstm`.`Interface_Outbound_Query` `Interface_Outbound_Query`, \
                `_cstm`.`Interface_Inbound_TestResults` `Interface_Inbound_TestResults` \
              FROM \
                `assets` `t0` \
                LEFT JOIN `accounts` `account` ON `account`.`id` = `t0`.`account_id` \
                AND `account`.`deleted` = 0 \
                LEFT JOIN `accounts_cstm` `account._cstm` ON `account._cstm`.`id_c` = `account`.`id` \
                LEFT JOIN `assets_cstm` `_cstm` ON `_cstm`.`id_c` = `t0`.`id` \
              WHERE \
                `_cstm`.`Supported_Product_Type` = 'System Installation' \
                AND `t0`.`deleted` = 0 \
              ORDER BY \
                `account`.`name` ASC"\
              )
#     dicts = [{'Date_Entered': r['Date_Entered'],'Measure_Value': r['Measure_Value'],'NoteCol':r['noteCol']}
#             for r in waitinglist]                  
#     return cur.fetchall() 
  dicts = [{'Company': r['account'],'Name': r['name'],'InUseStatus':r['InUseStatus'], 'shipping_address_country':r['account.shipping_address_country'],
  'CFApplicationArea':r['CFApplicationArea']}
  for r in cur.fetchall()]
#     app_tables.projects.add_row(company = row['Company'], projectname= row['Name'],boardname= row['BoardName'], status = row['Status'], startdate = row['StartDate'], enddate = row['EndDate'])
  total_rows = len(dicts)
  for row in dicts:
  t= app  
  return dicts, total_rows




@anvil.server.callable
def applications():
  conn = connect()
  with conn.cursor() as cur:
   cur.execute( "SELECT  DISTINCT `_cstm`.`CFApplicationArea` `CFApplicationArea`  FROM \
                `assets` `t0` \
                LEFT JOIN `accounts` `account` ON `account`.`id` = `t0`.`account_id` \
                AND `account`.`deleted` = 0 \
                LEFT JOIN `accounts_cstm` `account._cstm` ON `account._cstm`.`id_c` = `account`.`id` \
                LEFT JOIN `assets_cstm` `_cstm` ON `_cstm`.`id_c` = `t0`.`id` \
              WHERE \
                `_cstm`.`Supported_Product_Type` = 'System Installation' \
                AND `t0`.`deleted` = 0 \
              ORDER BY \
                `CFApplicationArea` ASC"\
              
              )
#     dicts = [{'Date_Entered': r['Date_Entered'],'Measure_Value': r['Measure_Value'],'NoteCol':r['noteCol']}
#             for r in waitinglist]                  
#     return cur.fetchall() 
  dictsapps = [{'CFApplicationArea': r['CFApplicationArea']}
  for r in cur.fetchall()]
  print(dictsapps)
#     app_tables.projects.add_row(company = row['Company'], projectname= row['Name'],boardname= row['BoardName'], status = row['Status'], startdate = row['StartDate'], enddate = row['EndDate'])
#   total_rows = len(dicts)
  return dictsapps