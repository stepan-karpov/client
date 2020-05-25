import datetime
import time
from cities import get_cities
from dictionary import get_dates, day
import random
import mysql.connector

MONTH = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july",
         8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}


def get_weather(table_name):
	start_time = datetime.datetime.now()
	connection = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="password",
	  database="voice_helper"
	)

	cursor = connection.cursor()

	cursor.execute("SELECT * FROM " + table_name)

	data = cursor.fetchall()
	print("[ log ] connection time: " + str(datetime.datetime.now() - start_time))
	return data

def find_city(Text):
	found_city = "None"
	# if you want to see weather in "Venice" watch for "Nice"
	cities = get_cities()
	cities.sort(key=len)
	cities.reverse()

	for city in cities:
		if Text.find(city.lower()) != -1:
			found_city = city.lower()
			break
	if found_city == "None":
		words = Text.split(" ")
		for i in range(len(words)):
			if words[i] == "in":
				return words[i + 1]
		return "moscow"
	else:
		return found_city

def days_of_week(day):
	days = {1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday", 7: "sunday"}
	today = str(time.ctime(time.time()))[:3].lower()
#	print(today)
	for k, v in days.items():
		if v[:3] == today:
			return day - k
	return 0


def find_date(Text):
	change_date = {"day after tomorrow": day(2), "day after today": day(1), "today": day(0), "tomorrow": day(1),
		       "monday": day(days_of_week(1)), "yesterday": day(-1), "tuesday": day(days_of_week(2)),
		       "wednesday": day(days_of_week(3)), "thursday": day(days_of_week(4)), "friday": day(days_of_week(5)),
		       "saturday": day(days_of_week(6)), "sunday": day(days_of_week(7))}
	for k, v in change_date.items():
		Text = Text.replace(k, v).strip()
	found_date = "None"

	dates = get_dates()
	dates.reverse()

	for date in dates:
		if Text.find(date) != -	1:
			return date
	if found_date == "None":
		return str(day(0))
	else:
		return found_date

def weather_forecast(Text):
	print(Text)
	# temp, wind, pressure, sunrise, sunset, status
	params = [False, False, False, False, False, False]
	keys = [" KEY: 000", " KEY: 001", " KEY: 010", " KEY: 011", " KEY: 100", " KEY: 101"]

	for i in range(len(params)):
		if Text.endswith(keys[i]):
			Text = Text.replace(keys[i], "").strip()
			params[i] = True


	print(params)
	print(Text)
	found_city = find_city(Text.lower())
	date = find_date(Text.lower())
	print("[ log ] City detected: " + found_city)
	print("[ log ] Date of forecast: " + date)
	year = int(str(datetime.datetime.today())[:4])
	day = int(date[:date.find(" ")])
#	print(year)
#	print(day)
	for k, v in MONTH.items():
		if date.find(v) != -1:
			date = datetime.datetime(year, int(k), day)
			break
	timedelta = str(date - datetime.datetime.today())
#	print(timedelta)
	try:
		forecast_day = int(timedelta[:timedelta.find(" ")]) + 1
	except ValueError:
		forecast_day = 1
#	print(forecast_day)

	if not -1 < forecast_day < 8:
		return "sorry i dont have forecast on this day"
	else:
		weather = []
		data = get_weather(str(forecast_day) + "_day_forecast")
		for city in data:
			if city[1].lower() == found_city.lower():
				weather = city
				break
		params_answers = [weather[2] + " degrees ", weather[3] + " meters per second ", str(int(round(float(weather[4]) / 10))) + " kilopascales ",
				" at " + weather[5] + " o clock ", " at " + weather[6] + " o clock ", weather[7]]

		if len(weather) == 0:
			return "sorry i have no information about city " + found_city
		else:
			if params.count(True) != 0:
				answer = ""
				for i in range(len(params)):
					if params[i]:
						answer += params_answers[i]
				answer = answer.replace("  ", " ").strip()
				return answer
			else:
				try:
					return weather[2] + " degrees " + weather[7].lower().strip(".") + " and " + weather[8]
				except:
					return weather[2] + " degrees and " + weather[7].lower().strip(".")
	return "forecast error"

#   0   1    2    3
#   6   7    8    9

if __name__ == "__main__":

	print(days_of_week(4))
	print("endline")
