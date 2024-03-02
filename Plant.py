from Pixels import Pixels
import random
import pygame

class Plant:

    #vars
    height = 0
    pos = 0

    #kill window function
    def kill():
        key = pygame.key.get_pressed() 
        if key [pygame.K_SPACE]:
            pygame.quit()

    def wideGrowth(use):
        

        global height, pos
        pixSize = Pixels.getSize()
        LoR = use

        wide = random.randint(3, 9)
        counter = 0

        if (LoR%2) == 1:
            print("left")
            while counter <= wide:

                counter += 1 #counting how many times it moves to the side
                posChange = random.randint(2, pixSize) #how far to the side it should move

                Pixels.pixel(pos, height)
                height -= 2
                pos -= posChange
                pygame.display.update()
                pygame.time.wait(100)
        else:
            print("right")
            while counter <= wide:

                counter += 1 #counting how many times it moves to the side
                posChange = random.randint(2, pixSize) #how far to the side it should move

                Pixels.pixel(pos, height)
                height -= 2
                pos += posChange
                pygame.display.update()
                pygame.time.wait(100)
        
    def wideGrowthCurve(use):
        

        global height, pos
        LoR = use
        pixSize = Pixels.getSize()
        wide = random.randint(2, 3)
        counter = 0

        if (LoR%2) == 1:
            print("left")
            while counter <= wide:

                counter += 1 #counting how many times it moves to the side
                posChange = random.randint(2, pixSize) #how far to the side it should move

                Pixels.pixel(pos, height)
                height -= (pixSize * (4/5))
                pos -= posChange
                pygame.display.update()
                pygame.time.wait(100)
        else:
            print("right")
            while counter <= wide:

                counter += 1 #counting how many times it moves to the side
                posChange = random.randint(2, pixSize) #how far to the side it should move

                Pixels.pixel(pos, height)
                height -= (pixSize * (4/5))
                pos += posChange
                pygame.display.update()
                pygame.time.wait(100)

    def verticalGrowth():
        global height, pos
        amount = random.randint(5, 10)
        x = 0
        while x <= amount:
            x += 1
            Pixels.pixel(pos, height)
            height -= Pixels.getSize()
            pos += random.randint(-3, 3)
            pygame.display.update()
            pygame.time.wait(100)

    def curve():
        global height, pos

        LoR = random.randint(0,1)

        Plant.wideGrowthCurve(LoR)

        #making curve smooth
        amount = random.randint(1, 2)
        x = 0
        while x <= amount:
            x += 1
            Pixels.pixel(pos, height)
            if (LoR%2) == 1:
                height -= Pixels.getSize()
                pos -= random.randint(1, 2)
                pygame.display.update()
                pygame.time.wait(100)
            else:
                height -= Pixels.getSize()
                pos += random.randint(0, 2)
                pygame.display.update()
                pygame.time.wait(100)

        LoR += 1
        Plant.wideGrowthCurve(LoR)
        

    def growingPlant(maxHeight, startPos, strtHeight, curveChance):

        global height, pos
        
        #vars
        repeat = True
        use = 0
        pos = startPos
        height = strtHeight

        while height >= maxHeight:
            Plant.kill()
            action = random.randint(0, 10)
            if action < curveChance:
                print("z")
                Plant.curve()
                #use += 1
                #repeat = False
            else:
                print("x")
                Plant.verticalGrowth()
                #repeat = True

    