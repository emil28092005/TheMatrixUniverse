
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





#ENTITIES
class Entity:
    position = Vector2(0,0)
    name = ""
    def __init__(self, initial_position, name):
        self.position = initial_position
        self.name = name
    def draw(self):
        font = pg.font.Font(None, 32)
        text = font.render(self.name, True, (0, 255, 255))
        screen.blit(text, (self.position + Vector2(0, 0)).to_array())

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
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.position = coordinates // self.size
        self.piece = pg.Rect(self.coordinates.x, self.coordinates.y, self.size, self.size)
    def draw(self):
        pg.draw.rect(screen, (255, 255, 255), self.piece)
        
class Map:
    cellSize = CELLSIZE
    cell_Grid = []
    margin = 5
    dimension = Vector2(8,8)
    offset = Vector2(50, 50)
    def __init__(self):
        
        for x in range(self.dimension.x):
            col = []
            for y in range(self.dimension.y):
                col.append(Cell(Vector2(self.offset.x + x * (self.cellSize + self.margin), self.offset.y +  y * (self.cellSize + self.margin))))
            self.cell_Grid.append(col)
    def draw(self):
        for y in range(self.dimension.y):
            for x in range(self.dimension.x):
                print(self.cell_Grid[x][y].coordinates.y)
                self.cell_Grid[x][y].draw()



pg.init()
screen = pg.display.set_mode([512,512])
pg.display.set_caption("Matrix Universe")

cell = Cell(coordinates=Vector2(50,50))
map = Map()

neo = Neo(map.cell_Grid[0][0].coordinates, 1, Vector2(0,0))
neo.position = map.cell_Grid[1][0].coordinates
running = True

while (running): 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill('BLACK')
    map.draw()
    neo.draw()
    pg.display.update()
