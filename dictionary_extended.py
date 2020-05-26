"""
    to_change_keys = [
	["weather_forecast", 'temperature', 'wind', 'pressure', 'sunrise', 'sunset', 'status'],	["whatdaytoday", "whatdayweek", "whatdom"],
	["weather_forecast"], ['whatdayweek'], ["whatdayweek"], ["answer"], ["fs"], ["fs"], ["wdyh"], ["wdyh"], ["ago", "happy", "welcome"], ["ago"], ["ago"], ["hmr"],
	["hmr"], ["hmr"], ["happy"], ["welcome"], ["tell"], ["thanks"], ["abc"]
	]
    to_change_items = [
	get_cities(), ["today", "tomorrow", "day after tomorrow", "day after today", "yesterday"], get_months(),
	['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], get_dates(),
	['album', 'an album', 'song', 'a song'], ["season", "time of year", "year time"], [" is", "'s"], ["tell", "told"],
	["hear", "heard"], ['', "i ", "i am "],
	["n't", " not"], ["hear", "heard", "see", "seen"], ["answer", "answers", "request", "requests"],
	["prepared", "processed", "were in process", "protest"], ["much", "many"], ["hear", "to_hear"], ["your work", "work"], ["tell", "say"],
	["girl", "woman", "voice helper", "helper", name], ["Stepa", "Matvei"]
	]
    to_change_key_words = [
	"CITY", "NEAREST_DAYS", "MONTH", "DAY_OF_WEEK", "DATES", "ALBUM_SONG", "SEASON", "IS", "TELL", "HEAR", "I", "NOT", "HEAR_SEE", "ANSW_REQ",
	"PREPARED", "MUCH_MANY", "HEAR_TO_HEAR", "YOUR_WORK", "SAY_TELL", "WHO", "AUTHORS"
	]
"""

to_change_keys = [ 
	["who"]
]

to_change_items = [
	["stepa", "matvei"]
]

to_change_key_words = [
	"AUTHORS"
]

cmds = {
	"who": ('do you know AUTHORS', 'who do you know')
} 


# ! answers won't be imported
# just write here and copy them to dictionary.py
# this happends becose there's no import of answers, only question
answers = {
	"who": ('of course i know')
}

def get_cmds():
	return cmds, to_change_keys, to_change_items, to_change_key_words