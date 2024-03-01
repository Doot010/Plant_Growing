import pygame
class Pixels:

    def define(surfaceDec, r, g, b, sizeDec):
        global color, surface, size
        color = (r, g, b)
        surface = surfaceDec
        size = sizeDec

    def pixel(xPos, yPos):
        global color, surface, size
        pygame.draw.rect(surface, color, [xPos, yPos, size, size], 0)

    def getSize():
        global size
        return size


    

    