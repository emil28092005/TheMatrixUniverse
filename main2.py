#import time #TODO TEMP

MAP_SIZE = 8
map = []
start = (0, 0) #initial position of Neo
neo = start #position of Neo
keymaster = () #position of Keymaster

def get_position_input():
    position_input_list = (input().split(" "))
    return ((int)(position_input_list[0]), (int)(position_input_list[1]))

def get_walkable_cells():
    walkable_cells = []
    potential_positions = []
    potential_positions.append((neo[0], neo[1] + 1))
    potential_positions.append((neo[0], neo[1] - 1))
    potential_positions.append((neo[0] - 1, neo[1]))
    potential_positions.append((neo[0] + 1, neo[1])) 
    for i in potential_positions:
        if i[0] in range(MAP_SIZE) and i[1] in range(MAP_SIZE) and i not in closed_cells:
            walkable_cells.append(i)
    return walkable_cells
    
def get_g(cell:tuple):
    return abs(start[0] - cell[0]) + abs(start[1] - cell[1]) #TODO FROM START OR NEO?

def get_h(cell:tuple):
    return abs(keymaster[0] - cell[0]) + abs(keymaster[1] - cell[1])

def get_f(cell:tuple):
    return get_g(cell) + get_h(cell) 

def get_verified_move_position(new_postion:tuple):
    if new_postion in get_walkable_cells():
        return new_postion
    else:
        print("CAN'T MOVE HERE!") #TEMP
        return neo

def print_wheights(cell:tuple):
    print(f"{get_g(cell)} + {get_h(cell)} = {get_f(cell)}") 
    
def print_map_f():
    print("f")
    map_str = ""
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            if x == neo[0] and y == neo[1]:
                map_str += " n "
            elif (x == keymaster[0] and y == keymaster[1]):
                map_str += " k "
            else:
                f = get_f((x,y))
                
                
                if len(str(f)) == 2:
                    f_str = " " + str(f)
                else:
                    f_str = " " + str(f) + " "
                map_str += f_str
        map_str += "\n"
    print(map_str)
    
def print_map_g():
    print("g")
    map_str = ""
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            if x == neo[0] and y == neo[1]:
                map_str += " n "
            elif (x == keymaster[0] and y == keymaster[1]):
                map_str += " k "
            else:
                f = get_g((x,y))
                
                
                if len(str(f)) == 2:
                    f_str = " " + str(f)
                else:
                    f_str = " " + str(f) + " "
                map_str += f_str
        map_str += "\n"
    print(map_str)

def print_map_h():
    print("h")
    map_str = ""
    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            if x == neo[0] and y == neo[1]:
                map_str += " n "
            elif (x == keymaster[0] and y == keymaster[1]):
                map_str += " k "
            else:
                f = get_h((x,y))
                
                
                if len(str(f)) == 2:
                    f_str = " " + str(f)
                else:
                    f_str = " " + str(f) + " "
                map_str += f_str
        map_str += "\n"
    print(map_str)

def read_system():
    number_of_items = (int)(input())
    items = dict()
    if number_of_items == 0:
        return False
    else:
        
        for i in range(number_of_items):
            input_str_split = input().split(' ')
            input_formatted = []
            input_formatted.append((int)(input_str_split[0]))
            input_formatted.append((int)(input_str_split[1]))
            input_formatted.append((input_str_split[2]))
            
            
            items[(input_formatted[0], input_formatted[1])] = input_formatted[2] #SWAP 0 and 1 ?
        
    return items
    

perception_radius = input()
position_input = get_position_input()

keymaster = (position_input[0], position_input[1])

finish = False

closed_cells = []

#print("neo:")
#print(neo)
#print("keymaster:")
#print(keymaster)
walkable_cells_and_f = dict()
for i in get_walkable_cells():
    walkable_cells_and_f[i] = get_f(i)
min_f_cell = min(walkable_cells_and_f, key=walkable_cells_and_f.get)    
#print("min_f:")
#print(min_f_cell)
#neo = get_verified_move_position(position_input)
#print(walkable_cells_and_f)
print(f"m {neo[0]} {neo[1]}")
steps_count = 0
while (finish == False):
    '''
    position_input = get_position_input()
    print(position_input)
    neo = get_verified_move_position(position_input)
    print("\nneo:")
    print(neo)
    print("\nkeymaster:")
    print(keymaster)
    print("\nwalkabe cells")
    '''
    #A*
    
    
    recieved_input = read_system()
    
    if recieved_input != False:
        for i in recieved_input.items():
            if i[1] == "P":
                closed_cells.append(i[0])
    
    walkable_cells_and_f = dict()
    for i in get_walkable_cells():
        walkable_cells_and_f[i] = get_f(i)
    min_f_cell = min(walkable_cells_and_f, key=walkable_cells_and_f.get)
    min_f_value = walkable_cells_and_f[min_f_cell]

    # Находим минимальное значение f
    min_f_value = min(walkable_cells_and_f.values())

    # Собираем все ячейки с минимальным значением f
    min_f_cell_list = [cell for cell, f_value in walkable_cells_and_f.items() if f_value == min_f_value]

    # Если только одна ячейка с минимальным f, выбираем её
    if len(min_f_cell_list) == 1:
        next_cell = min_f_cell_list[0]
    else:
        # Если таких ячеек несколько, выбираем ту, у которой минимальный h
        next_cell = min(min_f_cell_list, key=lambda cell: get_h(cell))

    #time.sleep(3) #TODO TEMP
    neo = get_verified_move_position(next_cell)
    closed_cells.append(next_cell)
    print(f"m {next_cell[0]} {next_cell[1]}")
    steps_count += 1
    finish = neo == keymaster
    '''
    for i in walkable_cells_and_f.items():
        cell = i[0]
        print(cell)
        print(f"{get_g(cell)} + {get_h(cell)} = {get_f(cell)}") 
    print(neo)
    print(print_wheights(neo))
    print_map_g()
    print_map_h()
    print_map_f()
    print(walkable_cells_and_f)
    
    
    
    
    print("min_f:")
    print(min_f_cell)
    print("min_f_count:")
    print(len(min_f_cell_list))
    #neo = get_verified_move_position(position_input)
    for i in walkable_cells_and_f.items():
        cell = i[0]
        print(cell)
        print(f"{get_g(cell)} + {get_h(cell)} = {get_f(cell)}") 
    print(walkable_cells_and_f)
    print("next_cell:")
    print(next_cell)'''
    #print_map_f()
#print("FINISH!")
print(f"e {steps_count}")