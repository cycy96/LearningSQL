import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="11111"
)

mycursor = db.cursor()

#Create database
mycursor.execute("CREATE DATABASE mydatabase")

#Show database
mycursor.execute("SHOW DATABASES")

#Check if Database Exists
for x in mycursor:
  print(x)


