import os
import time
from random import randint
import datetime
from functions import *
from music import *
from fuzzywuzzy import fuzz
from naval_battle import get_cells
from weather import *
from execute_cmds import *
from dictionary import *


def change_request(Text):
	for to_be_changed in opts["change_request"]:
		if Text == to_be_changed:
			Text = opts["change_request"][to_be_changed]
	nums = "0123456789"
	letters = "abcdefghijklmnopqrstuvwxyz"

	for word in Text.split(" "):
		try:
			int(word)
		except:
			if not word.isalpha() and word.find("'") == -1:
				to_change = ""
				for letter in word:
					if not letter.isalpha():
						to_change += letter
				if cells.count(Text) == 0:
					Text = Text.replace(word, to_change)
					print("[ log ] Warning! " + word + " changed on " + to_change)
	return Text

def prepare_answer(Text):
    start_time = datetime.datetime.now()
    print("[ log ] text preparation module starts ============")
    global opts
    opts = import_dictionary()
    print("[ log ] import_dictionary() time: " + str(datetime.datetime.now() - start_time))
    Text = Text.lower()
    Text = change_request(Text)
    start_time = datetime.datetime.now()
    Answer = callback(Text)
    print("[ log ] callback time: " + str(datetime.datetime.now() - start_time))
    print("[ log ] text preparation module ends ==============")
    return Answer

def callback(Text):
    cmd = Text
#    print(Text)
    for x in opts['tbr']:
        cmd = cmd.replace(x, "").strip()
#    for k, v in opts['tbc'].items():
#        cmd = cmd.replace(k, v).strip()
    Text = cmd
#    print(Text)
    start_time = datetime.datetime.now()
    cmd = recognize_cmd(cmd)
    print("[ log ] recognize_cmd() time: " + str(datetime.datetime.now() - start_time))
    return execute_cmd(cmd['cmd'], Text)

def recognize_cmd(cmd):
	if cmd.find("ask wolframalpha") != -1:
		return {'cmd': 'wolframalpha', 'percent' : 100}

	variants, variants_sorted = import_variants()
	pos = binary_search(variants_sorted, cmd)
#	print(variants.index(cmd))
	#print(variants.index())
	print("[ log ] dictionary length: " +str(len(variants)))
	if pos != -1:
		sum = 0
		pos = variants.index(cmd) + 1
		print("pos of cmd: " + str(pos))
		for k, v in opts["cmds"].items():
			sum += len(v)
#			print(v)
#			print("1: " + v[len(v) - 1] + " pos: " + str(sum))
			if pos <= sum:
				break


		print(str(k))
		return {'cmd': str(k), 'percent': 100}
		try:
			eval(cmd + " + 1")
			return {'cmd': 'count', 'percent' : 100}
		except:
			pass
	else:

		cells = get_cells()
		for cell in cells:
			if Text.split(" ").count():
				return {'cmd': 'naval_battle', 'percent': 100}
# was it all worth it
		units_list = ["meter", "gram", "bit", "newton", "tesla", "byt", "piko", "nano", "micro", 
					  "milli", "centi", "deci", "kilo", "mega", "giga", "tera", "peta"]

		for word in cmd.split(" "):
			for unit in units_list:
				if word.find(unit) != -1:
					answ = units(cmd)
					if answ != "i think that is it impossible to convert this units":
						return {'cmd': 'units', 'percent': 100}
		f = False
		ttl = -1
		RC = {'cmd': '', 'percent': 0}
		for c, v in opts['cmds'].items():
			for x in v:
				vrt = fuzz.ratio(cmd, x)
				if vrt > RC['percent']:
					RC['cmd'] = c
					RC['percent'] = vrt
				if RC['percent'] > 80 and not f:
					f = True
					ttl = 501
					break
				if f:
					ttl -= 1
				if ttl == 0:
					break
			if ttl == 0:
				break
#	print(RC)
	print(RC)
	return RC

def write_request(request, answer):
	file = open('FILES/DialogStory.txt', mode="a")
	file.write("request: " + request + '\n')
	file.write("answer: " + answer + '\n')
	file.write("datetime: " + str(datetime.datetime.today()) + '\n')
	file.write('\n')
	file.close()
	return "writing succesfull"

# so let let them know when they stare, 
# it's just a private affaire 
# they'll have us hung in the air 
# and tell me what do they care

def execute_cmd(cmd, Text):
	#print(cmd)
	dir = subprocess.check_output("ls FILES/requests/", shell=True).decode("utf-8")
	for filename in "FILES/requests":
		if Text == filename:
			return filename.read()

	functions = {
		"time": time,
		"whatdayweek": day_of_a_week,
		"hi": hello,
		"wwyb": how_old_are_you,
		"bye": bye,
		"hmr": how_many_requests,
		"ago": last_call,
		"wdyh": what_heard,
		"whatdom": what_day_of_month,
		"whatdaytoday": what_day_today,
		"music": recognize_song,
		"answer": recognize_answer,
		"wolframalpha": wolframalpha_answer,
		"count": eval,
		#"servo": servo,
		"weather_forecast": weather_forecast,
		"temperature": weather_forecast,
		"wind": weather_forecast,
		"pressure": weather_forecast,
		"sunrise": weather_forecast,
		"sunset": weather_forecast,
		"status": weather_forecast,
		"fests": fests,
		"units": units,
		"naval_battle": naval_battle,
	}

	keys = {"temperature": " KEY: 000", "wind": " KEY: 001", "pressure": " KEY: 010", "sunrise": " KEY: 011", "sunset": " KEY: 100", "status": " KEY: 101"}

	for k, v in functions.items():
		if cmd == k:
			if k in keys:
				return v(Text + keys[k])
			else:
				return v(Text)

	try:
		variat = opts['answ'][cmd]
		return variat[randint(0, len(variat) - 1)]
	except KeyError:
		return cmd




if __name__ == "__main__":
	req = str(input("Request: "))
	#req = "current weather in moscow on today"
	answ = str(prepare_answer(req)).lower()
	print("")
	print("Request: " + req)
	print("Answer: " + answ)
	#write_request(req, answ)
