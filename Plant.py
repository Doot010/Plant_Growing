from Pixels import Pixels

class Plant:

    #vars
    global food

    def growingPlantRules(strtfood):
        global food
        food = strtfood

    def getFood():
        global food
        return food