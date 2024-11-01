import sys
import heapq

# Initialize cost, heuristic, map, visited nodes, and parent tracking arrays
min_costs = [[10000]*9 for _ in range(9)]  # Initialize minimum cost array with a high value (10000)
hs = [[0]*9 for _ in range(9)]  # Heuristic array for A* (Manhattan distance)
astar_map = [['.']*9 for _ in range(9)]  # Initial unexplored map with '.'
visited_nodes = [[False]*9 for _ in range(9)]  # Track visited nodes
node_parents = [[None]*9 for _ in range(9)]  # Track path parents for backtracking

# Input: perception radius and Keymaker position
perception_radius = int(input())  # 1 or 2 for Neo’s perception variant
input_list = input().split()
goal_x, goal_y = int(input_list[0]), int(input_list[1])  # Keymaker’s coordinates

# Set up heuristic values (Manhattan distance) and initial costs for A*
for i in range(9):
    for j in range(9):
        hs[j][i] = abs(j - goal_y) + abs(i - goal_x)  # Calculate heuristic distance
        min_costs[j][i] = 10000  # Set initial high cost for all cells

min_costs[0][0] = 0  # Starting position (0,0) cost is zero

# Priority queue for A* with starting point at (0,0)
priority_queue = []
heapq.heappush(priority_queue, (min_costs[0][0] + hs[0][0], 0, 0))  # Push initial cell to queue

# Main A* loop
while len(priority_queue) != 0:
    # Extract node with lowest f = g + h value
    temp, current_x, current_y = heapq.heappop(priority_queue)
    if visited_nodes[current_y][current_x]:
        continue
    visited_nodes[current_y][current_x] = True  # Mark node as visited

    # Backtrack to get the path to current node
    parent_node = node_parents[current_y][current_x]
    path_to_current = [(current_x, current_y)]
    while parent_node is not None:
        path_to_current.append(parent_node)
        parent_node = node_parents[parent_node[1]][parent_node[0]]

    # Execute path, querying for perception data
    for i in reversed(range(len(path_to_current))):
        print(f"m {path_to_current[i][0]} {path_to_current[i][1]}")
        neighbor_count = int(input())  # Read the number of perceived items
        # Update map with perceived items
        for _ in range(neighbor_count):
            input_data = input().split()
            neighbor_x = int(input_data[0])
            neighbor_y = int(input_data[1])
            neighbor_char = input_data[2][0]  # Character representing item
            astar_map[neighbor_y][neighbor_x] = neighbor_char  # Update map cell

    # Explore neighboring cells
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # Move in four directions
        neighbor_x = current_x + dx
        neighbor_y = current_y + dy
        # Check boundaries and if cell is unexplored and safe
        if 0 <= neighbor_x < 9 and 0 <= neighbor_y < 9 and not visited_nodes[neighbor_y][neighbor_x] and astar_map[neighbor_y][neighbor_x] not in ('P', 'A', 'S'):
            # Update cost if a better path is found
            if min_costs[neighbor_y][neighbor_x] > min_costs[current_y][current_x] + 1:
                node_parents[neighbor_y][neighbor_x] = (current_x, current_y)
                min_costs[neighbor_y][neighbor_x] = min_costs[current_y][current_x] + 1
                # Add node to priority queue with updated f = g + h value
                heapq.heappush(priority_queue, (min_costs[neighbor_y][neighbor_x] + hs[neighbor_y][neighbor_x], neighbor_x, neighbor_y))

    # Repeat path execution to keep querying
    for i in range(len(path_to_current)):
        print(f"m {path_to_current[i][0]} {path_to_current[i][1]}")
        neighbor_count = int(input())  # Re-read surroundings
        for _ in range(neighbor_count):
            input_data = input().split()
            neighbor_x = int(input_data[0])
            neighbor_y = int(input_data[1])
            neighbor_char = input_data[2][0]
            astar_map[neighbor_y][neighbor_x] = neighbor_char  # Update map

# Check if the goal is reached and output the result
if min_costs[goal_y][goal_x] != 10000:
    print(f"e {min_costs[goal_y][goal_x]}")  # Output shortest path length
else:
    print("e -1")  # Output -1 if unsolvable.
