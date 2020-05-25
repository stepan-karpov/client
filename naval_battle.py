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
    if i != 2:
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
    else:
        ships = field_line.split(";")[:-1]
        for i in range(0, len(ships)):
            ships[i] = ships[i].split(":")[:-1]
        field = ships
#    for row in field:
#        print(row)

    return field

def get_fields():
    return [initialize_field(i=0), initialize_field(i=1)], initialize_field(i=2)


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
    return field, coords

def set_up_ships():
    field = initialize_field(True)
    ships = []
    for i in range(1, 5):
#        print(i, ' ', 5 - i)
        for j in range(1, 6 - i):
            possible = False
            while not possible:
                pos = [randint(1, 10), randint(1, 10)]
                direction = randint(1, 4)
                possible = possible_to_set_up_ship(pos, direction, i, field)
            #print(possible)
            field, ship = stay_up_ship(pos, direction, i, field)
            ships.append(ship)
    """
    for row in field:
        print(row)
        print()
    """
    return field, ships

def write_fields(fields, ships):
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
    q = "INSERT INTO naval_battle (field) VALUES ('"
    for ship in ships:
        for cell in ship:
            q += str(cell) + ":"
        q += ";"
    q += "');"
    cursor.execute(q)
    connection.commit()


def start_game():
    ships_field, ships = set_up_ships()
    fields = [ships_field, initialize_field(not_empty=True)]

    for field in fields:
        for row in field:
            print(row)
        print("==========")
    print(ships)
    write_fields(fields, ships)

def ship_killed(field, ship, cell_no_check):
    for cell in ship:
        if field[cell[1] - 1][cell[0] - 1] != "**":
            return False
    return True

def mark_around(field, ship):
    to_mark = []
    for cell in ship:
        ar = free_around_cell(cell, field, "01")
        for a in ar:
            to_mark.append(a)
    to_mark = list(set(to_mark))

    for cell in to_mark:
        field[cell[1] - 1][cell[0] - 1] = "11"

    for cell in ship:
        field[cell[1] - 1][cell[0] - 1] = "**"
    return field

def no_other_ships(field):
    c = 0
    for row in field:
        for cell in row:
            if cell == "**":
                c += 1
    print("c is: " + str(c))
    if c == 20:
        return True
    else:
        return False


def get_shot(cell):
    fields, ships_to_correct = get_fields()
    ships = []
    for ship in ships_to_correct:
        ship_to_add = []
        for ship_cell in ship:
            ship_cell_mod = ship_cell[1:-1].split(", ")
            ship_cell_mod.reverse()
            ship_cell_mod[0] = int(ship_cell_mod[0])
            ship_cell_mod[1] = int(ship_cell_mod[1])
            ship_to_add.append(ship_cell_mod)
        ships.append(ship_to_add)
    print(ships)
    status = fields[0][cell[1] - 1][cell[0] - 1]
    if status == "00":
        fields[0][cell[1] - 1][cell[0] - 1] = "11"
        write_fields(fields, ships_to_correct)
        return "in water"
    elif status == "01":
        marked_ship = []
        for ship in ships:
            if ship.count(list(cell)) != 0:
                marked_ship = ship
        print(marked_ship)
        print("^ marked ship")
        fields[0][cell[1] - 1][cell[0] - 1] = "**"
        write_fields(fields, ships_to_correct)
        if not ship_killed(fields[0], marked_ship, cell):
            fields[0][cell[1] - 1][cell[0] - 1] = "**"
            write_fields(fields, ships_to_correct)
            return "hit"
        else:
            if not no_other_ships(fields[0]):
                fields[0] = mark_around(fields[0], marked_ship)
                write_fields(fields, ships_to_correct)
                return "you just killed a ship now"
            else:
                return "you win"
    elif status == "**" or status == "11":
        return "sorry, you can not shot there"
        """
        around = free_around_cell(cell, fields[0], "01")
        print(around)
        not_killed = True
        for cell_around in around:
            cell_around_status = fields[0][cell_around[1] - 1][cell_around[0] - 1]
            if cell_around_status == "01":
                not_killed = False
        if not_killed:
            fields[0][cell[1] - 1][cell[0] - 1] = "**"
        """
        return "status was 01"


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
    fields, ships = get_fields()
    for field in fields:
        for row in field:
            print(row)
        print("===")
#    print(ships)
