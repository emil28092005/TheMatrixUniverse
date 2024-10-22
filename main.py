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
        pg.draw.rect(screen, "white", self.rect)
        
        if self.perceptor == None:
            pg.draw.rect(screen, "white", self.rect)
        else:
            pg.draw.rect(screen, self.perceptor.color, self.rect)
        
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
                if 0 <= x < map.dimensions[0] and 0 <= y < map.dimensions[1]:
                    if (x != self.position[0] or y != self.position[1]):
                        self.percepted_cells.append(map.get_cell(x, y)) #set current percieved cells
            
        #set perceptors        
        for i in self.percepted_cells:
            if (i != None):
                i.set_perceptor(self)
        map.draw()
        pg.display.update()
        
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
screen = pg.display.set_mode([1124,1124])
pg.display.set_caption("Matrix Universe")
running = True
#pg.time.delay(7000)
move(0, 0)
read_initial_inputs()
pg.time.delay(1500)
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
    pg.time.delay(1500)
    
    move((int)(move_input[0]), (int)(move_input[1]))
    

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

