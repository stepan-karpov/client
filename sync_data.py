import mysql.connector

def sync_table(table_name):
	main_connection = mysql.connector.connect(
		host="192.168.0.35",
		user="rpi1",
		passwd="some_pass",
		database="voice_helper",
	)

	local_connection = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="voice_helper",
	)

	main_cursor = main_connection.cursor()
	local_cursor = local_connection.cursor()

	local_cursor.execute("DELETE FROM " + table_name + " WHERE True")

	main_cursor.execute("SELECT * FROM " + table_name)
	main_data = main_cursor.fetchall()
	if table_name == "worldcities":
		query = "INSERT INTO worldcities (city, city_ascii, lat, lng, country, iso2, iso3, admin_name, capital, population, id) VALUES "
	else:
		if table_name.startswith("0"):
			query = "INSERT INTO " + table_name + " (id, city, temp, wind, pressure, sunrise, sunset, status) VALUES "
		else:
			query = "INSERT INTO " + table_name + " (id, city, temp, wind, pressure, sunrise, sunset, status, icon) VALUES "

	for city in main_data:

		local_cursor.execute(query + str(city))
		local_connection.commit()
#		print(city)

	main_connection.close()
	local_connection.close()

def sync():
	tables = ["0_day_forecast", "1_day_forecast", "2_day_forecast", "3_day_forecast", '4_day_forecast',
		 "5_day_forecast", "6_day_forecast", "7_day_forecast", "worldcities"]
	for table in tables:
		sync_table(table)
sync()
