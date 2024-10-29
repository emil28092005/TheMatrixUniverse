
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
        if i[0] in range(MAP_SIZE) and i[1] in range(MAP_SIZE):
            walkable_cells.append(i)
    return walkable_cells
    
def get_g(cell:tuple):
    return abs((start[0] - cell[0]) + (start[1] - cell[1])) #TODO FROM START OR NEO?

def get_h(cell:tuple):
    return abs((keymaster[0] - cell[0]) + (keymaster[1] - cell[1]))

def get_f(cell:tuple):
    return get_g(cell) + get_h(cell) 

def get_verified_move_position(new_postion:tuple):
    if new_postion in get_walkable_cells():
        return new_postion
    else:
        print("CAN'T MOVE HERE!") #TEMP
        return neo


perception_radius = input()
position_input = get_position_input()

keymaster = (position_input[0], position_input[1])



print("neo:")
print(neo)
print("keymaster:")
print(keymaster)
walkable_cells_and_f = dict()
for i in get_walkable_cells():
    walkable_cells_and_f[i] = get_f(i)
min_f_cell = min(walkable_cells_and_f, key=walkable_cells_and_f.get)    
print("min_f:")
print(min_f_cell)
#neo = get_verified_move_position(position_input)
print(walkable_cells_and_f)

while (True):
    position_input = get_position_input()
    print(position_input)
    neo = get_verified_move_position(position_input)
    print("\nneo:")
    print(neo)
    print("\nkeymaster:")
    print(keymaster)
    print("\nwalkabe cells")
    #A*
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
    print(next_cell)