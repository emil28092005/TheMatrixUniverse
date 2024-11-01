# Initialize global variables for the map grid and minimum distances
import time

def get_percepted_cells(position:tuple):  
    cells = []  
    for x in range(position[0]- perception_radius, position[0] + perception_radius + 1):
        for y in range(position[1]- perception_radius, position[1] + perception_radius + 1):
            if (x,y) != position:
                cells.append((x,y))
    return cells

failed_tests = 0
passed_tests = 0

total_time = 0
average_time = 0

test_number = 0
with open("20k_testset.txt", "r") as file:
    lines = file.readlines()
        
        
        

        
        
        
line_number = 0
while(test_number < 1000):
    #time.sleep(.5)
    start_time = time.time()
    current_test_lines = []
    for local_line_number in range(14):
        current_line = lines[line_number]
        current_test_lines.append(current_line)
        line_number += 1
        



    
    grid_map = []
    min_distances = []


    def observe(x, y):
        # Sends a move command and receives information on perceived cells around position (x, y)
        #print(f"m {x} {y}")
        for x_temp in range(len(test_map_matrix)):
                for y_temp in range(len(test_map_matrix)):
                    if (x_temp,y_temp) in get_percepted_cells((x, y)) and test_map_matrix[x_temp][y_temp] != ".":
                        grid_map[x_temp][y_temp] = test_map_matrix[x_temp][y_temp]

    def find_path(x, y):
        # Explore surroundings from the current position (x, y)
        observe(x, y)
        
        # Try moving right if within bounds, the cell is safe, and the new distance is shorter
        if x + 1 < 9 and grid_map[y][x + 1] not in ('P', 'A', 'S') and min_distances[y][x + 1] > min_distances[y][x] + 1:
            min_distances[y][x + 1] = min_distances[y][x] + 1
            find_path(x + 1, y)  # Recursive call to explore the new position
        
        observe(x, y)  # Explore again after returning
        
        # Try moving left with similar conditions
        if x - 1 >= 0 and grid_map[y][x - 1] not in ('P', 'A', 'S') and min_distances[y][x - 1] > min_distances[y][x] + 1:
            min_distances[y][x - 1] = min_distances[y][x] + 1
            find_path(x - 1, y)
        
        observe(x, y)  # Explore again after returning

        # Try moving down
        if y + 1 < 9 and grid_map[y + 1][x] not in ('P', 'A', 'S') and min_distances[y + 1][x] > min_distances[y][x] + 1:
            min_distances[y + 1][x] = min_distances[y][x] + 1
            find_path(x, y + 1)
        
        observe(x, y)  # Explore again after returning
        
        # Try moving up
        if y - 1 >= 0 and grid_map[y - 1][x] not in ('P', 'A', 'S') and min_distances[y - 1][x] > min_distances[y][x] + 1:
            min_distances[y - 1][x] = min_distances[y][x] + 1
            find_path(x, y - 1)
        
        observe(x, y)  # Final exploration after checking all directions.



    # Create a 9x9 grid map filled with '.'
    grid_map = [['.' for temp in range(9)] for temp in range(9)]
    # Create a minimum distance grid with initial values set to "infinity" (10000)
    min_distances = [[10000 for temp in range(9)] for temp in range(9)]
        
    # Read perception variant
    perception_radius = int(current_test_lines[1][0])
    # Read Keymaker's position
    keymaker_x = int(current_test_lines[2][1])
    keymaker_y = int(current_test_lines[2][4])
    test_map_matrix = current_test_lines[3:12]
    # Set the starting position (0, 0) with a minimum distance of 0
    min_distances[0][0] = 0
    # Start the recursive pathfinding search from the starting position
    find_path(0, 0)
        
    # Output the result based on the minimum distance to the Keymaker's position
    if min_distances[keymaker_y][keymaker_x] == 10000:
        print("e -1")  # If no path is found, output -1
        time.sleep(1)
        failed_tests += 1
        test_number += 1
        end_time = time.time()
        test_time = end_time - start_time
        total_time += 0 # we don't consider failed tests in statistics
        
    else:
        print("e " + str(min_distances[keymaker_y][keymaker_x]))  # Output the shortest path length
        time.sleep(1)
        passed_tests += 1
        test_number += 1
        end_time = time.time()
        test_time = end_time - start_time
        total_time += test_time
        
average_time = total_time / passed_tests

print("-------BACKTRACKING_RESULTS-------")
print(f"passed tests: {passed_tests}")
print(f"failed tests: {failed_tests}")
print(f"total time: {total_time}")
print(f"average time: {average_time}")

'''
FOR 100 tests
-------BACKTRACKING_RESULTS-------
passed tests: 99
failed tests: 1
total time: 156.93781638145447
average time: 1.58523046849954
'''