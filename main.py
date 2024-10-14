
import pygame as pg


CELLSIZE = 50

#TOOLS
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)
    
    def __floordiv__(self, other):
        return Vector2(self.x // other, self.y // other)
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    def to_array(vector):
        return [vector.x, vector.y]
    def normalize(self):
        length = self.magnitude()
        return Vector2(self.x / length, self.y / length)
    def set_from_tuple(self,tup):
        self.x = tup[0]
        self.y = tup[1]





#ENTITIES
class Entity:
    coordinates = Vector2(0,0) ##PIXELS
    position = Vector2(0,0) ##CELLS
    name = ""
    def __init__(self, initial_position:tuple, name):
        self.position.set_from_tuple(initial_position)
        #self.set_cell(initial_position[0], initial_position[1])
        self.coordinates = map.cell_grid[initial_position[0]][initial_position[1]].coordinates
        map.cell_grid[initial_position[0]][initial_position[1]].set_content(self)
        self.name = name
    def set_cell(self, x, y):
        map.get_cell(self.position.x,self.position.y).set_content(None)
        self.position.set_from_tuple((x,y))
        self.coordinates = map.cell_grid[x][y].coordinates
        map.cell_grid[x][y].set_content(self)
    def draw(self, color):
        font = pg.font.Font(None, 32)
        text = font.render(self.name, True, color)
        screen.blit(text, (self.coordinates + Vector2(0, 0)).to_array())

class Actor(Entity):
    perception_radius = 0
    perceived_cells = None 
    def __init__(self, initial_position, name, perception_radius):
        super().__init__(initial_position, name)
        self.perception_radius = perception_radius

class Neo(Actor):
    key_maker_position = Vector2(0,0)
    def __init__(self, initial_position, perception_radius, key_maker_position):
        super().__init__(initial_position, "neo", perception_radius)
        self.key_maker_position = key_maker_position
        

class Smith(Actor):
    def __init__(self, initial_position, perception_radius):
        super().__init__(initial_position, "smith", perception_radius)
    def kill():
        print("Neo is killed.") #TODO: delete

class Sentinel(Actor):
    def __init__(self, initial_position, perception_radius):
        super().__init__(initial_position, "sentinel", perception_radius)
    def kill():
        print("Neo is killed.") #TODO: delete

class Key_maker(Entity):
    def __init__(self, initial_position):
        super().__init__(initial_position, "key_maker")

class Backdoor_key(Entity):
    def __init__(self, initial_position):
        super().__init__(initial_position, "backdoor_key")






#MAIN
class Cell:
    coordinates = Vector2(0,0)
    position = Vector2(0,0)
    size = 50
    piece = pg.Rect(0, 0, size, size)
    content = None
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.piece = pg.Rect(self.coordinates.x, self.coordinates.y, self.size, self.size)
    def draw(self):
        pg.draw.rect(screen, (255, 255, 255), self.piece)
    def set_content(self, content):
        self.content = content
    
        
class Map:
    cellSize = CELLSIZE
    cell_grid = []
    margin = 5
    dimension = Vector2(8,8)
    offset = Vector2(50, 50)
    def __init__(self, dimension:tuple):
        self.dimension.set_from_tuple(dimension)
        for x in range(self.dimension.x):
            col = []
            for y in range(self.dimension.y):
                cell = Cell(Vector2(self.offset.x + x * (self.cellSize + self.margin), self.offset.y +  y * (self.cellSize + self.margin)))
                cell.position = Vector2(x,y)
                col.append(cell)
            self.cell_grid.append(col)
    def get_cell(self, x, y):
        return self.cell_grid[x][y]
    def draw(self):
        for y in range(self.dimension.y):
            for x in range(self.dimension.x):
                self.cell_grid[x][y].draw()



pg.init()
screen = pg.display.set_mode([512,512])
pg.display.set_caption("Matrix Universe")

cell = Cell(coordinates=Vector2(50,50))
map = Map((8, 8))

neo = Neo((0,0), 1, (0,0))
neo.set_cell(4,5)

#smith = Smith((0,0),2)
print(map.get_cell(4,5).content.name)
print(map.get_cell(0,0).content)

running = True

while (running): 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill('BLACK')
    map.draw()
    neo.draw("blue")
    #smith.draw("red")
    pg.display.update()
