import mysql.connector
from random import randint

def initialize_field(empty=False, i=0, not_empty=False):
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="voice_helper"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM naval_battle")

    data = cursor.fetchall()

    try:
        field_line = data[i][0]
    except:
        pass
#    print(field_line)

    field = []
    field_row = []

    for i in range(0, 100):
        if not empty and not not_empty:
            cell = field_line[i*2] + field_line[i*2+1]
        elif not_empty:
            cell = "10"
        elif empty:
            cell = "00"
        field_row.append(cell)
        if (i - 9) % 10 == 0:
            field.append(field_row)
            field_row = []


#    for row in field:
#        print(row)

    return field

def get_fields():
    return [initialize_field(i=0), initialize_field(i=1)]


def free_around_cell(cell, field, pattern="00"):
    if (not 0 < cell[0] < 11) or (not 0 < cell[1] < 11):
        if pattern == "01":
            return []
        else:
            return False
    """
    print("field to check===")
    for row in field:
        print(row)
    print("====")
    """
    x = cell[0]
    y = cell[1]
    #print("cell: " + str(cell[0]) + "," + str(cell[1]))
    coords = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y), (x, y + 1),
		(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
    coord_exists = []
    for coord in coords:
        if -1 < coord[0] - 1 < 10 and -1 < coord[1] - 1 < 10:
            coord_exists.append((coord[0], coord[1]))
    if len(coord_exists) == 0:
        if pattern == "01":
            return []
        else:
            return False
    #print(coords)
    c = 0
    """
    for i in range(0, 10):
        for j in range(0, 10):
#            print(i, ' ', j)
            c += 1
            if coord_exists.count((j, i)) != 0:
                print("**", end=" ")
            else:
                print(field[i][j], end=" ")
        print("")
    print(coord_exists)
    """
    if pattern == "01":
        return coord_exists
    for coord in coord_exists:
#        print(coord[0] - 1, ' ', coord[1] - 1)
        if field[coord[0] - 1][coord[1] - 1] != "00":
            return False
    return True

def possible_to_set_up_ship(pos, direction, deck, field):
    """
    print("setting up new ship")
    print("ship: ")
    print(str(pos) + " " + str(direction) + " " + str(deck))
    print("field: ")
    for row in field:
        print(row)
    """
    coords = []
    dir = ((0, -1), (1, 0), (0, 1), (-1, 0))
    for i in range(0, deck):
        coords.append((	pos[0] + dir[direction - 1][0] * i, pos[1] + dir[direction - 1][1] * i))
    #print("coords of ship: ")
    #print(coords)
    for cell in coords:
        if not free_around_cell((cell[0], cell[1]), field):
#            print("cell " + str(cell) + " is not free")
#            print("END OF SHIP ==========================================", 'False')
            return False
#    print("END OF SHIP ==================================================", 'True')
    return True


def stay_up_ship(pos, direction, deck, field):
    coords = []
    dir = ((0, -1), (1, 0), (0, 1), (-1, 0))
    for i in range(0, deck):
        coords.append(( pos[0] + dir[direction - 1][0] * i, pos[1] + dir[direction - 1][1] * i))
    for cell in coords:
        field[cell[0] - 1][cell[1] - 1] = "01"
    return field

def set_up_ships():
    field = initialize_field(True)

    for i in range(1, 5):
#        print(i, ' ', 5 - i)
        for j in range(1, 6 - i):
            possible = False
            while not possible:
                pos = [randint(1, 10), randint(1, 10)]
                direction = randint(1, 4)
                possible = possible_to_set_up_ship(pos, direction, i, field)
            #print(possible)
            field = stay_up_ship(pos, direction, i, field)
#            print("new ship: ")
    """
    for row in field:
        print(row)
        print()
    """
    return field

def write_fields(fields):
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="voice_helper"
    )

    cursor = connection.cursor()
    cursor.execute("DELETE FROM voice_helper.naval_battle WHERE True;")
    connection.commit()
    f = ""
    for field in fields:
        for row in field:
            for cell in row:
                f += cell
        q = "INSERT INTO naval_battle (field) VALUES ('" + f + "');"
        cursor.execute(q)
        connection.commit()
        f = ""


def start_game():
    fields = [set_up_ships(), initialize_field(not_empty=True)]

    for field in fields:
        for row in field:
            print(row)
        print("==========")
    write_fields(fields)

def get_shot(cell):
    fields = get_fields()
    status = fields[0][cell[1] - 1][cell[0] - 1]
    if status == "00":
        fields[0][cell[1] - 1][cell[0] - 1 = "11"
        return "in water"



#initialize_field(True)
#set_up_ships()
#print(free_around_cell((10, 9), initialize_field(True)))
#print(possible_to_set_up_ship([10, 10], 1, 3, initialize_field(True)))
start_game()
#get_shot((3, 3))
#print(get_shot((2, 3)))
#print(get_shot((4, 3)))

while 1:
    x = int(input())
    y = int(input())
    print(get_shot((x, y)))
    #print("hw")
    fields = get_fields()
    for field in fields:
        for row in field:
            print(row)
        print("===")

