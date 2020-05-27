import mysql.connector
from random import randint, shuffle

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
#    print("ship to mark: " + str(ship))
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
#    print("c is: " + str(c))
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
#    print(ships)
    status = fields[0][cell[1] - 1][cell[0] - 1]
    print("status: " + status)
    if status == "00":
        fields[0][cell[1] - 1][cell[0] - 1] = "11"
        write_fields(fields, ships_to_correct)
        return "in water"
    elif status == "01":
        marked_ship = []
        for ship in ships:
            if ship.count(list(cell)) != 0:
                marked_ship = ship
#        print(marked_ship)
#        print("^ marked ship")
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

        # i can't code more, i want to sleep
        # this "if" is when direction (destination) and first cell of ship (cell_to_search) are defined
        #found, cell = is_there_alone_cell(field[1])

def mark_around_killed(field, ship):
    for i in range(1, 11):
        for j in range(1, 11):
            if ship.count([j, i]) != 0:
#                print("ship cell: " + str((j, i)))
                cells_around = [(i - 2, j - 1), (i - 1, j), (i, j - 1), (i - 1, j - 2), (i - 2, j - 2), (i - 2, j), (i - 1, j - 1),
                                (i, j - 2), (i, j)]
                for k in cells_around:
                    if -1 < k[0] < 10 and -1 < k[1] < 10:
                        if field[k[0]][k[1]] != "KK":
                            field[k[0]][k[1]] = "00"
    return field

def cells_around(cell, diagonal=True, include_cell=True):
    cells = []
    j, i = cell[0], cell[1]

    cells_around = [(j, i - 1), (j, i + 1), (j - 1, i), (j + 1, i)]
    diag = [(j - 1, i - 1), (j + 1, i - 1), (j - 1, i + 1), (j + 1, i + 1)]

    if diagonal:
        for d in diag:
            cells_around.append()
    if include_cell:
        cell_around.append((j, i))

    for k in cells_around:
        if 0 < k[0] < 11 and 0 < k[1] < 11:
            cells.append(k)
    return cells

def situation(field):
    variants = []
    for i in range(1, 11):
        for j in range(1, 11):
            if field[i - 1][j - 1] == "**":
 #               print("** found in " + str((j, i)))
                statuses_around = []
                all_around = cells_around((j, i), False, False)
 #               print("cells : " + str(all_around) + " around cell: " + str((j, i)))
                for cell_around in all_around:
                    statuses_around.append(field[cell_around[1] - 1][cell_around[0] - 1])
                if statuses_around.count("**") == 0:
                    return [[(j, i), 0]]
                else:
                    directions_accord = {(j, i - 1): 1, (j + 1, i): 2, (j, i + 1): 3, (j - 1, i): 4}
                    directions_accord_delta = {(0, -1): 1, (1, 0): 2, (0, 1): 3, (-1, 0): 4}
                    directions_accord_delta_rev = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
                    destination_reverse = {1: 3, 2: 4, 3: 1, 4: 2}
 #                   print("should check where is the nearest cell")
                    destinations = []
                    for cell_around in all_around:
                        if field[cell_around[1] - 1][cell_around[0] - 1] == "**":
                            destinations.append(directions_accord_delta[(cell_around[0] - j, cell_around[1] - i)])
                    if len(destinations) == 1:
                        dest = destination_reverse[destinations[0]]
                        cell_to_check = (j + directions_accord_delta_rev[dest][0], i + directions_accord_delta_rev[dest][1])
#                        print(cell_to_check)
#                        print("^ cell_to_check")
                        if all_around.count(cell_to_check) == 1:
                            variants.append([(j, i), dest])
    return variants

def make_shot():
    fields, ships = get_fields()
    where_to_shot = situation(fields[1])
    print("=====where_to_shot========")
    print(where_to_shot)
    print("=====where_to_shot========")

    if len(where_to_shot) == 0:
        c = "00"
        while c != "10":
            i = randint(1, 10)
            j = randint(1, 10)
            c = fields[1][i - 1][j - 1]
        return (j, i)
    elif len(where_to_shot) == 1:
#        print("single cell found")


        main_cell = where_to_shot[0][0]
        directions = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
        all_around = cells_around(main_cell, False, False)
        dir = [1, 2, 3, 4]
        shuffle(dir)
        for d in dir:
            cell_to_s = (main_cell[0] + directions[d][0], main_cell[1] + directions[d][1])
            try:
                if fields[1][cell_to_s[1] - 1][cell_to_s[0] - 1] == "10" and all_around.count(cell_to_s) != 0:
                    return cell_to_s
            except:
                pass
        return "is there single deck in " + str(main_cell)
    else:
        shuffle(where_to_shot)
#        print("shuffled: " +str(where_to_shot))
        for cell_to_shot in where_to_shot:
            main_cell = cell_to_shot[0]
            print(main_cell)
            direction = cell_to_shot[1]
            directions = {1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}
            cell_to_s = (main_cell[0] + directions[direction][0], main_cell[1] + directions[direction][1])
#            print("cell to start: " + str(main_cell))
#            print("cell to shot: " + str(cell_to_s))
#            print("direction: " + str(direction))
            if fields[1][cell_to_s[1] - 1][cell_to_s[0] - 1] == "10":
                return cell_to_s
        return "You lie to me"

# just walking down the street
# one cloudless sunny day
# just minding my bussines
# thinking my thoughts - nothing much to say
# when suddenly i got hit - imagine my surprise

def mark_shot(Text, cell):
    fields, ships = get_fields()
    ship = []
    if Text.find("kill") != -1:
        for i in range(1, 11):
            for j in range(1, 11):
                if fields[1][i - 1][j - 1] == "**":
                    fields[1][i - 1][j - 1] = "KK"
                    ship.append([j, i])
        ship.append(list(cell))
        fields[1][cell[1] - 1][cell[0] - 1] = "KK"
        fields[1] = mark_around_killed(fields[1], ship)
        k = 0
        for i in range(1, 11):
            for j in range(1, 11):
                if fields[1][i - 1][j - 1] == "KK":
                    k += 1
        if k == 20:
            return "I win"

    elif Text.find("hit") != -1:
        fields[1][cell[1] - 1][cell[0] - 1] = "**"
    elif Text.find("water") != -1:
        fields[1][cell[1] - 1][cell[0] - 1] = "00"
    else:
        return "sorry, i do not understand"
    write_fields(fields, ships)
    return "got it"


def get_cells():
    chars = "abcdefghij"
    cells = []

    for i in range(1, 11):
        for char in chars:
            cells.append(char + str(i))
#    print(cells)
    return cells

def draw_fields():
    fields, ships = get_fields()
    for field in fields:
        for row in field:
            print(row)
        print("===")

if __name__ == "__main__":
    #initialize_field(True)
    #set_up_ships()
    #print(free_around_cell((10, 9), initialize_field(True)))
    #print(possible_to_set_up_ship([10, 10], 1, 3, initialize_field(True)))
    start_game()
    #get_shot((3, 3))
    #print(get_shot((2, 3)))
    #print(get_shot((4, 3)))

    while 1:
        """
        x = int(input())
        y = int(input())
        print(get_shot((x, y)))
        """
        #print("hw")
	#sfgsfgdfgfdg
        """
        fields, ships = get_fields()
        x = int(input())
        y = int(input())
        status = raw_input()
        fields[1][y - 1][x - 1] = status
        write_fields(fields, ships)
        """
        #print(cell, ' ', ' : cell and destination')
        answer = "hit"
        while not (answer.find("hit") == -1 and answer.find("kill") == -1):
            x = int(input())
            y = int(input())
            answer = get_shot((x, y))
            print(answer)

        cell = make_shot()

        Text = str(raw_input("What is about cell " + str(cell) + "?: "))
        print(mark_shot(Text, cell))
    
    #    print(ships)

