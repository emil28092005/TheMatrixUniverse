

def get_position_input():
    position_input_list = (input().split(" "))
    position_input_tuple = ()
    for i in position_input_list:
        position_input_tuple += (i,)
    return position_input_tuple

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
    return abs((neo[0] - cell[0]) + (neo[1] - cell[1]))

def get_h(cell:tuple):
    return abs((keymaster[0] - cell[0]) + (keymaster[1] - cell[1]))

def get_f(cell:tuple):
    return get_g(cell) + get_h(cell) 

def set_position(new_postion:tuple):
    neo = new_postion





MAP_SIZE = 8
map = []
start = (0, 0) #initial position of Neo
neo = start #position of Neo
keymaster = () #position of Keymaster

perception_radius = input()
position_input = get_position_input()

keymaster = (position_input[0], position_input[1])



print(neo)
print(get_walkable_cells())

while (True):
    position_input = get_position_input()
    set_position(position_input)
    print(neo)
    print(get_walkable_cells())