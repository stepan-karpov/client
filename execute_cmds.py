import datetime
import mysql.connector
from words import *
from dictionary import get_dates, day
from weather import find_date
from naval_battle import *
from music import *
import wolframalpha
#from servo import rotate
from random import randint

answers = {
	"hi": ("Hi", "Hello", "Hey"),
	"hoy": ('i am very young', 'i am younger than my creator on fifteen years', 'i am surely younger than you'),
}

digits = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
	  7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth",
	  13: "thirteenth", 14: "fourteenth", 15: "fifteenth", 16: "sixteenth", 17: "seventeenth",
	  18: "eighteenth", 19: "nineteenth", 20: "twentieth", 21: "twenty first",
	  22: "twenty second", 23: "twenty third", 24: "twenty fourth", 25: "twenty fifth",
	  26: "twenty sixth", 27: "twenty seventh", 28: "twenty eighth", 29: "twenty ninth",
	  30: "thirtieth", 31: "thirty first"}

MONTH = {"01": "january", "02": "febrary", "03": "march", "04": "april", "05": "may", "06": "june", "07": "july",
         "08": "august", "09": "september", "10": "october", "11": "november", "12": "december"}
DAYS = {0: "monday", 1: "tuesday", 2: "wednesday", 3: "thursday", 4: "friday", 5: "saturday", 6: "sunday"}

def time(Text):
	now = datetime.datetime.now()
	return "now it is " + str(now.hour) + " : " + str(now.minute)

#def statement(Text):

def find_date_without_week_days(Text):
	change_date = {"day after tomorrow": day(2), "day after today": day(1), "today": day(0), "tomorrow": day(1), "yesterday": day(-1)}
	for k, v in change_date.items():
		Text = Text.replace(k, v).strip()
	found_date = "None"

	dates = get_dates()
	dates.reverse()

	for date in dates:
		if Text.find(date) != - 1:
			return date
	if found_date == "None":
		return str(day(0))
	else:
		return found_date

def stop_naval_battle(Text):
    write_file("stop", "cell.txt")
    write_file("stop", "status.txt")
    write_file("None", "beaten_cell.txt")
    return "ok. if you want to play just tell me"


def day_of_a_week(Text):
	date = find_date_without_week_days(Text)
	m = 0
	d = ""
	while d != "31 of december":
		m -= 1
		d = day(m)
#	print(m)
	for i in range(m + 1, m + 367):
		#print(day(i))
		if day(i) == date:
			break
	print("day in request: " + date)
	date = date.replace(date[:2], digits[int(int(date[:2]))])
	print("delta days: " + str(i))
	today = DAYS[(datetime.datetime.today().weekday() + i) % 7]
	print("day of week in request: " + today)
	day_in = False
	for k, v in DAYS.items():
		if Text.find(v) != -1:
			day_in = True
			break
	print(Text)
	if day_in:
		if Text.find("is it") != -1:
			for k, v in DAYS.items():
				if Text.find(v) != -1:
					if v == today:
						answ = ["yes, it is " + today, "yes, you are right"]

					else:
						answ = ["no, it is not " + v + ', it is ' + today]
					return answ[randint(0, len(answ) - 1)]
	#if day_of_week_in_req(Text) and nearest_day_in_req(Text):
	for k, v in DAYS.items():
		if Text.find("is " + v) != -1:
			if today == v:
				return "yes, " + date + " is " + v
			else:
				return "no, " + date + " is " + today

	answ = ['It is ' + today + ", for sure", today, "i think that it is " + today]
	return answ[randint(0, len(answ) - 1)]

def units(Text):
	print("[ log ] units function")
	try:
		f = ""
		s = ""
		f_unit_name = ""
		s_unit_name = ""
		units = ["meters", "grams", "bytes", "bits", "newtons", "tesla",
			 "meter", "gram", "byte", "bit", "newton"]
		for word in Text.split(" "):
			for unit in units:
				if word.endswith(unit):
					if f == "" and f_unit_name == "":
						f = word.replace(unit, "").strip()
						f_unit_name = word.replace(f, "").strip()
						print("rec " + word)
					else:
						s = word.replace(unit, "").strip()
						s_unit_name = word.replace(s, "").strip()
		print("[ log ] " + f + " " + f_unit_name)
		print("[ log ] " + s + " " + s_unit_name)

		prefixes = {"piko": .000000000001, "nano": .000000001, "micro": .00000001,
			    "milli": .001, "centi": .01, "deci": .1, "": 1, "kilo": 1000, "mega": 1000000,
		    	"giga": 1000000000, "tera": 1000000000000, "peta": 1000000000000000}
		digit = ""
		if f_unit_name == s_unit_name or f_unit_name.find(s_unit_name) != -1 or s_unit_name.find(f_unit_name) != -1:
			digit =  prefixes[s] / prefixes[f]
		elif f_unit_name.startswith("byt") and s_unit_name.startswith("bit"):
			digit =  (prefixes[s] / 8) / prefixes[f]
		elif f_unit_name.startswith("bit") and s_unit_name.startswith("byt"):
			digit =  (prefixes[s] * 8) / prefixes[f]
		else:
			return "i think that is it impossible to convert this units"
		if digit > .99:
			digit = str(int(digit))
		else:
			digit = str(digit)
		return "there are " + digit + " " + f + f_unit_name + " in one " + s + s_unit_name
	except:
		return "i think that is it impossible to convert this units"

def hello(Text):
	try:
		return answers["hi"][randint(0, len(answers) + 1)]
	except:
		now = datetime.datetime.now()
		if now.hour < 6:
			return "Good night"
		elif now.hour > 5 and now.hour < 11:
			return "Good morning"
		elif now.hour > 10 and now.hour < 18:
			return "Good day"
		elif now.hour > 17 and now.hour < 23:
			return "Good evening"
		elif now.hour > 22:
			return "Good night"
		return "Hi"

def words(Text):
    status = str(open("FILES/words.txt", mode='r').readlines()[0]).strip('\n')
    file = open('FILES/DialogStory.txt', mode="r").readlines()
    last_answer = file[len(file) - 3]
    last_answer = last_answer[8:-1]

    print("[ log ] status is: " + status)
    print("[ log ] last_answer is: " + str(last_answer))
    if status == "stop":
        if Text.find("--debug") != -1:
            open("FILES/words.txt", mode='w').write("debug")
            return "ok, i am ready to play. to leave game mode say stop. now i have " + str(len(get_vocabulary())) + " words to use. !DEBUG MODE"
        else:
            open("FILES/words.txt", mode='w').write("start")
            return "ok, i am ready to play. to leave game mode say stop. now i have " + str(len(get_vocabulary())) + " words to use"
    elif status == "debug":
        if Text.find("delete") != -1:
            last_request = what_heard("does't matter what text is here :)")
            return delete_word(last_answer)
        elif Text.find("insert") != -1 or last_answer.startswith("should i insert word"):
            if last_answer.startswith("should i insert word"):
                if Text.find("yes") != -1:
                    to_insert = last_answer[21:].replace('"', '').strip()
                    return insert_word(to_insert)
                else:
                    return "word won't be inserted. keep playing"
            else:
                Text = Text.replace("insert", "").replace("  ", " ").replace("  ", " ").replace("word", "").replace("  ", " ").strip()
                Text = Text.split(" ")[0]
                return 'should i insert word "' + Text + '"'
        elif Text.find("stop") != -1:
            open("FILES/words.txt", mode='w').write("stop")
            insert_used_word("abc", True)
            return "ok, i keep listening your requests"
        else:
            if len(Text.split(" ")) == 1:
                return find_word(Text, True)
            else:
                return "you should say only one word"
    elif status == "start":
        if Text.find("stop") != -1:
            open("FILES/words.txt", mode='w').write("stop")
            insert_used_word("abc", True)
            return "ok, i keep listening your requests"
        else:
            if len(Text.split(" ")) == 1:
                return find_word(Text)
            else:
                return "you should say only one word"
    else:
        return "words module error"

def how_old_are_you(Text, teleg=False):
	answ = ""
	if not teleg:
		makeday = datetime.datetime(2019, 6, 21)
	else:
		makeday = datetime.datetime(2020, 5, 29)
	today = datetime.datetime.today()
	days = str(today - makeday)

	try:
		if teleg:
			int("not int :)")
		answ = answers["hoy"][randint(0, len(answers) + 1)]
	except:
		years = int(days[0:days.find(" ")]) // 365
		months = (int(days[0:days.find(" ")]) // 30) - years*12
		if years == 0:
			answ = "I am " + str(months) + " months old"
		elif years == 1:
			if months == 1:
				answ = "I am 1 year 1 month old"
			else:
				answ = "I am 1 year " + str(months) + " months old"
		else:
			if months == 1:
				answ = "I am " + str(years) + " years 1 month old"
			else:
				answ = "I am " + str(years) + " years " + str(months) + " months old"


	if Text.find("day") != -1:
		days = int(days[0:days.find(" ")])
		answ = str(days) + " days old"
	if Text.find("month") != -1:
		days = int(days[0:days.find(" ")]) // 30
		i = days
		answ = str(i) + " months old"
	if Text.find("year") != -1:
		days = int(days[0:days.find(" ")]) // 365
		i = days
		if i == 1:
			answ = str(i) + " year old"
		else:
			answ = str(i) + " years old"
	if not teleg:
		return answ
	else:
		return answ[4:-4]

def bye(Text):
	print("[ log ] DON'T FORGET TO WRITE FUNCTION \"BYE\" FOR EXIT")
	return "goodbye"

def how_many_requests(Text):
		before_writting_this_function = 1677
		kolvo = int(len(open('FILES/DialogStory.txt', mode="r").readlines()) / 4) + before_writting_this_function
		return "i prepared " + str(kolvo) + " requests"


def start_naval_battle(Text):
    start_game() # starts naval battle
    write_file("start", "status.txt")
    write_file("start", "cell.txt")
    return "i am happy we are playing. i have already build my field. you starts. it is better to use words kill, in water and hit while playing. i am waiting for your variant"

    """
     connection = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="voice_helper"
    )
    cursor = connection.cursor()
    cursor.execute("INSERT INTO voice_helper.naval_battle (field) VALUES (101);")
    connection.commit()

    """

"""
def detect_cell_status(Text):
	cells = get_cells()
	cell = ()
	for word in Text.split(" "):
		if cells.count(word) != -1:
			try:
				cell = (cells_accord[word[:1]], int(word[2:]))
			except:
				return status, "sorry, i do not understand cell"
	if cell == ():
		return status, "what cell have you chosen"

	return cell, status
"""
def detect_status(Text):
	statuses = {
		"hit": ["hit", "touched"],
		"kill": ["kill"],
		"water": ["water", "clear"]
	}
	status = []
#	print(Text)
	for k, v in statuses.items():
		for u in v:
#			print(u)
#			print(Text.find(u))
			if Text.find(u) != -1:
				status.append(k)
	print("[ log ] statuses list: " + str(status))
	if len(status) == 0 and Text.find("no") != -1:
		return "water"
	if len(status) > 1:
		return "you should say only one cell status"
	elif len(status) == 0:
		return "please, repeat status"
	else:
		return status[0]

def detect_cell(Text):
	cell = (0, 0)
	cells = get_cells()
	cells_accord = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
	for word in Text.split(" "):
		if cells.count(word) != 0:
#			print("[ log] word to cell: " + str(word))
#			print("[ log] letter in word: " + str(word[:1]))
#			print("[ log ] int in word: " + str(word[1:]))
			cell = (cells_accord[word[:1]], int(word[1:]))
	return cell

# stealin'
# i gave you the key to my home
# i left you alone
# in charge of my heart, hey, stealin'

def write_file(item, file):
    file = open("FILES/naval_battle/" + file, mode="w")
    file.write(str(item))
    file.close()

def get_line(file):
    file = open("FILES/naval_battle/" + file, mode="r")
    return str(file.readlines()[0])

def get_naval_battle_request(start=False):
    cell = get_line("cell.txt")[1:-1]
    cell = cell.split(", ")
    print("[ log ] cell to say status: " + str(cell))
    status = get_line("status.txt")
    print("[ log ] status of my past cell: " + status)

    cells = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}

    if status != "hit" and status != "kill":
        try:
            get = get_shot((int(cell[0]), int(cell[1])))
        except ValueError:
            print("[ log ] first 'water' after series of hits of computer")
            if status == "hit" or status == "kill" or status == "water":
                write_file(status, "status.txt")
                write_file("None", "cell.txt")
            return "please, say correct cell"
    else:
        get = "in water" #very big crutch

    if status == "kill" or status == "hit":
        if count_killed() == 20:
            get = "i win"

    print("[ log ] get_shot return is: " + get)

    answ = ["in water", "it is water there", "clear there", "there is no any ships"]
    if answ.count(get) == 0:
        print("[ log ] looks like a hit or kill :)")
        if get.startswith("sorry"):
            print("[ log ] impossible to shot here")
            if start:
                print("[ log ] impossible to shot at the start")
                write_file("start", "cell.txt")
            else:
                write_file("None", "cell.txt")
            write_file(status, "status.txt")
            draw_fields()
            return get + ". please repeat cell"
        elif get.find("win") != -1:
            print("[ log ] someone win")
            write_file("stop", "cell.txt")
            write_file("stop", "status.txt")
            write_file("None", "beaten_cell.txt")
            draw_fields()
            return get + ". do you want to start new game"
        elif get.find("lie") != -1:
           print("[ log ] looks like 'you lie to me'")
           write_file("None", "cell.txt")
           draw_fields()
           return get
        else:
            if status != "hit or kill":
                print("[ log ] hit for the first time")
                if not start:
                    beaten_cell = get_line("beaten_cell.txt")[1:-1]
                    if beaten_cell == "None":
                        raise AlgorithmError
                    beaten_cell = beaten_cell.split(", ")
                    mark_shot(status, (int(beaten_cell[0]), int(beaten_cell[1])))
                write_file("hit or kill", "status.txt")
                write_file("None", "cell.txt")
                write_file("None", "beaten_cell.txt")
                draw_fields()
                return get
            else:
                print("[ log ] hit NOT for the first time")
                write_file("None", "cell.txt")
                draw_fields()
                return get
    else:
        if status != "kill" and status != "hit":
            print("[ log ] my shot was in water")
            if status == "hit or kill":
                print("[ log ] it is first 'water' after hit or kill")
                write_file("None", "status.txt")
                write_file("None", "cell.txt")
                cell_to_shot = make_shot()
                write_file(str(cell_to_shot), "beaten_cell.txt")
                draw_fields()
                return get + ". " + str(cells[cell_to_shot[0]]) + str(cell_to_shot[1])
            if start:
                print("[ log ] start and not kill")
                write_file("None", "status.txt")
                write_file("None", "cell.txt")
                cell_to_shot = make_shot()
                write_file(str(cell_to_shot), "beaten_cell.txt")
                draw_fields()
                return get + ". " + str(cells[cell_to_shot[0]]) + str(cell_to_shot[1])
            else:
                print("[ log ] not start and not kill")
                beaten_cell = get_line("beaten_cell.txt")[1:-1]
                if beaten_cell == "None":
                    raise AlgorithmError
                beaten_cell = beaten_cell.split(", ")
                mark_shot(status, (int(beaten_cell[0]), int(beaten_cell[1])))
                cell_to_shot = make_shot()
                write_file(str(cell_to_shot), "beaten_cell.txt")
                write_file("None", "cell.txt")
                write_file("None", "status.txt")
                draw_fields()
                return get + ". " + str(cells[cell_to_shot[0]]) + str(cell_to_shot[1])
        else:
            print("[ log ] my shot was hit or kill")
            print("[ log ] now my task is not to permit to know cell status you said")
            write_file("i hit or kill", "cell.txt")
            write_file("None", "status.txt")
            beaten_cell = get_line("beaten_cell.txt")[1:-1]
            if beaten_cell == "None":
                raise AlgorithmError
            beaten_cell = beaten_cell.split(", ")
            mark_shot(status, (int(beaten_cell[0]), int(beaten_cell[1])))
            cell_to_shot = make_shot()
            write_file(str(cell_to_shot), "beaten_cell.txt")
            draw_fields()
            return str(cells[cell_to_shot[0]]) + str(cell_to_shot[1])

# hold on,
# baby tell me
# it's all right


def naval_battle(Text):
#    print(Text)
    cell = get_line("cell.txt").strip("\n")
    status = get_line("status.txt").strip("\n")
    if cell == "stop" and status == "stop":
        print("sdfsdfsdfsdfsdfsdfsdfsd")
        return "do you want to start a new game"

    if cell != "None":
        c = "1"
    else:
        c = "0"
    if cell == "i hit or kill" or Text.find("hit") != -1  or Text.find("kill") != -1:
        c = "1"

    if cell == "i hit or kill" and Text.find("water") != -1:
       c = "0"

    if cell == "i hit or kill" and status == "water":
      c = "0"

    if status == "hit" or status == "water" or status == "kill" or status == "hit or kill":
        s = "1"
    else:
        s = "0"

    start = s + c
    if status == "start":
        start = "101"

    if status == "stop" or cell == "stop":
        start = "111"

    print("[ log ] cell: " + str(cell))
    print("[ log ] status: " + str(status))
    print("[ log ] start: " + start)


    if start == "101":
        print("[ log ] first request of naval battle")
        cell = detect_cell(Text)
        if cell[0] != 0:
            write_file(cell, "cell.txt")
            return get_naval_battle_request(True)
        else:
            return "please say cell you want to know"
    elif start == "00":
        print("[ log ] know nothing")
        cell = detect_cell(Text)
        status = detect_status(Text)
        print("[ log ] cell is: " + str(cell))
        print("[ log ] status is: " + str(status))
        if cell[1] != 0 and (status == "hit" or status == "water" or status == "kill"):
            write_file(cell, "cell.txt")
            write_file(status, "status.txt")
            return get_naval_battle_request()
#            return "all success"
        else:
            if status == "hit" or status == "water" or status == "kill":
                write_file(status, "status.txt")
                return "please repeat cell"
            else:
                write_file(cell, "cell.txt")
                return "please repeat status"
    elif start == "10":
        print("[ log ] know only status")
        cell = detect_cell(Text)
        if cell[0] != 0:
            write_file(cell, "cell.txt")
            return get_naval_battle_request()
        else:
            return "please repeat cell you want to shot"
    elif start == "01":
        print("[ log ] know only cell")
        status = detect_status(Text)
        if status == "hit" or status == "water" or status == "kill":
            write_file(status, "status.txt")
            return get_naval_battle_request()
        else:
            return "please repeat cell status"
    elif start == "111":
       return "the game is over. if you want to start a new one just tell me"

    #cursor.execute("DELETE FROM voice_helper.naval_battle WHERE field == \"" + str(data[3] + "\";")
    #cursor.execute("INSERT INTO voice_helper.naval_battle (field) VALUES (10);")
    #connection.commit()
"""
    start = data[3]

    cell = detect_cell(Text)
    status = detect_status(Text)
    detect = detect_cell_status(Text)

    if start == "00":
        try:
            if (detect[0] == "kill" or detect[0] == "hit" or detect[0] == "water") and detect[1][0] != 0:
                cell, status = detect[0], detect[1]
            else:
                return detect[0] + ". repeat status and cell please"
        except ValueError:
            status = detect[0]
            cursor.execute("INSERT INTO voice_helper.naval_battle (field) VALUES ('10');")
            connection.commit()
            cursor.execute("INSERT INTO voice_helper.naval_battle (field) VALUES ('" + str(status) "');")
            connection.commit()
            return detect[1]
    elif status == "10":
        if not detect[0].startswith("you should"):
            try:
                if detect[1][0] != 0:
                    cell, status = detect[1], data[4]

            except ValueError:
                return detect[1]
    elif status == "101":
        try:
            if detect[1] != 0:

               return get_shot(detect[1])
            else:

        except:
            return "i have not found any cells in your sentence"
"""

def last_call(Text):
		# may be "govno-code"
		file = open('FILES/DialogStory.txt', mode="r").readlines()
		cut = file[len(file) - 2]
		cut = cut[10:len(cut) - 8]
		last_time = datetime.datetime.strptime(cut, '%Y-%m-%d %H:%M:%S')
		difference = str(datetime.datetime.today() - last_time)
		difference = difference.replace("day", "days")
		difference = difference.replace("dayss", "days")
		if difference.find("days") == -1:
			difference = "0 days, " + difference
		delta_days = int(difference[0:difference.find(" ")])
		difference = difference[difference.find("days, ") + 6:]
		delta_hours = int(difference[0:difference.find(":")])
		difference = difference[difference.find(":") + 1:]
		delta_minutes = int(difference[0:difference.find(":")])
		difference = difference[difference.find(":") + 1:]
		delta_seconds = int(difference[0:difference.find(":")][0:2])
		difference = difference[difference.find(":") + 1:]
		answ = "last request was processed "

		if delta_days == 1:
			string_days = "day"
		else:
			string_days = "days"
		if delta_hours == 1:
			string_hours = "hour"
		else:
			string_hours = "hours"
		if delta_minutes == 1:
			string_minutes = "minute"
		else:
			string_minutes = "minutes"
		if delta_seconds == 1:
			string_seconds = "second"
		else:
			string_seconds = "seconds"

		if delta_days != 0:
			if delta_days < 4:
				if delta_hours != 0:
					return answ + str(delta_days) + " " + string_days + " " + str(delta_hours) + " " + string_hours + " ago"
				else:
					return answ + str(delta_days) + " " + string_days + " ago"
			else:
				return answ + str(delta_days) + " " + string_days + " ago"
		else:
			if delta_hours != 0:
				if delta_hours < 20:
					return answ + str(delta_hours) + " " + string_hours + " " + str(delta_minutes) + " " + string_minutes + " ago"
				else:
					return answ + str(delta_hours) + " " + string_hours + " ago"
			else:
				if delta_minutes != 0:
					return answ + str(delta_minutes) + " " + string_minutes + " " + str(delta_seconds) + " " + string_seconds + " ago"
				else:
					return answ + str(delta_seconds) + " " + string_seconds + " ago"

def what_heard(Text):
	file = open('FILES/DialogStory.txt', mode="r").readlines()
	cut = file[len(file) - 4]
	cut = cut[9:-1]
	return cut

# you found success and recognition
# but into every life a little
# rain must fall

def what_day_of_month(Text):
	res = what_day_today(Text)
	return res[:res.find(",")]

def fests(Text):
	dates = {"independence of united states": "4 of july 1776",
		 "first space trip": "12 april 1961",}
	for k, v in dates.items():
		if Text.find(k) != -1:
			return v
	return "1 of july"

def what_day_today(Text):
	date = find_date_without_week_days(Text)
	m = 0
	d = ""
	while d != "31 of december":
		m -= 1
		d = day(m)
#       print(m)
	for i in range(m + 1, m + 367):
		#print(day(i))
		if day(i) == date:
			break
	print("day in request: " + date)
	date = date.replace(date[:2], digits[int(int(date[:2]))])
	print("delta days: " + str(i))
	today = DAYS[(datetime.datetime.today().weekday() + i) % 7]
	print("day of week in request: " + today)
	return "It is " + date + ", " + today

def recognize_answer(Text):
	file = open('FILES/DialogStory.txt', mode="r").readlines()
	last_answer = file[len(file) - 3]
	last_answer = last_answer[8:-1]
	last_request = what_heard("does't matter what text is here :)")
	print("[ log ] last_request is: " + str(last_request))
	print("[ log ] last_answer is: " + str(last_answer))
	if last_answer.find("album") != -1 and last_answer.find("song") != -1:
		if Text.find("song") != -1:
			recognize_song("song" + last_request)
			#recognize_song()
			return ""
		elif Text.find("album") != -1:
			recognize_song("album" + last_request)
			return ""
		return "not recognized what to turn on"
	elif last_answer.find("new game") != -1:
		if Text.find("yes") != -1:
			return start_naval_battle("abc")
		else:
			return "ok, then i keep waiting for your requests"
	else:
		return "not recognized answer"

# don't call any functions "wolframalpha"
# because it may cause some problems
# import wolframalpha    - main module you shoudn't touch
def wolframalpha_answer(Text):
	try:
		file = open('FILES/requests/' + Text)
		answer = file.read().strip('\n')
		file.close()
	except IOError:
		client = wolframalpha.Client('GE8JUR-XX3KL8W4Q3')
		res = client.query(Text.replace("ask wolframalpha ", ""))
		try:
			answer = next(res.results).text
			#replace = {"^2": " squaareeed", "/": " divide by ", "+": " plus ", " dx": " by dx", "  ": " "}
			#for k, v in replace.items():
			#	answer = answer.replace(k, v)

			file = open('FILES/requests/' + Text, mode='w')
			file.write(answer)
			file.close()
		except:
			answer = "WolframAlpha Error"
	#os.system("./speech.sh " + answer.replace('(', "\(").replace(")", "\)"))
	return answer

def servo(Text):
	for word in Text.split(" "):
		try:
			int(word)
			rotate(int(word))
			return "rotation successful"
		except:
			pass
	return "No integeres found"


if __name__ == "__main__":
	print(current_weather("current weather in new york"))
	print("endline")
