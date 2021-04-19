import mysql.connector


db = mysql.connector.connect(host="nicole.subnet04171433.vcn04171433.oraclevcn.com",user='nicole',password='',port=3306,database="data" )



cursorObject = db.cursor()


# sqlQuery            = "CREATE DATABASE data;"   

sqlQuery = "DROP TABLE mortalityPerCountry;"

cursorObject.execute(sqlQuery)

sqlQuery= "CREATE TABLE  mortalityPerCountry( location varchar(255),year int(11), indicator varchar(255) ,sex varchar(255),tooltip varchar(255),value1  decimal(10,1),value2 int(11));"

# Execute the sqlQuery

cursorObject.execute(sqlQuery)
 
# sqlQuery="show table"

# cursorObject.execute(sqlQuery)

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
