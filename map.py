import numpy as np
import pygame as pg

screen = pg.display.set_mode([512,512])
pg.display.set_caption("Matrix Universe")
pg.init()
class Cell:
    coordinates = np.array([0,0])
    position = np.array([0,0])
    size = 50
    piece = pg.draw.rect(screen, (255,255,255), (0, 0, size, size))
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.position = coordinates // self.size
    def draw(self):
        screen.blit(screen, self.coordinates ,self.piece)
        
class Map:
    cellGrid = None
    def __init__(self):
        pass