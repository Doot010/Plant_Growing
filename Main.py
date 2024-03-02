import time, pygame, math, sys, os
from Plant import Plant
from Pixels import Pixels

os.system("cls")
pygame.init()
surface = pygame.display.set_mode((800, 600))

Pixels.define(surface, 255, 255, 255, 8)

#Inputs: maxHeight, strtPos, strtHeight, curveChance
Plant.growingPlant(200, 400, 600, 7)

#game loop
run = True
while run:
   key = pygame.key.get_pressed() 
   if key [pygame.K_SPACE]:
      pygame.quit()
      run = False
   
