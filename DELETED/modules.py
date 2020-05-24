# coding: utf-8
import datetime
REPLACE = {
     'миллиарда': 'миллиард', 'миллиардов': 'миллиард', 'миллиона': 'миллион', 'миллионов': 'миллион',
     'тысячи': 'тысяча', 'тысяч': 'тысяча', 'единица': 'один', 'раз': 'один', 'миллиардный': 'миллиард',
     'миллионный': 'миллион', 'однотысячный': '', 'тысячный': 'тысяча', 'девятьсот': 'девятисотый',
     'восьмисотый': 'восемьсот', 'семисотый': 'семьсот', 'шестисотый': 'шестьсот', 'пятисотый': 'пятьсот',
     'четырехсотый': 'четыреста', 'трехсотый': 'триста', 'двухсотый': 'двести', 'сотый': 'сто',
     'девяностый': 'девяносто', '': '', 'восьмидесятый': 'восемьдесят', 'семидесятый': 'семьдесят',
     'шестидесятый': 'шестьдесят', 'пятидесятый': 'пятьдесят', 'сороковой': 'сорок', 'тридцатый': 'тридцать',
     'двадцатый': 'двадцать', 'девянадцатый': 'девятнадцать', 'восемнадцатый': 'восемнадцать', 'семнадцатый':
     'семнадцать', 'шестнадцатый': 'шестнадцать', 'пятнадцатый': 'пятнадцать', 'четырнадцатый': 'четырнадцать',
     'тринадцатый': 'тринадцать', 'двенадцатый': 'двенадцать', 'одиннадцатый': 'одиннадцать', 'десятый': 'десять',
     'девятый': 'девять', 'восьмой': 'восемь', 'седьмой': 'семь', 'шестой': 'шесть', 'пятый': 'пять',
     'четвертый': 'четыре', 'третий': 'три', 'второй': 'два', 'первый': 'один', 'нулевой': 'ноль', 'нулю': 'ноль',
     'единице': 'один', 'двойка': 'два', 'тройка': 'три', 'четверка': 'четыре', 'пятерка': 'пять', 'шестерка': 'шесть',
     'семерка': 'семь', 'восьмерка': 'восемь', 'девятка': 'девять', 'десятка': 'десять', 'двадцатка': 'двадцать',
     'тридцатка': 'тридцать', 'сотня': 'сто'}


def Chislo(line):
    line = line.lower()
    line.strip()
    line = line.replace("миллиарда", "миллиард").strip()
    line = line.replace("миллиардов", "миллиард").strip()
    line = line.replace("миллиона", "миллион").strip()
    line = line.replace("миллионов", "миллион").strip()
    line = line.replace("тысячи", "тысяча").strip()
    line = line.replace("тысяч", "тысяча").strip()
    line = line.replace("единица", "один").strip()
    line = line.replace("раз", "один").strip()

    line = line.replace("миллиардный", "миллиард").strip()
    line = line.replace("миллионный", "миллион").strip()
    line = line.replace("однотысячный", "").strip()
    line = line.replace("тысячный", "тысяча").strip()
    line = line.replace("девятьсот", "девятисотый").strip()
    line = line.replace("восьмисотый", "восемьсот").strip()
    line = line.replace("семисотый", "семьсот").strip()
    line = line.replace("шестисотый", "шестьсот").strip()
    line = line.replace("пятисотый", "пятьсот").strip()
    line = line.replace("четырехсотый", "четыреста").strip()
    line = line.replace("трехсотый", "триста").strip()
    line = line.replace("двухсотый", "двести").strip()
    line = line.replace("сотый", "сто").strip()
    line = line.replace("девяностый", "девяносто").strip()
    line = line.replace("восьмидесятый", "восемьдесят").strip()
    line = line.replace("семидесятый", "семьдесят").strip()
    line = line.replace("шестидесятый", "шестьдесят").strip()
    line = line.replace("пятидесятый", "пятьдесят").strip()
    line = line.replace("сороковой", "сорок").strip()
    line = line.replace("тридцатый", "тридцать").strip()
    line = line.replace("двадцатый", "двадцать").strip()
    line = line.replace("девянадцатый", "девятнадцать").strip()
    line = line.replace("восемнадцатый", "восемнадцать").strip()
    line = line.replace("семнадцатый", "семнадцать").strip()
    line = line.replace("шестнадцатый", "шестнадцать").strip()
    line = line.replace("пятнадцатый", "пятнадцать").strip()
    line = line.replace("четырнадцатый", "четырнадцать").strip()
    line = line.replace("тринадцатый", "тринадцать").strip()
    line = line.replace("двенадцатый", "двенадцать").strip()
    line = line.replace("одиннадцатый", "одиннадцать").strip()
    line = line.replace("десятый", "десять").strip()
    line = line.replace("девятый", "девять").strip()
    line = line.replace("восьмой", "восемь").strip()
    line = line.replace("седьмой", "семь").strip()
    line = line.replace("шестой", "шесть").strip()
    line = line.replace("пятый", "пять").strip()
    line = line.replace("четвертый", "четыре").strip()
    line = line.replace("третий", "три").strip()
    line = line.replace("второй", "два").strip()
    line = line.replace("первый", "один").strip()
    line = line.replace("нулевой", "ноль").strip()

    line = line.replace("нулю", "ноль").strip()
    line = line.replace("единице", "один").strip()
    line = line.replace("двойка", "два").strip()
    line = line.replace("тройка", "три").strip()
    line = line.replace("четверка", "четыре").strip()
    line = line.replace("пятерка", "пять").strip()
    line = line.replace("шестерка", "шесть").strip()
    line = line.replace("семерка", "семь").strip()
    line = line.replace("восьмерка", "восемь").strip()
    line = line.replace("девятка", "девять").strip()
    line = line.replace("десятка", "десять").strip()
    line = line.replace("двадцатка", "двадцать").strip()
    line = line.replace("тридцатка", "тридцать").strip()
    line = line.replace("сотня", "сто").strip()
    b = ""
    m = ""
    t = ""
    h = ""
    if line.find("миллиард") != -1:
        b = line[0:line.find("миллиард")].strip()
        if b == "":
            b = "один"
        line = line[line.find("миллиард") + 9:].strip()

    if line.find("миллион") != -1:
        m = line[0:line.find("миллион")].strip()
        if m == "":
            m = "один"
        line = line[line.find("миллион") + 8:].strip()

    if line.find("тысяча") != -1:
        t = line[0:line.find("тысяча")].strip()
        if t == "":
            t = "один"
        line = line[line.find("тысяча") + 7:].strip()

    h = line.strip()

    b += " "
    m += " "
    t += " "
    h += " "
    k = 0
    result = 0

    if b != " ":
        while b.find(" ") != -1:
            word = b[0:b.find(" ")].strip()
            if ChBool(IF(word)):
                k += int(IF(word))
            else:
                return "Not INT"
            b = b[b.find(" ") + 1:]
        result += k * 1000000000
        k = 0

    if m != " ":
        while m.find(" ") != -1:
            word = m[0:m.find(" ")].strip()
            if ChBool(IF(word)):
                k += int(IF(word))
            else:
                return "Not INT"
            m = m[m.find(" ") + 1:]
        result += k * 1000000
        k = 0

    if t != " ":
        while t.find(" ") != -1:
            word = t[0:t.find(" ")].strip()
            if ChBool(IF(word)):
                k += int(IF(word))
            else:
                return "Not INT"
            t = t[t.find(" ") + 1:]
        result += k * 1000
        k = 0

    if h != " ":
        while h.find(" ") != -1:
            word = h[0:h.find(" ")].strip()
            if ChBool(IF(word)):
                k += int(IF(word))
            else:
                return "Not INT"
            h = h[h.find(" ") + 1:]
        result += k
    return str(result)


def ChBool(line):
    try:
        int(line)
        return True
    except:
        return False


def IF(Copy):
    sum = 0
    Ch = True
    if (Copy == "девятьсот"): sum += 900
    elif (Copy == "восемьсот"):       sum += 800
    elif (Copy == "семьсот"):       sum += 700
    elif (Copy == "шестьсот"):       sum += 600
    elif (Copy == "пятьсот"):       sum += 500
    elif (Copy == "четыреста"):       sum += 400
    elif (Copy == "триста"):       sum += 300
    elif (Copy == "двести"):       sum += 200
    elif (Copy == "сто"):       sum += 100
    elif (Copy == "девяносто"):       sum += 90
    elif (Copy == "восемьдесят"):       sum += 80
    elif (Copy == "семьдесят"):       sum += 70
    elif (Copy == "шестьдесят"):       sum += 60
    elif (Copy == "пятьдесят"):       sum += 50
    elif (Copy == "сорок"):       sum += 40
    elif (Copy == "тридцать"):       sum += 30
    elif (Copy == "двадцать"):       sum += 20
    elif (Copy == "девятнадцать"):       sum += 19
    elif (Copy == "восемнадцать"):       sum += 18
    elif (Copy == "семнадцать"):       sum += 17
    elif (Copy == "шестнадцать"):       sum += 16
    elif (Copy == "пятнадцать"):       sum += 15
    elif (Copy == "четырнадцать"):       sum += 14
    elif (Copy == "тринадцать"):       sum += 13
    elif (Copy == "двенадцать"):       sum += 12
    elif (Copy == "одиннадцать"):       sum += 11
    elif (Copy == "десять"):       sum += 10
    elif (Copy == "девять"):       sum += 9
    elif (Copy == "восемь"):       sum += 8
    elif (Copy == "семь"):       sum += 7
    elif (Copy == "шесть"):       sum += 6
    elif (Copy == "пять"):       sum += 5
    elif (Copy == "четыре"):       sum += 4
    elif (Copy == "три"):       sum += 3
    elif (Copy == "два"):       sum += 2
    elif (Copy == "один"):       sum += 1
    elif (Copy == "ноль"):       sum += 0
    else:                                      Ch = False

    if (Ch):
        return str(sum)
    else:
        return "Not INT"


def FindOrder(a, b):
    if CountOrd(a) > CountOrd(b):
        return True
    else:
        return False


def CountOrd(a):
    if a >= 0 and a < 10:
        ao = 1
    if a > 9 and a < 100:
        ao = 10
    if a > 99 and a < 1000:
        ao = 100
    if a > 999 and a < 10000:
        ao = 1000
    if a > 9999 and a < 100000:
        ao = 10000
    if a > 99999 and a < 1000000:
        ao = 100000
    if a > 999999 and a < 10000000:
        ao = 1000000
    if a > 999999 and a < 100000000:
        ao = 10000000
    if a > 9999999 and a < 1000000000:
        ao = 10000000
    return ao


def FindInt(line):
    line += " а"
    readyline = line
    k = 0
    Ch = ""
    prev = -1
    ORD=[]
    DEL = False
    F = False
    for word in line.split():
        if F and Chislo(word) == "Not INT":
            #print(Ch)
            for w in Ch.split():
                ORD.append(   CountOrd(  int(Chislo(w))))

            for i in range(len(ORD)):
                if i > 0:
                    if ORD[i-1] <= ORD[i]:
                        DEL = True

            if DEL == False:
                readyline = readyline.replace(Ch, Chislo(Ch.strip()) + " " ).strip()
            else:
                for w in Ch.split():
                    readyline = readyline.replace(w, Chislo(w.strip()) + " ").strip()
            ORD.clear()
        if Chislo(word) != "Not INT":
            Ch += word + " "
            F = True
        else:
            F = False
            Ch = ""

    while "  " in readyline:
        readyline = readyline.replace("  ", " ")
    return readyline[0:len(readyline) - 2]



MONTH = {"январь": "01", "февраль": "02", "март": "03", "апрель": "04", "май": "05", "июнь": "06", "июль": "07",
         "август": "08", "сентябрь": "09", "октябрь": "10", "ноябрь": "11", "декабрь": "12"}
REPL = {"января": "январь", "февраля": "февраль", "марта": "март", "апреля": "апрель", "мая": "май", "июня": "июнь",
        "июля": "июль", "августа": "август", "сентября": "сентябрь", "октября": "октябрь", "ноября": "ноябрь",
        "декабря": "декабрь"}
MONTH2 = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня", "07": "июля",
         "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"}

YEARS = [i for i in range(1600, 2900)]
YEARS.remove(datetime.date.today().year)

def FindDate(Text):
    try:
        YEAR = False
        for month, num in REPL.items():
            if Text.find(month) != -1:
                words = Text.split()
                date = str(words[words.index(month) - 1])
                if int(date) < 10:
                    words[words.index(month) - 1] = "0" + date
                Text = ""
                for el in words:
                    Text += el + " "
                Text = Text.strip()
                Text = Text.replace(month, num).strip()
        for month, num in MONTH.items():
            if Text.find(month) != -1:
                for year in YEARS:
                    if Text.find(str(year)) != -1:
                        YEAR = True
                if not YEAR:
                    Text = Text.replace(" " + month, "." + num + "." + str(datetime.date.today().year)).strip()
                else:
                    Text = Text.replace(" " + month + " ", "." + num + ".")
                    Text = Text.replace("года", "")
                    Text = Text.replace("год", "")
        while "  " in Text:
            Text = Text.replace("  ", " ").strip()
    except:
        Text = "Ошибка в модуле определения даты"
    return Text

def DATETOTEXT(Text):
    date = Text.split(".")
    return date[0] + " " + MONTH2[date[1]] + " " + str(date[2]) + " года"

