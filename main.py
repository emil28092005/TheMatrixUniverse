import pygame as pg
from map import *

cell = Cell(coordinates=np.array([50,50]))

running = True

while (running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill('BLACK')
    cell.draw()
    