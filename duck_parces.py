#pip3 install duckduckgo3
import duckduckgo
import time
import mysql.connector
def fin_smtH_ddg(key):
	st = duckduckgo.get_zci(key)
	return st

def delete_url(st):
	i = 0
	j = 0
	st2 = ''
	while st[j+1] != '(':
		i = st[j]
		st2 += i
		j +=1
	return st2

def wrt_mysql(table_name, column_name, to_add_first, to_add_second):
	connection = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="voice_helper"
	)
	cursor = connection.cursor()
	#make a copy
	cursor.execute("SELECT * FROM " + table_name)
	data = cursor.fetchall()
	#delete all inf
	cursor.execute("DELETE FROM " + table_name + " WHERE True;")
	connection.commit()

	try:
		first_row = data[0][0]
		second_row = data[1][0]
	except:
		first_row = ''
		second_row = ''

	cursor.execute("INSERT INTO " + table_name + "(" + column_name + ")" + "VALUES ('" + str(first_row) + str(to_add_first) + "000" + "');")
	connection.commit()

	cursor.execute("INSERT INTO " + table_name + "(" + column_name + ")" + "VALUES ('" + str(second_row) + str(to_add_second) + "000" + "');")
	connection.commit()

def main():
	key = str(input('Seacrh key: '))
	start = time.time()
	st = fin_smtH_ddg(key)
	answer = delete_url(st)
	end = time.time()
	print(answer)
	print("[ log ]" + " " + "lead time =" + " " + str(end - start))
	wrt_mysql('qna', 'q_a', key, answer)
	print("[ log ]" + " " + "MYSQL UPDATED")
if __name__ == '__main__':
	main()
