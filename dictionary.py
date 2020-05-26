import mysql.connector
from music import *
from dictionary_extended import get_cmds
import datetime
from cities import get_cities

MONTH = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july",
     8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

name ="Isinka"

def day(delta):
    today = str(datetime.datetime.today() + datetime.timedelta(days=delta))
    return str(int(today[8:10])) + " of " + MONTH[int(today[5:7])]

def get_dates():
    day = datetime.datetime(2020, 1, 1)
    days = []
    for i in range(1, 367):
        str_day = str(int(str(day)[8:10])) + " of " + MONTH[int(str(day)[5:7])]
        days.append(str_day)
        day = day + datetime.timedelta(days=1)
    return days


"""
Instruction how to add new item to dictionary:
1)Generate new key for you command (for example weather >> wthr)
    * be sure that there's no any requests with this key
2)Add this key to keylist "cmds" like this ==> "wthr": ("", ""),
3)Generate some questions can be asked to VoiceHelper and write it to tuple
    like this "wthr": ("Hey", "Hay"),
4)To add answer on your query go to keylist answ
5)Create the same key like this ==> "wthr": ("", ""),
6)Add some content to your answer list like this
    ==> "wthr": ("Answer1", "Answer2"),
7)That's all!

"""

"""
        "whatdaytoday": ('what day is it ' + day(0), 'which day is ' + day(0), 'which day is it ' + day(0), 'what day is ' + day(0),
                         'do you know what day is it ' + day(0), 'which day is now', 'what day is now', 'what day is it now'),

        "thousand": ("how MUCH_MANY millimeters in ONE_A meter", "how MUCH_MANY millimeters is in ONE_A meter", "how MUCH_MANY millemiters are in ONE_A meter"),
	"hundred": ("how MUCH_MANY centimeters in ONE_A meter", "how MUCH_MANY centimeters is in ONE_A meter", "how MUCH_MANY centimeters are in ONE_A meter",
		    "how MUCH_MANY millimeters in ONE_A decimeter", "how MUCH_MANY millimeters is in ONE_A decimeter", "how MUCH_MANY millimeters are in ONE_A decimeter"),
	"ten":("how MUCH_MANY decimeters in ONE_A meter", "how MUCH_MANY decimeters is in ONE_A meter", "how MUCH_MANY decimeters are in ONE_A meter",
	       "how MUCH_MANY centimeters in ONE_A decimeter", "how MUCH_MANY centimeters is in ONE_A decimeter", "how MUCH_MANY centimeters are in ONE_A decimeter",
	       "how MUCH_MANY millimeters in ONE_A centimeter", "how MUCH_MANY millimeters is in ONE_A centimeter", "how MUCH_MANY millimeters are in ONE_A centimeter",),
	"one": ("how MUCH_MANY millimeters in ONE_A millimeter", "how MUCH_MANY millimeters is in ONE_A millimeter", "how MUCH_MANY millimeters are in ONE_A millimeter",
		"how MUCH_MANY meters in ONE_A meter", "how MUCH_MANY meters is in ONE_A meter", "how MUCH_MANY meters are in ONE_A meter",
		"how MUCH_MANY decimeters in ONE_A decimeter", "how MUCH_MANY decimeters is in ONE_A decimeter", "how MUCH_MANY decimeters are in ONE_A decimeter",
		"how MUCH_MANY centimeters in ONE_A centimeter", "how MUCH_MANY centimeters is in ONE_A centimeter", "how MUCH_MANY centimeters are in ONE_A centimeter"),

"""





opts = {
    "names": ('ee', 'hey', 'bay', name),
    #writting this case be sure any song names don't contain ANY of this words
    #becase may be something like this
    #please please me ===> me
    "tbr": ("detect"),

    "change_request": {"turn on something": "turn on queen"},
    "cmds": {
        "time": ("what time", "when", "what time is it", "time", "give me time", "give time",
                 "share time", "share me time", "what is the time now", "what time is it now", "time", "what is time"),
	   #NEAREST_DAYS are [today, tomorrow, day after tomorrow, day after today]
	   "whatdaytoday": ('what day is it NEAREST_DAYS', 'what day is NEAREST_DAYS', 'what day is it now', 'what day is now',
			 'do you know what day is it NEAREST_DAYS', 'do you know what day is NEAREST_DAYS',
			 'do you know what day is it now', 'do you know what day is now'
			 'which day is it NEAREST_DAYS', 'which day is NEAREST_DAYS', 'which day is it now', 'which day is now',
			 'do you know which day is it NEAREST_DAYS', 'do you know which day is NEAREST_DAYS',
			'do you know which day is it now', 'do you know which day is now'),
        "whatdayweek": ('what day of a week NEAREST_DAYS', 'is it DAY_OF_WEEK NEAREST_DAYS', 'what day of week is it NEAREST_DAYS', 'NEAREST_DAYS is DAY_OF_WEEK',
			'what day of a week is NEAREST_DAYS', 'what day of week', 'what day of week is it now', 'which day of a week NEAREST_DAYS',
			'which day of week is it NEAREST_DAYS', 'which day of a week is NEAREST_DAYS', 'which day of week', 'which day of week is it now',
			'what day of week is DATES', 'what day is DATES','what day of week is DATES'),
        "fests": ('day of independence uf unitet states', 'day of united states'),
        "whatdom": ('what day of month is it NEAREST_DAYS', 'what day of month NEAREST_GAYS', 'what day month',
		    'what day of month is NEAREST_DAYS', 'what month day is NEAREST_DAYS', 'what month day is NEAREST_DAYS',
		    'what day month NEAREST_DAYS', 'NEAREST_DAYS'),
        "hi":  ('hi', 'hello', 'big hello', 'hey', 'great hello', 'hello from me',"good morning", "good afternoon", "good evening", "good night", 'hello world'),
        "sfd": ('what the hell','whats the damn', 'what the shit'),
        "wwyb":  ('how old are you', 'how many years you are', 'as far are you old', 'as far are you young',
                  'how many days you are', 'how many months you are', 'what is you age', 'how old are you now',
		  'how old are you today', 'how long do you exist', 'how long do you exists'),
        # don't forget to write goodbye function for name
        "bye": ('goodbye', 'bye bye', 'go away', 'go out', 'shut up', "bye", 'see you later', 'see you soon', 'good luck', "have a good trip", "good night"),
        "hmr": ('how MUCH_MANY ANSW_REQ have you PREPARED',  'how MUCH_MANY ANSW_REQ were PREPARED', 'how MUCH_MANY ANSW_REQ have been PREPARED',
		'how MUCH_MANY ANSW_REQ were been PREPARED', 'how MUCH_MANY ANSW_REQ you PREPARED', 'how MUCH_MANY ANSW_REQ you have PREPARED',
		'how MUCH_MANY ANSW_REQ were in process', 'how MUCH_MANY ANSW_REQ been in process', 'how MUCH_MANY ANSW_REQ were been in process',
		'how MUCH_MANY ANSW_REQ have been in process',
		'how MUCH_MANY ANSW_REQ did you give', 'how MUCH_MANY ANSW_REQ did you gave', 'how MUCH_MANY ANSW_REQ did you prepared',
		'how MUCH_MANY ANSW_REQ',),
        "ago": ('IhaveNOT HEAR_SEE you for a long time', 'IhaveNOT HEAR_SEE you for a long time', 'IdidNOT HEAR_SEE you for a long time',
		'IdidNOT HEAR_SEE you for a long time', 'IdoNOT HEAR_SEE you for a long time'),
        "wdyh": ('what did you HEAR', 'what have you HEAR', 'what have been HEAR', 'what you did HEAR',
		 'what do you HEAR', 'what you HEAR', 'which speech did you HEAR', 'what speech did you HEAR',
		 'which speech have you HEAR', 'which speech have been HEAR',
		 'which words did you HEAR', 'which words have been HEAR', 'what words did you HEAR', 'which words were been HEAR',
		 'what did i TELL', 'what have been TELL', 'what i TELL', 'what have i TELL', 'what TELL',
		 'what did i TELL you', 'what have been TELL you', 'what i TELL you', 'what have i TELL you', 'what TELL you'),
        "servo": ('rotate servo on', 'servo on', 'turn servo'),
        #this tuple useful for two-phrases dialog with computer
        #it can be used like this:
        # - name, turn on please please me
        # - should it be an album or a song '?'
        # - an album
        "answer": ('ALBUM_SONG', 'its better to turn on ALBUM_SONG', 'i think ALBUM_SONG', 'i would like ALBUM_SONG',
		   'i think it is better to turn on ALBUM_SONG'),
        "fs": ("whatIS your favorite SEASON", "what SEASON do you like the most", "whatIS your most favorite SEASON",
	       "whatIS your the most favorite SEASON", "what SEASON do you prefer", "what SEASON do you like more",
	       "what SEASON do you like most", "what SEASON do you like best"),
        "fr": ("have you got any friends", "are you having any friends", "friends have", "friends", "any friends",
	       "do you have any friends", "have any friend", 'have any friends', 'you have any friends'),
        "happy": ('Ihappy to HEAR_TO_HEAR you', 'Ivery happy HEAR_TO_HEAR you','Iglad HEAR_TO_HEAR you'),
        "welcome": ('thanks for YOUR_WORK', 'thanks for YOUR_WORK you are doing', 'thank you very much',
                    'Isatisfied for YOUR_WORK', 'Iglad with YOUR_WORK', 'thanks a lot',
		    'thanks a lot for YOUR_WORK', 'Isatisfied with YOUR_WORK'),
        "tell": ("SAY_TELL something", "SAY_TELL me something", "SAY_TELL me something big",
		 "SAY_TELL me something long", "SAY_TELL me long sentence", "SAY_TELL me some big sentence",
		 "SAY_TELL me big sentence", "i want to hear long sentence", "i want to hear something long"),
        "thanks": ('i made you better', 'you are better than some time ago', 'you are improved now', 'great',
                    'well done', 'that is great', 'you are smart', 'you are better now', 'you are impoved', 'you are a good WHO',
		    'you are good WHO', 'you are good', 'you are a good WHO', 'you are good WHO',
		    'you are the best WHO', 'you are best WHO', 'you are greatest WHO', 'you are the greates WHO'
 		    'you are the best',
		    'you are best', 'you are the greatest'),
        "name":  ('what is your name', 'your name is', 'your name is what', 'tell me what is your name',
		  'how can i call you', 'how can i contact you', 'how should i call you',
		  'how should i contact you'),
        "howry":  ('how are you', 'how do you do', 'how do you feel'),
        "wcyd":  ('what can you do', 'what do you can', 'what are your possibilities'),
        "sorry": ('are you going to work', 'are you going to work today', 'silly machine', 'work', 'work please'),
        "wmy":  ('who made you', 'who create you', 'who is your creator', 'who was your creator',
                 'who worked under you'),
        "ayw": ('are you working', 'are you working now', 'are you hear me', 'working', 'are you ready to work'),
        "dyw": ('do you work', 'do you work at all', 'do you working', 'do you hear me', 'hear me', 'do you ready to work'),
        "cyw": ('can you hear me', 'can you hear me now', 'can hear me'),
        "music": ['turn on SONG', 'switch on SONG', 'turn on the SONG', 'switch on the SONG',
                  'turn on an ALBUM', 'turn on ALBUM', 'switch on ALBUM', 'switch on the ALBUM',
                  'turn on an ARTIST', 'turn on ARTIST', 'switch on ARTIST', 'switch on the ARTIST',
                  'SONG', 'ALBUM', 'ARTIST', 'turn on something'],

        "weather_forecast": ('tell me weather forecast in CITY', 'weather forecast in CITY', 'weather forecast in CITY on 15 of MONTH',
			     'weather forecast on 15 of MONTH', 'weather forecast in CITY on today',
			     'weather forecast in CITY on day after tomorrow', 'weather forecast on today', 'weather forecast on tomorrow'
			     'weather forecast on day after tommorow', 'what is the weather in CITY', 'weather in CITY',
			     "what is the weather in CITY", "CITY weather", "current weather in CITY", 'weather forecast',
			     'weather forecast on the street', 'weather forecat outside', 'what is the weather outside',
			     'the weather on the street','weather outside', 'weather'),

       "temperature": ('what temperature in CITY', 'which temperature in CITY now', 'what temperature in CITY is now', 'which temperature in CITY is now',
		       'what temperature in CITY '+ day(0), 'temperature in CITY', 'temperature on the street'),
       "wind": ('wind speed on the street', 'wind speed in CITY', 'wind speed', 'wind'),
       "pressure": ('pressure on the street', 'pressure in CITY', 'pressure'),
       "sunrise": ('when is sunrise in CITY', 'when is sunrise on the street', 'sunrise'),
       "sunset": ('when is sunset in CITY', 'when is sunset on the street', 'sunset'),
       "status": ('weather status in CITY', 'weather status on the street', 'weather status'),
       "abc": ("abc1", "abc2", "AUTHORS"),


    },
    "answ": {
        "fs": ("summer", "I think summer"),
        "hmk": ("one thousand", "thousand"),
        "hmik": ("one million", "million"),
        "hmc": ("there are actually ten", "ten"),
        "hmm": ("one thousand", "thousand"),
        "hck": ("one hundred thousand","hundred thousand"),
        "hcm": ("one hundred", "hundred"),
        "fr": ("yes i have", "yes", "of corse"),
        "ayw": ('yes, i am', 'i am', 'of course i am', 'yes'),
        "dyw": ('yes i do', 'of course i do', 'yes', 'i do'),
        "cyw": ('yes i can', 'yes', 'of course i can', 'i can'),
        "happy": ('i am happy too', 'i am happy about it'),
        "welcome": ('You are welcome', 'i am happy you are pleasured'),
        "tell": ('What should  I tell', 'i can answer any of question', 'hello world'),
        "thanks": ('thanks', 'thank you', 'thank you very much'),
        "name":  ('my name is ' + name, 'you should know me as ' + name, name),
        "sfd": ('It is just reality', 'It is true'),
        "howry":  ('i am fine', 'i am fine, thanks'),
        "wcyd":  ('i can not do a lot of things', 'my possibilities are not very big'),
        "sorry": ('sorry am trying to work', 'slow work may be caused by julius', 'sorry'),
        "wmy": ('my creator is stepa k', 'stepa k made me', 'stepa k'),
        "abc": ('answr for abc', 'answer for abc'),

    },
}

def get_dictionary():
    change_main_dictionary()
   # print(opts)

#    for cmd, items in opts["cmds"].items():
 #       print(cmd)
  #      print(items)
#    print(opts['cmds']['music'])
    return opts

def get_months():
    months = []
    for k, v in MONTH.items():
        months.append(v)
#    print(months)
    return months

def binary_search(L, target):
    start = 0
    end = len(L) - 1
    while start <= end:
        middle = (start + end)// 2
        midpoint = L[middle]
#        print(midpoint)
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle
    return -1


def export_dictionary():
    start_time = datetime.datetime.now()
    opts = get_dictionary()

    connection = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="password",
          database="voice_helper"
        )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM voice_helper.opts WHERE True;")
    connection.commit()
    print("Conn")
    variants = []
    for key, cmd in opts["cmds"].items():
        q = "INSERT INTO voice_helper.opts (dict, request) VALUES (\"" + key + "\", \""
        for r in cmd:
            q += r + ":"
            variants.append(r)
        q = q[:-1] + "\");"
        cursor.execute(q)
        connection.commit()
#        print(key + " added")
#    print(q)
    cursor.execute("DELETE FROM voice_helper.variants WHERE True;")
    connection.commit()

#    variants.sort()

    q = "INSERT INTO voice_helper.variants (variants) VALUES (\""
    for k in variants:
        q += k + ":"
    q = q[:-1] + "\");"
    cursor.execute(q)
    connection.commit()
    variants.sort()
    q = "INSERT INTO voice_helper.variants (variants) VALUES (\""

    for k in variants:
        q += k + ":"
    q = q[:-1] + "\");"
    cursor.execute(q)
    connection.commit()


    #print(binary_search(variants, "hello world"))
    #print(variants)

    print("[ log ] export time: " + str(datetime.datetime.now() - start_time))


def import_dictionary():
    cmds = {}
    start_time = datetime.datetime.now()
    connection = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="password",
          database="voice_helper"
        )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM opts")
    data = cursor.fetchall()
    #var = data[0][1].split(", ")
#    print(var)
    for row in data:
        cmds[row[0]] = tuple(row[1].split(":"))
    opts["cmds"] = cmds
#    print(cmds)
    print("[ log ] connection time: " + str(datetime.datetime.now() - start_time))
    return opts

def import_variants():
    start_time = datetime.datetime.now()
    connection = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="password",
          database="voice_helper"
        )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM variants")
    data = cursor.fetchall()
    #var = data[0][1].split(", ")
#    print(var)
    print("[ log ] connection time: " + str(datetime.datetime.now() - start_time))
    return tuple(data[0][0].split(":")), tuple(data[1][0].split(":"))

def change_items(to_change, items, key_word):
    """
    print("to change: " + str(to_change))
    print("items: " + str(items))
    print("key_word: " + str(key_word))
    print("==========")
    """
    for part in to_change:
        to_change = opts["cmds"][part]
        changed = []
        for req in to_change:
            if req.find(key_word) != -1:
                for item in items:
                     changed.append(req.replace(key_word, item.lower()))
#                     print(req.replace(key_word, item.lower()))
            else:
                changed.append(req)
#        for el in changed:
#            print(el)
    #   print(changed)
        opts["cmds"][part] = changed
#        for el in changed:
#            print(el)


def change_main_dictionary():
    a, b, c, d = get_cmds()
    for k, v in a.items():
        opts["cmds"][k] = v


    to_change = opts["cmds"]["music"]
    artists, albums, songs = get_lists()
    changed = []
    for req in to_change:
        if req.find("SONG") != -1:
            for song in songs:
                changed.append(req.replace("SONG", song))
        elif req.find("ALBUM") != -1:
            for album in albums:
                changed.append(req.replace("ALBUM", album))
        elif req.find("ARTIST") != -1:
            for artist in artists:
                changed.append(req.replace("ARTIST", artist))
        else:
            changed.append(req)

    opts["cmds"]["music"] = changed

    to_change_keys = [
	["weather_forecast", 'temperature', 'wind', 'pressure', 'sunrise', 'sunset', 'status'],	["whatdaytoday", "whatdayweek", "whatdom"],
	["weather_forecast"], ['whatdayweek'], ["whatdayweek"], ["answer"], ["fs"], ["fs"], ["wdyh"], ["wdyh"], ["ago", "happy", "welcome"], ["ago"], ["ago"], ["hmr"],
	["hmr"], ["hmr"], ["happy"], ["welcome"], ["tell"], ["thanks"]
	]
    to_change_items = [
	get_cities(), ["today", "tomorrow", "day after tomorrow", "day after today", "yesterday"], get_months(),
	['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], get_dates(),
	['album', 'an album', 'song', 'a song'], ["season", "time of year", "year time"], [" is", "'s"], ["tell", "told"],
	["hear", "heard"], ['', "i ", "i am "],
	["n't", " not"], ["hear", "heard", "see", "seen"], ["answer", "answers", "request", "requests"],
	["prepared", "processed", "were in process", "protest"], ["much", "many"], ["hear", "to_hear"], ["your work", "work"], ["tell", "say"],
	["girl", "woman", "voice helper", "helper", name]
	]
    to_change_key_words = [
	"CITY", "NEAREST_DAYS", "MONTH", "DAY_OF_WEEK", "DATES", "ALBUM_SONG", "SEASON", "IS", "TELL", "HEAR", "I", "NOT", "HEAR_SEE", "ANSW_REQ",
	"PREPARED", "MUCH_MANY", "HEAR_TO_HEAR", "YOUR_WORK", "SAY_TELL", "WHO"
	]

    for el in b:
        to_change_keys.append(el)
    for el in c:
        to_change_items.append(el)
    for el in d:
        to_change_key_words.append(d)



    for i in range(0, len(to_change_keys)):
        """
        print(to_change_keys[i])
        print(to_change_items[i])
        print(to_change_key_words[i])
        """
        change_items(to_change_keys[i], to_change_items[i], to_change_key_words[i])

#get_dictionary()
#print(get_dates())
#print(day(0))
#print(day(1))
#print(day(2))
#print(opts['cmds']['weather_forecast'])
#get_dictionary()
if __name__ == "__main__":
    export_dictionary()
#import_variants()
"""
var = import_variants()
req = "doens't matter what text is here :)"
while req != "stop":
    req = input("Enter request to find in variants: ")
    start_time = datetime.datetime.now()
    print(binary_search(var, req))
    print("[ log ] search_time: " + str(datetime.datetime.now() - start_time))

"""

#opts = import_dictionary()


"""
for k, v in opts["cmds"].items():
    print(k)
    print(v)
"""
