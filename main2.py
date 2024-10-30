import time
# Constants and Initialization
MAP_SIZE = 9
start = (0, 0)  # initial position of Neo
neo = start  # position of Neo
observer = neo
keymaster = ()  # position of Keymaster
closed_cells = []
blocked_cells = []
passed_cells = []
steps_count = 0
accumulated_g = 0
weighted_map_dict = dict()
# Helper Functions
def get_position_input():
    position_input_list = input().split(" ")
    return int(position_input_list[0]), int(position_input_list[1])

def get_walkable_cells(obj:tuple):
    potential_positions = [
        (obj[0], obj[1] + 1), (obj[0], obj[1] - 1),
        (obj[0] - 1, obj[1]), (obj[0] + 1, obj[1])
    ]
    return [pos for pos in potential_positions if pos[0] in range(MAP_SIZE) and pos[1] in range(MAP_SIZE) and pos not in closed_cells]

def get_g(cell):
    return accumulated_g + 1

def get_h(cell):
    return abs(keymaster[0] - cell[0]) + abs(keymaster[1] - cell[1])

def get_f(cell):
    return get_g(cell) + get_h(cell)

'''def get_verified_move_position(new_position):
    if new_position in get_walkable_cells():
        return new_position
    else:
        print("CAN'T MOVE HERE!")
        return neo'''
    
def print_map():
    map_str = ""
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            if x == neo[0] and y == neo[1]:
                map_str += " n "
            elif (x == observer[0] and y == observer[1]):
                map_str += " o "
            elif (x == keymaster[0] and y == keymaster[1]):
                map_str += " k "
            elif ((x,y) in passed_cells):
                map_str += " # "
            elif ((x,y) in closed_cells):
                map_str += " = "
            elif ((x,y) in blocked_cells):
                map_str += " - "
            else:
                map_str += " + "
        map_str += "\n"
    print(map_str)
    
def read_system():
    number_of_items = int(input())
    if number_of_items == 0:
        return False
    items = {}
    for _ in range(number_of_items):
        x, y, status = input().split(' ')
        items[(int(x), int(y))] = status
    return items

def regenerate_route():
    global closed_cells, observer
    accumulated_g = 0
    
    finish = False
    while not finish:
        walkable_cells_and_f = {cell: get_f(cell) for cell in get_walkable_cells(observer) if cell not in blocked_cells}
        min_f_value = min(walkable_cells_and_f.values())
        min_f_cell_list = [cell for cell, f_value in walkable_cells_and_f.items() if f_value == min_f_value]
        
        if len(min_f_cell_list) == 1:
            next_cell = min_f_cell_list[0]
        else:
            next_cell = min(min_f_cell_list, key=lambda cell: get_h(cell))
        observer = next_cell
        accumulated_g += 1 # TODO ENSURE THAT g WORKS PROPERLY
        closed_cells.append(next_cell)
        print(f"m {next_cell[1]} {next_cell[0]}") # TODO FIX OR ENSURE THAT x,y OR y,x DOES NOT MAKE ANY DIFFERENCE
        print_map()
        time.sleep(0.2)
        finish = (observer == keymaster)

def initialize_weighted_map_dict():
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            weighted_map_dict[(x, y)] = (float("inf"), float("inf"), float("inf"), '+') # (x,y) : (h, g, f, type)

# Main Logic


perception_radius = input()
keymaster = get_position_input()


print(f"m {neo[0]} {neo[1]}")
closed_cells.extend((0, 0)) #TODO FIX START CELL SET TO =
finish = False

while not finish:
    observer = neo
    regenerate_route()
    recieved_input = read_system()
    if recieved_input:
        blocked_cells.extend([pos for pos, status in recieved_input.items() if status == "P"])

    walkable_cells_and_f = {cell: get_f(cell) for cell in get_walkable_cells(neo) if cell not in blocked_cells}
    min_f_value = min(walkable_cells_and_f.values())
    min_f_cell_list = [cell for cell, f_value in walkable_cells_and_f.items() if f_value == min_f_value]
    
    if len(min_f_cell_list) == 1:
        next_cell = min_f_cell_list[0]
    else:
        next_cell = min(min_f_cell_list, key=lambda cell: get_h(cell))
    neo = next_cell
    accumulated_g += 1 # TODO ENSURE THAT g WORKS PROPERLY
    closed_cells.append(next_cell)
    passed_cells.append(next_cell)
    print(f"m {next_cell[1]} {next_cell[0]}") # TODO FIX OR ENSURE THAT x,y OR y,x DOES NOT MAKE ANY DIFFERENCE
    steps_count += 1
    #print_map()
    finish = (neo == keymaster)

print(f"e {steps_count}")
# TODO CHECK TESTS FROM CODEFORCES