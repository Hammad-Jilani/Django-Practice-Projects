import mysql.connector

database = mysql.connector.connect(
  host='localhost',
  user='root',
  password='Hammad@10'
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All done!")