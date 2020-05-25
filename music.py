import os
import subprocess
import random


def recognize_song(Text, is_song=False, is_album=False):
	# I hope I was smart enoungh to write this function normally
	artists, albums, songs = get_songs()
	to_play = []
	added = []
	added_names = []
	to_delete  = []
	found = {
		"songs": [],
		"albums": [],
		"artists": []
	}

	alternative_names = {"1 queens album": "album queen 1",
						 "2 queens album": "album queen 2",
						 "3 queens album": "album sheer heart attack",
						 "4 queens album": "album a night at the opera",
						 "5 queens album": "album a day at the races",
						 "6 queens album": "album news of the world",
						 "7 queens album": "album jazz",
						 "8 queens album": "album the game",
						 "10 queens album": "album hot space",
						 "11 queens album": "album the works"}

	#duplicate =

	for to_be_changed, on_what_to_change in alternative_names.items():
		Text = Text.replace(to_be_changed, on_what_to_change)

	#print(Text)

	if Text.find("album") == -1 and Text.find("artist") == -1:
		for album, album_songs in songs.items():
			for  song in album_songs:
				if Text.find(song) != -1:
					print("[ log ]  found \"" + song + "\" in request (song)")
					found["songs"].append(song)
					added.append("song:  " + song)
					added_names.append(song)

	if Text.find("song") == -1 and Text.find("artist") == -1:
		for artist, artist_albums in albums.items():
			for album in artist_albums:
				if Text.find(album) != -1:
					print("[ log ]  found \"" + album + "\" in request (album)")
					found["albums"].append(album)
					added.append("album: " + album)
					added_names.append(album)

	if Text.find("song") == -1 and Text.find("artist") == -1:
		for artist in artists:
			if Text.find(artist) != -1:
				print("[ log ]  found \"" + artist + "\" in request (artist)")
				found["artists"].append(artist)
				added_names.append(artist)


	for i in added:
		for j in added:
			if i[7:] == j[7:] and i != j:
				answ = ("this should be an album or a song", "song or album", "album or song")
				return answ[random.randint(0, len(answ) - 1)]

	for i in added_names:
		for j in added_names:
			if i.find(j) != -1 and i != j:

				to_delete.append(j)

	for k, v in found.items():
		for to_del in to_delete:
			if v.count(to_del) != 0:
				found[k].pop(v.index(to_del))

	#print(found)

	if len(found["albums"]) != 0:
		for song in songs[found["albums"][0]]:
			to_play.append(song)
	if len(found["songs"]) != 0:
		for song in found["songs"]:
			to_play.append(song)
	if len(found["artists"]) != 0:
		for artist in found["artists"]:
			for album in albums[artist]:
				for song in songs[album]:
					to_play.append(song)
		random.shuffle(to_play)

	#to_play contains all songs you need to play without ".mp3" and without path
	#start_to_play(to_play)
	print("======================")
	for s in to_play:
		print("Song to play: " + s)
	print("======================")
	return ""



# to create album list in the same folder
# like this:
# in /home/stepa/Music/queen/queen 1:
# keep your self alive
# doing alright
# great king rat
# ......
# seven seas of rhye 2

# listen to "mr. bad guy" there must be more the life than this
# good song, I like it :)
def make_list(album, album_to_speak):
	print("Should make list of: " + album_to_speak)
	album_without_spaces = album
	album = album.replace(' ', '\\ ')
	cmd = "ls -l " + album + "/"
	songs = []
	output = subprocess.check_output(cmd, shell=True).decode("utf-8").split('\n')
	output.pop(0)
	songs_sorted = []
	output.pop(len(output) - 1)

	for item in output:
		if item.find(".mp") != -1:
			songs.append(item[item.find(":") + 4:])

	print(songs)

	for song in songs:
		edit_song = song.strip().replace(' ', '\\ ')
		cmd = "mid3v2 " + album + "/" + edit_song
		info = subprocess.check_output(cmd, shell=True).decode("utf-8")
		num = info[info.find('TRCK') + 5:]
		if num.find("/") != -1:
			num = int(num[:num.find("/")])
			if num < 10:
				num = "0" + str(num)
			else:
				num = str(num)
		else:
			try:
				num = int(num[:num.find("\n")])
				if num < 10:
					num = "0" + str(num)
				else:
					num = str(num)
			except:
				print("[log] WARNING CREATING ORDER FILE: " + album_without_spaces)
		songs_sorted.append(num + ": " + song)
	songs_sorted.sort()
	#print(songs_sorted)
	file_to_write = open(album_without_spaces + "/order.txt", mode='a')
	for line in songs_sorted:
		#print(line[4:] + "\n")
		file_to_write.write(line[4:]  + '\n')
	file_to_write.close()
	os.system("./speech.sh " + "creating of an order txt file for an album " + album_to_speak + " is successful")



#function to get artists, albums and songs dictionaries :)
def get_songs():
	music_dir = "/home/pi/Music"
	cmd = "grep \".mp\" " + music_dir + "/* -R"
	answer = subprocess.check_output(cmd, shell=True).decode("utf-8").split('\n')[1:-1]
	request = []
	artists = []
	albums = {}
	songs = {}

	for i in range(len(answer)):
		if answer[i].find("order.txt") == -1:
			request.append(answer[i][12 + len(music_dir) + 1:-8])

	for i in range(len(request)):
		artist = request[i][:request[i].find("/")]
		without_artist = request[i][request[i].find("/") + 1:]
		album = without_artist[:without_artist.find("/")]
		#print(without_artist)

		try:
			artists.index(artist)
		except:
			artists.append(artist)
			albums[artist] = []

		if albums[artist].count(album) == 0:
			albums[artist].append(album)

	try:
		albums.pop('')
	except:
		pass

	for k, v in albums.items():
		for al in v:
			songs[al] = []
			try:

				file = open(music_dir + "/" + k + "/" + al + "/order.txt", mode='r')
			except IOError:
				make_list(music_dir + "/" + k + "/" + al, al)
				file = open(music_dir + "/" + k + "/" + al + "/order.txt", mode='r')
			content = file.readlines()
			for i in range(len(content)):
				content[i] = content[i].strip(' ').strip('\n')
			for line in content:
				songs[al].append(line[:-4])
			file.close()
			#make_list(music_dir + "/" + k + "/" + al)
			#print(al + " succes")
			#print("fail: " + al)

		#print(v)
	return artists, albums, songs

	"""
	print(artists)
	print("============================")
	for k, v in albums.items():
		print("Artist: " + k)
		for el in v:
			print("Album: " + el)
	print("============================")

	for k, v in songs.items():
		print("Albums: " + k)
		for el in v:
			print("Song: " + el)
	"""


	"""
	#make_list(music_dir + "/" + "ac dc" + "/" + "unknown")

	#make_list(music_dir + "/" + "Queen/The Game")

	#for song in request:
	#	print(song)



	process= request
	artists = []
	albums = {}

	for i in range(request.index('') + 1):
		if process[0] != '':
			artists.append(process[0])
		process.pop(0)
	print(artists)

	for artist in artists:
		for i in range(len(process)):
			if process[i] == music_dir + "/" + artist + ":":
				for i in range(request.index('') + 1):
					if process[0] != '':
					artists.append(process[0])
				process.pop(0)


	print(albums)
	for i in process:
		print(i)
"""

def get_lists():
	artists, albums, songs = get_songs()
	artist_to_return = []
	albums_to_return = []
	songs_to_return = []
	for artist in artists:
		artist_to_return.append(artist)
	for artist, albums in albums.items():
		for album in albums:
			albums_to_return.append(album)
	for album, songs in songs.items():
		for song in songs:
			songs_to_return.append(song)

	return artist_to_return, albums_to_return, songs_to_return


if __name__ == "__main__":
	print(recognize_song("turn on mister bad guy"))
