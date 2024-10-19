
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
    cell = None
    def __init__(self, initial_position:tuple, name):
        self.position.set_from_tuple(initial_position)
        self.name = name
        self.set_cell(initial_position[0], initial_position[1])

    def set_cell(self, x, y):
        map.get_cell(self.position.x,self.position.y).set_content(None)
        self.position.set_from_tuple((x,y))
        self.coordinates = map.cell_grid[x][y].coordinates
        map.get_cell(x,y).set_content(self)
        cell = map.get_cell(self.position.x,self.position.y)
    def get_cell(self):
        return self.cell
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
        super().__init__(initial_position, "neo", 1)
        self.key_maker_position = key_maker_position
    def percept(self):
        upper_left_corner_cell = map.get_cell(self.position.x - self.perception_radius, self.position.y - self.perception_radius)
        for y in range(upper_left_corner_cell.position.y, upper_left_corner_cell.position.y + self.perception_radius * 2 + 1):
            for x in range(upper_left_corner_cell.position.x, upper_left_corner_cell.position.x + self.perception_radius * 2 + 1):
                #print(x,y)
                
                if x < map.dimension.x and y < map.dimension.y:
                    
                    cell = map.get_cell(x, y) #TODO:PROPER COLORIZE
                    print(x,y)
                    cell.add_perceptor(self)
                    #print(map.get_cell(x,y).perceptors[0].name)
                    #print(cell.position.to_array())
                    #print(cell.perceptors[0].name)
        for x in range(8):
            for y in range(8):
                print(x,y)
                print(map.get_cell(x,y).perceptors[0])
        
                    
                
                
        

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
    perceptors = [None]
    color = (255, 255, 255)
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.piece = pg.Rect(self.coordinates.x, self.coordinates.y, self.size, self.size)
    def draw(self):
        if self.has_perceptor("neo"):
            #cell.set_color((0,255,0)) #TODO:COLORIZE
            print(self.position.to_array())
            pg.draw.rect(screen, "green", self.piece)
        else:
            #print(5555555555555555)
            pg.draw.rect(screen, "white", self.piece)
    def set_color(self, color):
        self.color = color
    def set_content(self, content):
        self.content = content
    def add_perceptor(self, new_perceptor):
        self.perceptors.append(new_perceptor)
    def delete_perceptor(self, redundant_perceptor):
        if self.has_perceptor(redundant_perceptor.name):
            self.perceptors.remove(redundant_perceptor)    
        else:
            pass #print(123)
    def has_perceptor(self, name):
        for i in self.perceptors:
            if (i != None and i.name == name):
                #print(987654321)
                #print(i)
                #print(self.position.to_array())
                return True
        #print(123456)
        return False
    
        
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
#print(map.get_cell(4,5).content.name)
#print(map.get_cell(0,0).content)

running = True


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill('BLACK')
    map.draw()
    neo.draw("blue")
    neo.percept()
    neo.set_cell(1,1)
    #print(map.get_cell(7,7).perceptors[0].name)
    
    pg.display.update()
    pg.time.delay(5000)


