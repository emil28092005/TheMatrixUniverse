# Initialize global variables for the map grid and minimum distances
grid_map = []
min_distances = []

def main():
    global grid_map, min_distances
    # Create a 9x9 grid map filled with '.'
    grid_map = [['.' for temp in range(9)] for temp in range(9)]
    # Create a minimum distance grid with initial values set to "infinity" (10000)
    min_distances = [[10000 for temp in range(9)] for temp in range(9)]
    
    # Read perception variant
    variant = int(input())
    # Read Keymaker's position
    position_input = input().split()
    keymaker_x = int(position_input[0])
    keymaker_y = int(position_input[1])

    # Set the starting position (0, 0) with a minimum distance of 0
    min_distances[0][0] = 0
    # Start the recursive pathfinding search from the starting position
    find_path(0, 0)
    
    # Output the result based on the minimum distance to the Keymaker's position
    if min_distances[keymaker_y][keymaker_x] == 10000:
        print("e -1")  # If no path is found, output -1
    else:
        print("e " + str(min_distances[keymaker_y][keymaker_x]))  # Output the shortest path length

def observe(x, y):
    # Sends a move command and receives information on perceived cells around position (x, y)
    print(f"m {x} {y}")
    num_items = int(input())  # Number of items perceived in the vicinity
    for temp in range(num_items):
        # Process each perceived item with coordinates and type
        item_info = input().split()
        item_x, item_y, item_type = item_info[0], item_info[1], item_info[2]
        item_x = int(item_x)
        item_y = int(item_y)
        item_type = item_type[0]
        # Update the grid map with the perceived item at the given position
        grid_map[item_y][item_x] = item_type

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

if __name__ == "__main__":
    main()
