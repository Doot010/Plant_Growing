from Pixels import Pixels
import random, math, pygame

class Plant:

    #vars


    #kill window function
    def kill():
        key = pygame.key.get_pressed() 
        if key [pygame.K_SPACE]:
            pygame.quit()

    def branchingStem(LoR):
        

        global height, pos
        branchHeight = height
        branchPos = pos
        pixSize = Pixels.getSize()
        #LoR = random.randint(0, 1)

        wide = random.randint(6, 20)
        counter = 0

        if (LoR%2) == 1:
            print("left")
            
        else:
            print("right")
            pixSize = pixSize*-1

        #stuff for changing height
        UorD = random.randrange(-1, 2, 2)
        amp = random.randint(1, 2)
        
        while counter <= wide:

            heightChange = UorD * amp * (math.sqrt(counter)) # final result for heightChange


            Pixels.pixel(branchPos, branchHeight)
            branchHeight -= heightChange
            branchPos -= pixSize
            pygame.display.update()
            pygame.time.wait(100)

            counter += 1 #counting how many times it moves to the side
        
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
        amount = random.randint(3, 7)
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

        pixSize = Pixels.getSize()
        LoR = random.randint(0,1)

        Plant.wideGrowthCurve(LoR)

        #making curve smooth
        amount = random.randrange(int(((1/5)*pixSize)), int((((1/4)*pixSize)+1)))
        x = 0
        while x <= amount:
            Pixels.pixel(pos, height)

            if x == amount:
                amount = amount*(-1)
            
            if (LoR%2) == 1:
                height -= pixSize
                pos -= amount
                pygame.display.update()
                pygame.time.wait(100)
            else:
                height -= pixSize
                pos += amount
                pygame.display.update()
                pygame.time.wait(100)
            x += 1

        LoR += 1
        Plant.wideGrowthCurve(LoR)


    def growingPlant(maxHeight, startPos, strtHeight, curveChance, branchChance):

        global height, pos
        
        #vars
        repeat = True
        pos = startPos
        height = strtHeight
        LoR = random.randint(0, 1)

        while height >= maxHeight:
            Plant.kill()
            action = random.randint(0, 100)
            if action < curveChance:
                print("curve")
                Plant.curve()
                repeat = True

            elif action < (curveChance + branchChance) and repeat:
                print("branch")
                Plant.branchingStem(LoR)
                repeat = False
                LoR += 1

            else:
                print('vert')
                Plant.verticalGrowth()
                repeat = True

    