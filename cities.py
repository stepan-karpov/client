import mysql.connector

def get_cities():
	cities = []
	connection = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="password",
	  database="voice_helper"
	)

	cursor = connection.cursor()

	cursor.execute("SELECT * FROM worldcities")

	data = cursor.fetchall()
	for info in data:
		cities.append(info[1])

#	print(cities)
	connection.close()
	return cities

if __name__ == "__main__":
	for c in get_cities():
		print(c)
	#get_cities_with_coord()
#print(get_cities_with_coord())
