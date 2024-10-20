import pygame as pg

class Cell:
    coordinates = (0, 0)
    position = (0, 0)
    size = 50
    perceptor = None
    content = None
    rect = pg.Rect(0, 0, size, size)
    border_width = 2
    g = 1
    h = 2
    f = g + h
    def __init__(self, position):
        self.set_position(position)
        self.rect = pg.Rect(self.coordinates[0], self.coordinates[1],
                            self.size - self.border_width, self.size - self.border_width)
    def set_position(self, position):
        self.position = position
        self.coordinates = (self.position[0] * self.size,
                            self.position[1] * self.size)
    def set_content(self, content):
        self.content = content
        self.content
    def set_perceptor(self, perceptor):
        self.perceptor = perceptor
    def clear_perceptor(self):
        self.perceptor = None
    def draw(self):
        if self.perceptor == None:
            pg.draw.rect(screen, "white", self.rect)
        else:
            pg.draw.rect(screen, self.perceptor.color, self.rect) #TODO:DELETE THIS AND MAKE OVERLAPING HALF_TRANSPARENT ADDITIONAL CELLS SPAWNIN UNDER PERCEPTION IN NEO CLASS
        
        g_font = pg.font.Font(None, 14)
        text = g_font.render((str)(self.g), True, "black")
        screen.blit(text, ((self.coordinates[0] + self.size * 0.05, self.coordinates[1] + self.size * 0.75)))
           
        h_font = pg.font.Font(None, 14)
        text = h_font.render((str)(self.h), True, "black")
        screen.blit(text, ((self.coordinates[0] + self.size * 0.8, self.coordinates[1] + self.size * 0.75)))
        
        
        f_font = pg.font.Font(None, 16)
        text = f_font.render((str)(self.f), True, "maroon")
        screen.blit(text, ((self.coordinates[0] + self.size * 0.425, self.coordinates[1] + self.size * 0.7)))
        
    def calculate_cost(self):
        self.g = abs(self.position[0] - neo.position[0]) + abs(self.position[1] - neo.position[1])
    def calculate_heuristic(self):
        self.h = abs(self.position[0] - keymaker.position[0]) + abs(self.position[1] - keymaker.position[1])   
    def calculate_estimated(self):
        self.f = self.g + self.h

class Map:
    cell_matrix = []
    dimensions = (8, 8)
    def __init__(self, dimensions:tuple):
        self.dimensions = dimensions
        for x in range(dimensions[0]):
            column = []
            for y in range(dimensions[1]):
                column.append(Cell((x,y)))
            self.cell_matrix.append(column)
    def get_cell(self, x, y):
        if (x < self.dimensions[0] and y < self.dimensions[1]):
            return self.cell_matrix[x][y]
    def calculate_costs(self):
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                self.get_cell(x, y).calculate_cost()
                self.get_cell(x, y).calculate_heuristic()
                self.get_cell(x, y).calculate_estimated()
    def draw(self):
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                self.get_cell(x, y).draw()
        


class Entity:
    coordinates = (0, 0)
    position = (0, 0)
    offset = (0, 0)
    cell = None
    name = ""
    color = "black"
    font_size = 32
    def __init__(self, cell_position):
        self.set_cell(map.get_cell(cell_position[0], cell_position[1]))
    def set_cell(self, cell):
        self.cell = cell
        self.position = cell.position
        self.coordinates = (self.cell.coordinates[0] + self.offset[0],
                            self.cell.coordinates[1] + self.offset[1])
        self.cell.set_content(self)
    def set_position(self, x, y):
        self.set_cell(map.get_cell(x, y))
    def draw(self):
        font = pg.font.Font(None, self.font_size)
        text = font.render(self.name, True, self.color)
        screen.blit(text, ((self.cell.coordinates[0] + self.offset[0], self.cell.coordinates[1] + self.offset[1])))
    
        
    
    pass
class Actor(Entity):
    perception_radius = 1
    percepted_cells = []
    pass

class Neo(Actor):
    def __init__(self, cell_position):
        super().__init__(cell_position)
        self.color = "blue"
        self.name = "neo"
    def percept(self):
        #clear percepted celles
        for i in self.percepted_cells:
            if (i != None):
                i.clear_perceptor()
        self.percepted_cells = []
            
        for x in range(self.position[0] - self.perception_radius,
                       self.position[0] + self.perception_radius + 1):
            for y in range(self.position[1] - self.perception_radius,
                           self.position[1] + self.perception_radius + 1):
                if (x != self.position[0] or y != self.position[1]):
                    self.percepted_cells.append(map.get_cell(x, y)) #set current percieved cells
            
        #set perceptors        
        for i in self.percepted_cells:
            if (i != None):
                i.set_perceptor(self)
            
                    
                
    pass
class Smith(Actor):
    def __init__(self, cell_position):
        super().__init__(cell_position)
        self.color = "red"
        self.name = "smith"
        self.font_size = 26
    def percept(self):
        #clear percepted celles
        for i in self.percepted_cells:
            i.clear_perceptor()
        self.percepted_cells = []
            
        for x in range(self.position[0] - self.perception_radius,
                       self.position[0] + self.perception_radius + 1):
            for y in range(self.position[1] - self.perception_radius,
                           self.position[1] + self.perception_radius + 1):
                if (x != self.position[0] or y != self.position[1]):
                    self.percepted_cells.append(map.get_cell(x, y)) #set current percieved cells
            
        #set perceptors        
        for i in self.percepted_cells:
            i.set_perceptor(self)
    pass
class Sentinel(Actor):
    def __init__(self, cell_position):
        super().__init__(cell_position)
        self.color = "orange"
        self.name = "sentinel"
        self.font_size = 18
    def percept(self):
        #clear percepted celles
        for i in self.percepted_cells:
            i.clear_perceptor()
        self.percepted_cells = []
            
        stencil_cells_positions = []
        stencil_cells_positions.append((self.position[0], self.position[1] + 1))
        stencil_cells_positions.append((self.position[0] - 1, self.position[1]))
        stencil_cells_positions.append((self.position[0], self.position[1]))
        stencil_cells_positions.append((self.position[0] + 1, self.position[1]))
        stencil_cells_positions.append((self.position[0], self.position[1] - 1))
        
        for i in stencil_cells_positions:
            if (i[0] != self.position[0] or i[1] != self.position[1]):
                self.percepted_cells.append(map.get_cell(i[0], i[1])) #set current percieved cells
            
        #set perceptors        
        for i in self.percepted_cells:
            i.set_perceptor(self)
    pass
class Keymaker(Entity):
    def __init__(self, cell_position):
        super().__init__(cell_position)
        self.color = "green"
        self.name = "key maker"
        self.font_size = 14
    pass
class Backdoor_key(Entity):
    pass



def read_initial_inputs():
    neo.perception_radius = (int)(input())
    keymaker_position = input().split(" ")
    keymaker.set_position((int)(keymaker_position[0]), (int)(keymaker_position[1]))

def read_input():
    inpt = input().split(" ")
    return inpt
    
def move(x, y):
    neo.set_position(x, y)
    print(f"m {x} {y}")



map = Map((8, 8))
neo = Neo((3, 3))
neo.perception_radius = 2
smith = Smith((1,1))
sentinel = Sentinel((3,4))
keymaker = Keymaker((5,5))
pg.init()
screen = pg.display.set_mode([512,512])
pg.display.set_caption("Matrix Universe")
running = True
#pg.time.delay(7000)
move(0, 0)
read_initial_inputs()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False        
    screen.fill("black")
    map.calculate_costs()
    map.draw()
    neo.percept()
    neo.draw()
    
    keymaker.draw()
    pg.display.update()
    
    move_input = read_input()
    
    move((int)(move_input[0]), (int)(move_input[1]))
    
    '''
    inpt = read_input()
    
    item_position = ()
    item_type = ""
    if len(inpt) == 3:
        item_position[0] = inpt[0]
        item_position[1] = inpt[1]
        item_type = inpt[2]
    elif len(inpt) == 1:
        pass
    
    move(3,4)
    '''
    pg.display.update()
    '''
    
    
    
    neo.set_position(5,6)
    
    smith.draw()
    smith.percept()
    
    sentinel.draw()
    sentinel.percept()
    
    keymaker.draw()
    
    '''
    
    
    #pg.time.delay(1000)














'''
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


'''