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
            map_dict[(x, y)] = [float("inf"), float("inf"), float("inf"), '.'] # (x,y) : (h, g, f, status)


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

def get_g(cell, accumulated_g): # TODO MAYBE FIX NEEDED
    return accumulated_g + 1

def get_h(cell):
    return abs(keymaster[0] - cell[0]) + abs(keymaster[1] - cell[1])

def get_f(cell, accumulated_g):
    if map_dict[cell][3] == '=':
        return float("inf")
    return get_g(cell, accumulated_g) + get_h(cell)

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
    map_dict[position][3] = status

def print_cells_paremeters(cells:list):
    str = ""
    for cell in cells:
        str += f"({cell[0]},{cell[1]}): {map_dict[cell][0]} + {map_dict[cell][1]} = {map_dict[cell][2]} ({map_dict[cell][3]}) | "
    print(str)
def calculate_next_cell(actor, accumulated_g):
    
    fs = []
    for cell in get_walkable_cells(actor):
        fs.append(get_f(cell, accumulated_g))
    min_f = min(fs)
    
    min_cells_by_f = []
    for cell in get_walkable_cells(actor):
        if get_f(cell, accumulated_g) == min_f:
            min_cells_by_f.append(cell)
    
    hs = []
    for cell in min_cells_by_f:
        hs.append(get_h(cell))
    min_h = min(hs)
    
    min_cells_by_h = []
    for cell in min_cells_by_f:
        if get_h(cell) == min_h:
            min_cells_by_h.append(cell)
            
    next_cell = min_cells_by_h[0]
    return next_cell

def regenerate_route():
    global green_cells, red_cells, black_cells, neo, observer
    accumulated_g = 0
    observer = neo
    previous_cell = ()
    finish = False
    while not finish:
        
        
        # setting green cells
        for cell in get_walkable_cells(observer):
            if map_dict[cell][3] not in "kon-#=":
                set_status(cell, '+')
    
        for cell in get_walkable_cells(observer):
            map_dict[cell][0] = get_h(cell)
            map_dict[cell][1] = get_g(cell, accumulated_g)
            map_dict[cell][2] = get_f(cell, accumulated_g)
    
        
        next_cell = calculate_next_cell(observer, accumulated_g)
        
        print_cells_paremeters(get_walkable_cells(observer))
        print_map()
        
        previous_cell = observer
        observer = next_cell
        
        set_status(previous_cell, '-')
        
        accumulated_g += 1
        red_cells.append(next_cell)
        
        time.sleep(0.5)
        if observer == keymaster:
            finish = True


perception_radius = 2 #input()
keymaster = (6,4) #get_position_input()

initialize_weighted_map_dict()
set_status((0,4),'=')
set_status((1,3),'=') # TODO FIX STUCK IN A DEAD END ISSUE
regenerate_route()
