import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="voice_helper"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM cities")0

data = cursor.fetchall()

for info in data:
	print(info)

connection.close()