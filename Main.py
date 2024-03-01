import time, pygame, math, sys, os
from Plant import Plant
from Pixels import Pixels

os.system("cls")
pygame.init()
surface = pygame.display.set_mode((800, 600))

Pixels.define(surface, 255, 255, 255, 5)

#first input must be greater than last
Plant.growingPlant(200, 400, 600)

#game loop
run = True
while run:
   key = pygame.key.get_pressed() 
   if key [pygame.K_SPACE]:
      pygame.quit()
      run = False
   
