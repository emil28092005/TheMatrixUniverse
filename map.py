import pygame as pg
from tools import *
from entities import *

pg.init()
screen = pg.display.set_mode([512,512])
pg.display.set_caption("Matrix Universe")


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
    cell_Grid = []
    margin = 5
    dimension = Vector2(8,8)
    offset = Vector2(50, 50)
    def __init__(self):
        for x in range(self.dimension.x):
            for y in range(self.dimension.y):
                self.cell_Grid.append(Cell()) #TODO: Finish it
        pass



cell = Cell(coordinates=Vector2(50,50))

running = True

while (running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill('BLACK')
    cell.draw()
    pg.display.update()
