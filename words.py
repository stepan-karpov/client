import mysql.connector
from random import randint
from dictionary import *

def define_vocabulary():
    words = []

    opts = import_dictionary()

    for k, v in opts["cmds"].items():
        for cmd in v:
            for word in cmd.split(" "):
                w = True
                for char in word:
                    if not char.isalpha():
                        w = False
                if words.count(word) == 0 and word.lower() == word and w:
                    words.append(word)
    return words

def export_vocabulary(vocabulary):
    connection = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="password",
          database="voice_helper"
        )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM voice_helper.vocabulary WHERE True;")
    connection.commit()

    q = "INSERT INTO voice_helper.vocabulary (vocabulary) VALUES ('"

    for item in vocabulary:
        q += str(item) + "AAA"

    q = q[:-3] +  "');"
    cursor.execute(q)
    connection.commit()

def get_vocabulary(used=False):
    table_name = "vocabulary"
    if used:
        table_name = "words"
    connection = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="password",
          database="voice_helper"
        )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM voice_helper." + table_name + ";")
    data = cursor.fetchall()
    words = []
    try:
        for word in data[0][0].split("AAA"):
            words.append(word)
    except:
        return []
    return words

def delete_word(word):
    print("[ log ] word to delete: " + str(word))
    data = get_vocabulary()
    try:
        data.remove(word)
        export_vocabulary(data)
        return "i deleted word '" + word + "' from my vocabulary"
    except:
        return "i cant delete this word because i can't find it in my vocabulary"

def insert_word(word):
    print("[ log ] word to insert: " + str(word))
    data = get_vocabulary()
    data.append(word)
    export_vocabulary(data)
    return "word '" + word + "' successfully added"

def find_word(last_word, debug=False):
    data = get_vocabulary()
    used = get_vocabulary(True)
    to_ret = []

#    print(last_word[-1])

    file = open('FILES/DialogStory.txt', mode="r").readlines()
    last_answer = file[len(file) - 3]
    last_answer = last_answer[8:-1]
    i = 1
    while last_answer.endswith("my vocabulary") or last_answer.endswith('"') or last_answer.endswith("one word") \
       or last_answer.endswith("successfully added") or last_answer.endswith("module error") or last_answer.endswith("my word")\
       or last_answer.endswith("this word") or last_answer.endswith("keep playing"):
#    while i != 4:
        i += 1
        last_answer = file[len(file) - 4 * i + 1]
        last_answer = last_answer[8:-1]
        print(last_answer)

    print("[ log ] i is: " + str(i))
    print("[ log ] last_answer: " + last_answer)
    if used.count(last_word) != 0 or (data.count(last_word) == 0 and not debug):
        print("[ log ] debug: " + str(debug))
        print("[ log ] data.count(last_word) = " + str(data.count(last_word)))
        return "sorry, but you can not use this word"
    if not last_answer[-1] == last_word[0] and not last_answer.startswith("ok, i am ready"):
        return "this word does not starts with last char of my word"

    if debug:
        if data.count(last_word) == 0:
            insert_word(last_word)

    for word in data:
#        print(word[0])
        if word[0] == last_word[-1] and used.count(word) == 0:
            to_ret.append(word)

    to_ret = to_ret[randint(0, len(to_ret) - 1)]

    if to_ret == []:
        return "sorry, i don't have more words on this letter"
    else:
        insert_used_word(last_word)
        insert_used_word(to_ret)
        return to_ret

def insert_used_word(word, delete=False):
    data = get_vocabulary(True)
    data.append(word)
    connection = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="password",
          database="voice_helper"
        )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM voice_helper.words WHERE True;")
    connection.commit()
    if not delete:
        q = "INSERT INTO voice_helper.words (variants) VALUES ('"
        for item in data:
            q += str(item) + "AAA"

        q = q[:-3] +  "');"
        cursor.execute(q)
        connection.commit()




if __name__ == "__main__":
    delete_word("destination")
