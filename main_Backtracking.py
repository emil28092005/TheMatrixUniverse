map_grid = []
minDists = []
keymaker = []
def main():
    global map_grid, minDists
    map_grid = [['.' for _ in range(9)] for _ in range(9)]
    minDists = [[100 for _ in range(9)] for _ in range(9)]
   
    n = int(input())
    position_input = input().split()
    
    x = (int)(position_input[0])
    y = (int)(position_input[1])

    minDists[0][0] = 0
    findShortestPath(0, 0)
    if minDists[y][x] == 100:
        print("e -1")
    else:
        print("e " + str(minDists[y][x]))

def exploreMap(x, y):
    print(f"m {x} {y}")
    n = int(input())
    for _ in range(n):
        inpt = input().split()
        posX, posY, character = inpt[0], inpt[1], inpt[2]
        posX = int(posX)
        posY = int(posY)
        character = character[0]
        map_grid[posY][posX] = character
         

def findShortestPath(x, y):
    exploreMap(x, y)
    if x + 1 < 9 and map_grid[y][x + 1] not in ('P', 'A', 'S') and minDists[y][x + 1] > minDists[y][x] + 1:
        minDists[y][x + 1] = minDists[y][x] + 1
        findShortestPath(x + 1, y)
    exploreMap(x, y)
    if x - 1 >= 0 and map_grid[y][x - 1] not in ('P', 'A', 'S') and minDists[y][x - 1] > minDists[y][x] + 1:
        minDists[y][x - 1] = minDists[y][x] + 1
        findShortestPath(x - 1, y)
    exploreMap(x, y)
    if y + 1 < 9 and map_grid[y + 1][x] not in ('P', 'A', 'S') and minDists[y + 1][x] > minDists[y][x] + 1:
        minDists[y + 1][x] = minDists[y][x] + 1
        findShortestPath(x, y + 1)
    exploreMap(x, y)
    if y - 1 >= 0 and map_grid[y - 1][x] not in ('P', 'A', 'S') and minDists[y - 1][x] > minDists[y][x] + 1:
        minDists[y - 1][x] = minDists[y][x] + 1
        findShortestPath(x, y - 1)
    exploreMap(x, y)

if __name__ == "__main__":
    main()
