import csv 
                 
import mysql.connector

import pandas as pd

db = mysql.connector.connect(host="nicole.subnet04171433.vcn04171433.oraclevcn.com",user='nicole',password='123456Aa.',port=3306,database="data" )


cursorObject = db.cursor()

# file = open('data1.csv')
# csv_data = csv.reader(file,delimiter = ';')
# csv_data = pd.read_csv('data.csv',encoding = "utf-8")

# sqlQuery            = "CREATE DATABASE data;"   
# for row in csv_data:
#     cursorObject.execute('INSERT INTO mortalityPerCountry(location,\year , \indicator,\sex,\tooltip,\value1 ,\value2)' \
#           'VALUES("%s", "%s", "%s","%s","%s","%s","%s")', 
#           row)

# csv_data.to_sql=(con=db, name='mortalityPerCountry',
#   if_exists='replace', flavor='mysql')



df = pd.read_csv("data2.csv",sep=';',quotechar='\'',encoding='utf8') # Replace Excel_file_name with your excel sheet name
df.to_sql('mortalityPerCountry',con=db,index=False,if_exists='replace') # Replace Table_name with your sql table name



#close the connection to the database.
db.commit()


# Execute the sqlQuery
sqlQuqery = "SELECT  * FROM mortalityPerCountry limit 5;"
cursorObject.execute(sqlQuery)
 

# #Fetch all the rows

rows                = cursorObject.fetchall()

 
count =0
for row in rows:
  if count<=5:
       print(row)
       count+=1
  else:
    break

cursorObject.close()
