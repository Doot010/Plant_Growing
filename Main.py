import time, pygame, math, sys, os
from Plant import Plant
from Pixels import Pixels

pygame.init()
surface = pygame.display.set_mode((800, 600))

Pixels.define(surface, 255, 255, 255, 10)

Pixels.pixel(10, 10)

#game loop
while True:
    pygame.display.update()
