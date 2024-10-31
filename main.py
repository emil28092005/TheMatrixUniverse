import time
MAP_SIZE = 9
start = (0, 0)
neo = start
observer = neo
keymaster = ()

green_cells = [] #open cells      +
red_cells = []   #closed cells    -
black_cells = [] #blocked cells   =
blue_cells = []  #traversed cells #

steps_count = 0
#accumulated_g = 0
map_dict = dict()

def initialize_weighted_map_dict():
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            map_dict[(x, y)] = [0, 0, 0, '.'] # (x,y) : (h, g, f, status) ??? [float("inf"), float("inf"), float("inf"), '.']


def print_map():
    map_str = ""
    
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            if map_dict[(x,y)][3] in "kon":
                set_status((x,y), '.')
    
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            
            set_status(keymaster, 'k')
            set_status(observer, 'o')
            set_status(neo, 'n')
            
            map_str += " " + map_dict[(x, y)][3] + " "
        map_str += "\n"
    print(map_str)

def get_g(cell): # TODO MAYBE FIX NEEDED
    #new_g = accumulated_g + 1 
    #if accumulated_g + 1 < map_dict[cell][1]:
    #    new_g = map_dict[cell][1]
    return map_dict[cell][1] + 1

def get_h(cell):
    return abs(keymaster[0] - cell[0]) + abs(keymaster[1] - cell[1])

def get_f(cell):
    if map_dict[cell][3] == '=':
        return float("inf")
    return get_g(cell) + get_h(cell)

def get_walkable_cells(actor:tuple):
    potential_positions = [
        (actor[0], actor[1] + 1), (actor[0], actor[1] - 1),
        (actor[0] - 1, actor[1]), (actor[0] + 1, actor[1])
    ]
    return [pos for pos in potential_positions if pos[0] in range(MAP_SIZE) and pos[1] in range(MAP_SIZE)]

def get_position_input():
    position_input_list = input().split(" ")
    return int(position_input_list[0]), int(position_input_list[1])

def set_status(position:tuple, status:str):
    if status == ".":
        map_dict[position] = [0, 0, 0, '.']
    else:
        map_dict[position][3] = status

def print_cells_paremeters(cells:list):
    str = ""
    for cell in cells:
        str += f"({cell[0]},{cell[1]}): {map_dict[cell][0]} + {map_dict[cell][1]} = {map_dict[cell][2]} ({map_dict[cell][3]}) | "
    print(str)
    
def print_cells_dict_paremeters(cells_dict:dict):
    str = ""
    for cell in cells_dict.items():
        str += f"({cell[0][0]},{cell[0][1]}): {cell[1][0]} + {cell[1][1]} = {cell[1][2]} ({cell[1][3]}) | "
    print(str)    

def get_local_walkable_cells(actor):
    local_walkable_cells = dict()
    for cell in get_walkable_cells(actor):
        if actor == observer and map_dict[cell][3] == "=":
            local_walkable_cells[cell] = [map_dict[cell][0], map_dict[cell][1], float("inf"), map_dict[cell][3]]
        elif actor == observer and map_dict[cell][3] == "-":
            local_walkable_cells[cell] = [map_dict[cell][0], map_dict[cell][1], map_dict[cell][2] + 100000, map_dict[cell][3]]
        else:
            local_walkable_cells[cell] = [map_dict[cell][0], map_dict[cell][1], map_dict[cell][2], map_dict[cell][3]]
    return local_walkable_cells
    
def calculate_next_cell(actor):
    
    # making local mutable walkable cells dictionary
    walkable_cells_dict = dict()
    #walkable_cells_dict = get_local_walkable_cells(actor)
    for cell in get_walkable_cells(actor):
        if actor == observer and map_dict[cell][3] == "=":
            walkable_cells_dict[cell] = [map_dict[cell][0], map_dict[cell][1], map_dict[cell][2], map_dict[cell][3]]
        elif actor == observer and map_dict[cell][3] == "-":
            walkable_cells_dict[cell] = [map_dict[cell][0], map_dict[cell][1], 1000000 + map_dict[cell][2], map_dict[cell][3]]
        else:
            walkable_cells_dict[cell] = [map_dict[cell][0], map_dict[cell][1], map_dict[cell][2], map_dict[cell][3]]
    
    
    fs = []
    for cell_values in walkable_cells_dict.values():
        fs.append(cell_values[2]) # get_f(cell, accumulated_g)
    min_f = min(fs)
    
    min_cells_by_f = []
    for cell in walkable_cells_dict.keys():
        if walkable_cells_dict[cell][2] == min_f: # get_f(cell, accumulated_g)
            min_cells_by_f.append(cell)
    
    hs = []
    for cell in min_cells_by_f:
        hs.append(walkable_cells_dict[cell][0]) #get_h(cell)
    min_h = min(hs)
    
    min_cells_by_h = []
    for cell in min_cells_by_f:
        if walkable_cells_dict[cell][0] == min_h: #get_h(cell)
            min_cells_by_h.append(cell)
            
    next_cell = min_cells_by_h[0]
    return next_cell

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
    global green_cells, red_cells, black_cells, neo, observer
    observer = neo
    previous_cell = ()
    finish = False
    green_cell_found = False
    
    
    while not finish:
        map_dict[observer][1] += 5
        
        # setting green cells
        for cell in get_walkable_cells(observer):
            if map_dict[cell][3] not in "kon-#=":
                set_status(cell, '+')
    
        for cell in get_walkable_cells(observer):
            map_dict[cell][0] = get_h(cell)
            map_dict[cell][1] = get_g(cell)
            map_dict[cell][2] = get_f(cell)
    
        # check if there is any green cell
        green_count = 0
        for cell in get_walkable_cells(observer):
            if map_dict[cell][3] == "+":
                green_cell_found = True
                green_count += 1
        set_status(observer, "-")
        if green_count == 0 and green_cell_found:
            print("return")
            print_cells_paremeters(get_walkable_cells(observer))
            #print_map()
            
            regenerate_route()
            break
    
        
        next_cell = calculate_next_cell(observer)
        
        
        
        #print_cells_paremeters(get_walkable_cells(observer))
        print_cells_paremeters(get_walkable_cells(observer))
        print_map()
        
        previous_cell = observer
        observer = next_cell
        
        
        set_status(previous_cell, '-')
        
        #accumulated_g += 1
        red_cells.append(next_cell)
        
        
        
        time.sleep(0.1)
        if observer == keymaster:
            finish = True


def do_step():
    global neo
    next_cell = calculate_next_cell(neo)
    neo = next_cell
    print(f"m {neo[0]} {neo[1]}")

perception_radius = 2 #input()
keymaster = (6,4) #get_position_input()

initialize_weighted_map_dict()
set_status((0,4),'=')
set_status((1,3),'=') 
set_status((2,2),'=')
set_status((3,1),'=') 
#set_status((4,0),'=') # TODO MAKE ERROR IF ALL PATHS ARE BLOCKED
regenerate_route()

finish = False

while (finish == False):
    do_step()
    print_map()
    recieved_inputs = read_system()

    for inpt in recieved_inputs.items():
        if inpt[1] == "P":
            set_status(inpt[0], "=") 
    
    '''#refreshing the path
    for item in map_dict.items():
        if item[1][3] not in "=":
            set_status(item[0],".")'''
    
    regenerate_route()

