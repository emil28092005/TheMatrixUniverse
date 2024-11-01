#import time
MAP_SIZE = 9
start = (0, 0)
neo = start
keymaker = ()

open_set = []
closed_set = []
blocked_set = []

steps_count = 0

map_dict = dict()

def initialize_map_dict():
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            map_dict[(x,y)] = [1000000, 0, ".", None] #g h status previous_cell

def calculate_all_h_for_target(target:tuple):
    for item in map_dict.items():
        item[1][1] = abs(target[0] - item[0][0]) + abs(target[1] - item[0][1]) 

def print_map():
    global neo, keymaker
    map_str = ""
    
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            if (x,y) == neo:
                map_str += " n "
            elif (x,y) == keymaker:
                map_str += " k "  
            #elif (x,y) == (3,7):
            #    map_str += " m " 
            else: 
                map_str += f" {map_dict[(x, y)][2]} "
        map_str += "\n"
    print(map_str)

def print_cells_parameters(cells:list):
    str = ""
    for cell in cells:
        str += f"({cell[0]},{cell[1]}): {map_dict[cell][0]} + {map_dict[cell][1]} = {map_dict[cell][0] + map_dict[cell][1]} ({map_dict[cell][2]}) prev:{map_dict[cell][3]} |  "
    print(str)

def get_walkable_cells_list(actor:tuple):
    potential_positions = [
        (actor[0], actor[1] + 1), (actor[0], actor[1] - 1),
        (actor[0] - 1, actor[1]), (actor[0] + 1, actor[1])
    ]
    return [pos for pos in potential_positions if pos[0] in range(MAP_SIZE) and pos[1] in range(MAP_SIZE)]

def get_open_set_list():
    open_set = []
    for item in map_dict.items():
        if item[1][2] == "+":
            open_set.append(item[0])
    return open_set
    
def get_closed_set_list():
    closed_set = []
    for item in map_dict.items():
        if item[1][2] == "-":
            closed_set.append(item[0])
    return closed_set

def make_opened(cell:tuple):
    map_dict[cell][2] = "+"
    
def make_closed(cell:tuple):
    map_dict[cell][2] = "-"
    
def make_blocked(cell:tuple):
    map_dict[cell][2] = "="

def get_status(cell:tuple):
    return map_dict[cell][2]

def get_g(cell:tuple):
    return map_dict[cell][0]

def get_h(cell:tuple):
    return map_dict[cell][1]

def get_f(cell:tuple):
    return map_dict[cell][0] + map_dict[cell][1]

def set_g(cell:tuple, value):
    map_dict[cell][0] = value

def set_h(cell:tuple, value):
    map_dict[cell][1] = value
        
def add_g(cell:tuple, value):
    map_dict[cell][0] += value

def add_h(cell:tuple, value):
    map_dict[cell][1] += value
    
def assign_previous(cell:tuple, previous_cell:tuple):
    map_dict[cell][3] = previous_cell

def get_previous(cell:tuple):
    return map_dict[cell][3]

def calculate_cell_with_minimal_g(cells:list, filter=None):
    selected_cells = []
    if filter == None:
        for cell in cells:
            if get_status(cell) != "=":
                selected_cells.append(cell)
    else:
        for cell in cells:
            if get_status(cell) == filter and get_status(cell) != "=":
                selected_cells.append(cell)
                
    gs = []
    for cell in selected_cells:
        gs.append(get_g(cell)) # get_f(cell, accumulated_g)
    min_g = min(gs)
    
    min_cells_by_g = []
    for cell in selected_cells:
        if get_g(cell) == min_g: # get_f(cell, accumulated_g)
            min_cells_by_g.append(cell)

            
    next_cell = min_cells_by_g[0]
    return next_cell


def calculate_minimal_cell(cells:list, filter=None):
    selected_cells = []
    if filter == None:
        for cell in cells:
            if get_status(cell) != "=":
                selected_cells.append(cell)
    else:
        for cell in cells:
            if get_status(cell) == filter and get_status(cell) != "=":
                selected_cells.append(cell)
                
    fs = []
    for cell in selected_cells:
        fs.append(get_f(cell)) # get_f(cell, accumulated_g)
    min_f = min(fs)
    
    min_cells_by_f = []
    for cell in selected_cells:
        if get_f(cell) == min_f: # get_f(cell, accumulated_g)
            min_cells_by_f.append(cell)
    
    hs = []
    for cell in min_cells_by_f:
        hs.append(get_h(cell)) #get_h(cell)
    min_h = min(hs)
    
    min_cells_by_h = []
    for cell in min_cells_by_f:
        if get_h(cell) == min_h: #get_h(cell)
            min_cells_by_h.append(cell)
            
    for cell in min_cells_by_h:
        if get_status(cell) == "+":
            next_cell = cell
            return next_cell
    next_cell = min_cells_by_h[0]
    return next_cell

'''def roll_back(looking_for_cell:tuple):
    global neo
    time.sleep(0.1)
    while(get_previous(neo) != None and looking_for_cell not in get_walkable_cells_list(neo)):
        print_cells_paremeters(get_walkable_cells_list(neo))
        print_map()
        neo = get_previous(neo)
        time.sleep(0.1)'''
        
def roll_back(looking_for_cell:tuple):
    global neo
    #time.sleep(0.1)
    while(get_previous(neo) != None and looking_for_cell not in get_walkable_cells_list(neo)):
        #print_cells_parameters(get_walkable_cells_list(neo))
        #print("roll back")
        #print(f"target: ({looking_for_cell[0]},{looking_for_cell[1]})")
        #print_map()
        inputs = read_system()
        neo = get_previous(neo)
        steps_count += 1
        print(f"m {neo[0]} {neo[1]}")
        #time.sleep(0.1)

def get_position_input():
    position_input_list = input().split(" ")
    return int(position_input_list[0]), int(position_input_list[1])

def read_system():
    number_of_items = int(input())
    if number_of_items == 0:
        return False
    items = {}
    for _ in range(number_of_items):
        x, y, status = input().split(' ')
        items[(int(x), int(y))] = status
    return items
        
# TODO MAYBE MAKE A FUNCTION THAT RECALCULATES ALL "PREVIOSES" ON THE MAP USING assign_previous(cell, calculate_cell_with_minimal_g(get_walkable_cells_list(cell), "-"))
keymaker = (5,6)

initialize_map_dict()
calculate_all_h_for_target(keymaker)

make_blocked((0,1))
make_blocked((1,0))

#make_blocked((4,6))

#make_blocked((6,6))

#make_blocked((4,8))
print_map()

#print_cells_parameters(get_walkable_cells_list(neo))
#time.sleep(0.1)
finish = False
seeking_for_target = False
perception_radius = input()
keymaster = get_position_input()
print("m 0 0")
while (finish == False):
    inputs = read_system()
    if inputs != False:
        for inpt in inputs.items():
            if inpt[1] == "P":
                make_blocked(inpt[0])
    
    make_closed(neo)
    for cell in get_walkable_cells_list(neo):
        if get_status(cell) == ".":
            make_opened(cell)
            # TODO find and connect to minimum f|h closed in its own walkable radius
        if get_status(cell) == "+":
            if (get_g(neo) + 1) < get_g(cell) or get_g(cell) == 1000000:
                set_g(cell, (get_g(neo) + 1)) # TODO MAKE A CHECK IF EXISTING g SMALLER THAN NEW ONE
    
    target_cell = calculate_minimal_cell(list(map_dict.keys()), "+") 
   
    if target_cell in get_walkable_cells_list(neo):
        seeking_for_target = False
    if target_cell not in get_walkable_cells_list(neo) and not seeking_for_target:
        roll_back(target_cell)
        seeking_for_target = True
        if target_cell in get_walkable_cells_list(neo):
            next_cell = target_cell
            seeking_for_target = False
        else:            
            next_cell = calculate_minimal_cell(get_walkable_cells_list(neo))
    else:
        next_cell = calculate_minimal_cell(get_walkable_cells_list(neo))
    assign_previous(next_cell, calculate_cell_with_minimal_g(get_walkable_cells_list(next_cell), "-"))
    previous = get_previous(next_cell)
    #print_cells_parameters(get_walkable_cells_list(neo))
    print_map()
    neo = next_cell
    steps_count += 1
    print(f"m {neo[0]} {neo[1]}")
    #time.sleep(0.2)
    if neo == keymaker:
        finish = True
        # TODO MAKE CHECK IF NO PATH EXISTS
print(f"e {steps_count}")