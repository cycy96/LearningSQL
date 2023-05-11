import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="11111",
    database="testdb"
)

mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

