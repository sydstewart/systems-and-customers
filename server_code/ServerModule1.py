import anvil.users
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.secrets
import anvil.server
import pymysql
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, time , date , timedelta





def connect():
  connection = pymysql.connect(host='51.141.236.29',
                               port=3306,
                               user='CRMReadOnly',
                               password=anvil.secrets.get_secret('crm pass'),
                               database = 'infoathand',
                               cursorclass=pymysql.cursors.DictCursor)
  if not connection:
     alert(' Connection down')
  return connection
# Select t0.name, t0.id, account.name account, t0.account_id,
#   `account._cstm`.Dawn_Country `account.Dawn_Country`, _cstm.CFApplicationArea
#   CFApplicationArea, _cstm.InUseStatus InUseStatus,
#   account.shipping_address_country `account.shipping_address_country`,
#   `account._cstm`.location_c `account.location_c`, _cstm.Interface_Inbound_INR
#   Interface_Inbound_INR, _cstm.Interface_Bidirectional_SystmOne
#   Interface_Bidirectional_SystmOne, _cstm.Interface_Inbound_ADT
#   Interface_Inbound_ADT, _cstm.Interface_Inbound_Demographics
#   Interface_Inbound_Demographics, _cstm.Interface_Inbound_Medications
#   Interface_Inbound_Medications, _cstm.Outbound_Billing_Interface
#   Outbound_Billing_Interface, _cstm.Interface_Outbound_Dosing
#   Interface_Outbound_Dosing, _cstm.Interface_Outbound_PDF
#   Interface_Outbound_PDF, _cstm.Interface_Outbound_Query
#   Interface_Outbound_Query, _cstm.Interface_Inbound_TestResults
#   Interface_Inbound_TestResults, `account._cstm`.latitude_c,
#   `account._cstm`.longtitude_c, _cstm.Installed_Version_Num
# From assets t0 Left Join
#   accounts account On account.id = t0.account_id And account.deleted = 0
#   Left Join
#   accounts_cstm `account._cstm` On `account._cstm`.id_c = account.id Left Join
#   assets_cstm _cstm On _cstm.id_c = t0.id
# Where _cstm.Supported_Product_Type = 'System Installation' And t0.deleted = 0
# Order By account.name

@anvil.server.callable
def listsystems():
  conn = connect()
  with conn.cursor() as cur:
   cur.execute(
    "Select t0.name , t0.id, account.name account, t0.account_id, `account._cstm`.Dawn_Country `account.Dawn_Country`, _cstm.CFApplicationArea ,\
      CFApplicationArea, _cstm.InUseStatus InUseStatus,\
      account.shipping_address_country `account.shipping_address_country`, \
      `account._cstm`.location_c `account.location_c`, \
      _cstm.Interface_Inbound_INR  Interface_Inbound_INR,\
      _cstm.Interface_Bidirectional_SystmOne  Interface_Bidirectional_SystmOne, \
      _cstm.Interface_Inbound_ADT  Interface_Inbound_ADT,\
      _cstm.Interface_Inbound_Demographics Interface_Inbound_Demographics,\
      _cstm.Interface_Inbound_Medications  Interface_Inbound_Medications, \
      _cstm.Outbound_Billing_Interface Outbound_Billing_Interface, \
      _cstm.Interface_Outbound_Dosing Interface_Outbound_Dosing,\
      _cstm.Interface_Outbound_PDF Interface_Outbound_PDF, \
      _cstm.Interface_Outbound_Query Interface_Outbound_Query, \
      _cstm.Interface_Inbound_TestResults  Interface_Inbound_TestResults,\
      `_cstm`.`Interface_Birectional_Telehealth` `Interface_Birectional_Telehealth`,\
      `account._cstm`.latitude_c as latitude, \
      `account._cstm`.longtitude_c as longitude, \
      _cstm.Installed_Version_Num  as Live_Version_no,\
       `account._cstm`.customertype_c, \
       _cstm.Operating_System As Operating_System , \
       _cstm.Database_Version As  Database_Version, \
       _cstm.Remote_Access_Available As Remote_Access_Available, \
       _cstm.TextSMS_Setup_Done \
     From assets t0 Left Join \
      accounts account On account.id = t0.account_id And account.deleted = 0 \
      Left Join \
      accounts_cstm `account._cstm` On `account._cstm`.id_c = account.id Left Join \
      assets_cstm _cstm On _cstm.id_c = t0.id \
    Where _cstm.Supported_Product_Type = 'System Installation' And t0.deleted = 0 \
    Order By account.name ASC"
   ) 
 
#
# Delete all rows in the table
  app_tables.suppported_products.delete_all_rows()
  for r in cur.fetchall(): 
      dicts = [{'Account': r['account'],'Name': r['name'],'InUseStatus':r['InUseStatus'], 'Shipping_Address_Country':r['account.shipping_address_country'],
      'CFApplicationArea':r['CFApplicationArea'], '4S_Country':r['account.Dawn_Country'], 'Location_c' : r['account.location_c'], 'latitude' : r['latitude'],
       'longitude' :r['longitude'], 'Account_id' : r['account_id'], 'System_id' : r['id'] , 'Live_version_no': r['Live_Version_no'], 'Customer_Type' : r['customertype_c'] ,
               'Inbound_INR' : r['Interface_Inbound_INR'], 'Bidirectional_SystmOne' : r['Interface_Bidirectional_SystmOne'],
               'Inbound_ADT' : r['Interface_Inbound_ADT'], 'Inbound_Demographics' : r['Interface_Inbound_Demographics'], 
               'Inbound_Medications' : r['Interface_Inbound_Medications'], 'Outbound_Billing': r['Outbound_Billing_Interface'],
               'Outbound_Dosing' : r['Interface_Outbound_Dosing'], 'Outbound_PDF' : r['Interface_Outbound_PDF'],
               'Outbound_Query' : r['Interface_Outbound_Query'], 'Inbound_TestResults' : r['Interface_Inbound_TestResults'],
               'Bidirectional_Telehealth' :r['Interface_Birectional_Telehealth'],  'Operating_System' : r['Operating_System'],
                'Database_Version': r['Database_Version'], 'Remote_Access_Available'  : r['Remote_Access_Available'], 'TextSMS_Setup_Done': r['TextSMS_Setup_Done']}]
      for d in dicts:

            fullstring = d['Live_version_no']
            substring = "CF 8"

            if substring in fullstring:
                  Version_Level = '8'
            else:
                  Version_Level= '7'

           
#             #Database Version blan
#             if d['Database_Version']=='':
#                 DB_Version  = 'Not Recorded'
#                 print(DB_Version)
#             else:
#                 DB_Version = d['Database_Version']
#                 print(DB_Version)

# ------------------------------------------------------------------------------
# Interfaces consolidate for datagrid display           
            Interfaces= ''
            count = 0        # to identify first interface in list
            inters = ["Inbound_INR", "Inbound_ADT","Bidirectional_SystmOne","Inbound_Demographics","Inbound_Medications",\
                     "Outbound_Billing","Outbound_Dosing","Outbound_PDF","Outbound_Query", \
                      "Inbound_TestResults","Bidirectional_Telehealth" ]
               

            for i in inters:
                if d[i] == 'yes' and count ==1: # second and subsequent lines
                    Interfaces = Interfaces + '\n' + i
                elif count == 0 and d[i] == 'yes': # first line
                    Interfaces = i
                    count =1

#---------------------------------------------------------------------------------------
# App Area consolidate for datagrid display          
            
            appcount = 0
            appareas= ''
            appfullstring  = d['CFApplicationArea']          
            apps = ["Anticoagulation","Rheumatology","Dermatology",	"AF Rate Control (97)", \
                    "Growth Factors", "Multiple Sclerosis",	"Gastroenterology","DVT Assessment", \
                    "Clinical Haematology",	"Ophthalmology","Respiratory","Heart Failure"]
            for r in apps:      
                appsubstring  = r
                if appsubstring in appfullstring and appcount == 1:
                      appareas = appareas + '\n' +  r
                elif appcount ==0 and appsubstring in appfullstring:
                      appareas = r
                      appcount = 1
                
            app_tables.suppported_products.add_row(Version_Level = Version_Level,Interfaces = Interfaces,appareas =appareas,  **d)

  return 




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
  total_rows = len(dicts)
  return dictsapps, total_rows

# @anvil.server.callable
# def four_way_search(V, X, Y, Z):
# #     V = selectedapp
# #     X = selectedregion
# #     Y = selectedversion
# #     Z = selectedcustomertype
#     if V and X and Y and X:
#        results = app_tables.suppported_products.search(CFApplicationArea = q.like(V ),Location_c = X,Version_Level= Y, Customer_Type = Z, InUseStatus= 'Live')
        
#     else:
#        results = app_tables.suppported_products.search()
#     return results