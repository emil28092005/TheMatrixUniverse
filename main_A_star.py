import sys
import heapq

min_costs = [[100]*9 for temp in range(9)]
hs = [[0]*9 for temp in range(9)]
astar_map = [['.']*9 for temp in range(9)]
visited_nodes = [[False]*9 for temp in range(9)]
node_parents = [[None]*9 for temp in range(9)]


perception_radius = int(input())
input_list = input().split()
goal_x, goal_y = int(input_list[0]), int(input_list[1])

for i in range(9):
    for j in range(9):
        hs[j][i] = abs(j - goal_y) + abs(i - goal_x)
        min_costs[j][i] = 100

min_costs[0][0] = 0

priority_queue = []
heapq.heappush(priority_queue, (min_costs[0][0] + hs[0][0], 0, 0))

while len(priority_queue) != 0:
    temp, current_x, current_y = heapq.heappop(priority_queue)
    if visited_nodes[current_y][current_x]:
        continue
    visited_nodes[current_y][current_x] = True

    parent_node = node_parents[current_y][current_x]
    path_to_current = []
    path_to_current.append((current_x, current_y))
    while parent_node is not None:
        path_to_current.append(parent_node)
        parent_node = node_parents[parent_node[1]][parent_node[0]]

    for i in reversed(range(len(path_to_current))):
        print(f"m {path_to_current[i][0]} {path_to_current[i][1]}")
        neighbor_count = int(input())
        for temp in range(neighbor_count):
            input_data = input().split()
            neighbor_x_str, neighbor_y_str, neighbor_char = input_data[0], input_data[1], input_data[2]
            neighbor_x = int(neighbor_x_str)
            neighbor_y = int(neighbor_y_str)
            neighbor_char = neighbor_char[0]
            astar_map[neighbor_y][neighbor_x] = neighbor_char

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        neighbor_x = current_x + dx
        neighbor_y = current_y + dy
        if 0 <= neighbor_x < 9 and 0 <= neighbor_y < 9 and not visited_nodes[neighbor_y][neighbor_x] and astar_map[neighbor_y][neighbor_x] not in ('P', 'A', 'S'):
            if min_costs[neighbor_y][neighbor_x] > min_costs[current_y][current_x] + 1:
                node_parents[neighbor_y][neighbor_x] = (current_x, current_y)
                min_costs[neighbor_y][neighbor_x] = min_costs[current_y][current_x] + 1
                heapq.heappush(priority_queue, (min_costs[neighbor_y][neighbor_x] + hs[neighbor_y][neighbor_x], neighbor_x, neighbor_y))

    for i in range(len(path_to_current)):
        print(f"m {path_to_current[i][0]} {path_to_current[i][1]}")
        neighbor_count = int(input())
        for temp in range(neighbor_count):
            input_data = input().split()
            neighbor_x_str, neighbor_y_str, neighbor_char = input_data[0], input_data[1], input_data[2]
            neighbor_x = int(neighbor_x_str)
            neighbor_y = int(neighbor_y_str)
            neighbor_char = neighbor_char[0]
            astar_map[neighbor_y][neighbor_x] = neighbor_char

if min_costs[goal_y][goal_x] != 100:
    print(f"e {min_costs[goal_y][goal_x]}")
else:
    print("e -1")
