##import pdb
##pdb.set_trace()

from psStories import *

class Game (object):
    def __init__(self, left, middle, right, story, alive):
        object.__init__(self)
        # Left
        self.setLeft(left)
        # Middle
        self.setMiddle(middle)
        # Right
        self.setRight(right)
        # Story
        self.setStory(story)
        # Alive Boolean
        self.setAlive(alive)

    # setter, getter, and property of left
    def setLeft(self, left):
        self.__left = left
    def getLeft(self):
        return self.__left
    left = property(fget = getLeft, fset = setLeft)

    # setter, getter, and property of middle
    def setMiddle(self, middle):
        self.__middle = middle
    def getMiddle(self):
        return self.__middle
    middle = property(fget = getMiddle, fset = setMiddle)

    # setter, getter, and property of right
    def setRight(self, right):
        self.__right = right
    def getRight(self):
        return self.__right
    right = property(fget = getRight, fset = setRight)

    # setter, getter, and property of story
    def setStory(self, story):
        self.__story = story
    def getStory(self):
        return self.__story
    story = property(fget = getStory, fset = setStory)

    # setter, getter, and property of alive
    def setAlive(self, alive):
        self.__alive = alive
    def getAlive(self):
        return self.__alive
    alive = property(fget = getAlive, fset = setAlive)
  
    def Play(self):
        # this just needs to check if alive, get choice, then return choice
        global currentNode
        if self.__alive == True:
           
            choiceCycle = True
            print()
            print(self.getStory())
            choice = input(">> ")
            while(choiceCycle):
                return choice
            
        # if user makes a game-ending choice
        else:
            print()
            print(self.getStory())
            choice = 7
            return choice

# Global variables
gameNode = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
towel = False
inventory = ["pajama shirt", "pajama pants"]
currentNode = 0
goodChoices = ["1", "2", "3", 7]

def main():
    keepGoing = True
    A = Game(1,2,3, storyA, True)
    R1 = Game(None, None, None, storyR1, False)
    ## in R1, set alive = False
    R2 = Game(4,5,6, storyR2, True)
    R3 = Game(4,5,6, storyR3, True)
    ## in R3, Towel is added to Inventory
    O1 = Game(7,8, None, storyO1, True)
    O2 = Game(4, 9, None, storyO2, True)
    O3 = Game(10, 16, 17, storyO3, True)
    Y1 = Game(11, 12, None, storyY1, True)
    Y2 = Game(11, 12, None, storyY2, True)
    Y3 = Game(13, 14, 15, storyY3, True)
    # Y3 is special because of inventory shenanigans
    Y4 = Game(4, 5, None, storyY4, True)
    G1 = Game(18, 19, None, storyG1, True)
    G2 = Game(18, 19, None, storyG2, True)
    G5Y = Game(7, 8, None, storyG5Y, True)
    G5N = Game(7, 8, None, storyG5N, True)
    G6 = Game(7, 8, None, storyG6, True)
    G7A = Game(7, 8, None, storyG7A, True)
    G7B = Game(7, 8, None, storyG7B, True)
    B1 = Game(None, None, None, storyB1, False)
    # in B1, set alive = False
    B2 = Game(20, 21, None, storyB2, True)
    I1 = Game(None, None, None, storyI1, False)
    # in I1, set alive = False
    I2 = Game(23, 22, 24, storyI2, True)
    P2 = Game(25, 26, 27, storyP2, True)
    # P2 is special
    P1A = Game(None, None, None, storyP1A, False)
    P1B = Game(None, None, None, storyP1B, False)
    # in P1A and P1B, set alive = False
    V1 = Game(None, None, None, storyV1, False)
    V2A = Game(None, None, None, storyV2A, False)
    V2B = Game(None, None, None, storyV2B, False)
    # in V2A and V2B, set alive = False

    gameNode[0] = A
    gameNode[1] = R1
    gameNode[2] = R2
    gameNode[3] = R3
    gameNode[4] = O1
    gameNode[5] = O2
    gameNode[6] = O3
    gameNode[7] = Y1
    gameNode[8] = Y2
    gameNode[9] = Y3
    gameNode[10] = Y4
    gameNode[11] = G1
    gameNode[12] = G2
    gameNode[13] = G5Y
    gameNode[14] = G5N
    gameNode[15] = G6
    gameNode[16] = G7A
    gameNode[17] = G7B
    gameNode[18] = B1
    gameNode[19] = B2
    gameNode[20] = I1
    gameNode[21] = I2
    gameNode[22] = P2
    gameNode[23] = P1A
    gameNode[24] = P1B
    gameNode[25] = V1
    gameNode[26] = V2A
    gameNode[27] = V2B

    currentNode = gameNode[0]
    global towel
    
    # title
    print("    ____  __     __         _                _____         _                       ")        
    print("   / __ \/ /__  / /_  ___  (_)___ _____     / ___/____    (_)___  __  ___________  ")
    print("  / /_/ / / _ \/ __ \/ _ \/ / __ `/ __ \    \__ \/ __ \  / / __ \/ / / / ___/ __ \ ")
    print(" / ____/ /  __/ /_/ /  __/ / /_/ / / / /   ___/ / /_/ / / / /_/ / /_/ / /  / / / / ")
    print("/_/   /_/\___/_.___/\___/_/\__,_/_/ /_/   /____/\____/_/ /\____/\__,_/_/  /_/ /_/  ")
    print("                                                    /___/                          ")
    print()

    while(keepGoing):
        choice = currentNode.Play()

        choiceCycle = True
        while(choiceCycle):

            # this section takes the choice from the user and uses it to assign the next node.
            # there are some special nodes

            # special for R3 because of the towel
            if currentNode == gameNode[3]:
                if towel == False:
                    # add towel to inventory
                    inventory.append("towel")
                #flip the towel switch
                towel = True
                if choice == "1":
                    currentNode = gameNode[currentNode.getLeft()]
                    choiceCycle = False
                    break
                elif choice == "2":
                    currentNode = gameNode[currentNode.getMiddle()]
                    choiceCycle = False
                    break
                elif choice == "3":
                    currentNode = gameNode[currentNode.getRight()]
                    choiceCycle = False
                    break
                if not choice in goodChoices:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")

            #special for O2 (because of the inventory)
            elif currentNode == gameNode[5]:
                if choice == "1":
                    currentNode = gameNode[currentNode.getLeft()]
                    choiceCycle = False
                    break
                elif choice == "2":
                    currentNode = gameNode[currentNode.getMiddle()]
                    choiceCycle = False
                    print(inventory)
                    break
                if not choice in goodChoices:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")

            # special for O3 dependent on towel
            elif currentNode == gameNode[6]:
                if choice == "1":
                        currentNode = gameNode[currentNode.getLeft()]
                        choiceCycle = False
                        break
                elif choice == "2":
                    if towel == True:
                        currentNode = gameNode[currentNode.getMiddle()]
                        choiceCycle = False
                        break
                    else:
                        currentNode = gameNode[currentNode.getRight()]
                        choiceCycle = False
                        break
                        
                if not choice in goodChoices:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")

            # special for Y3 and towel
            elif currentNode == gameNode[9] and towel == True:
                    if choice == "1":
                        print()
                        print("Would you like to use your shirt or your towel to wrap your hands in? \n\n1)shirt \n2)towel")
                        choice = input(">> ")
                        if choice == "1":
                            currentNode = gameNode[currentNode.getLeft()]
                            choiceCycle = False
                            break
                        elif choice == "2":
                            currentNode = gameNode[currentNode.getRight()]
                            choiceCycle = False
                            break             
                        if not choice in goodChoices:
                            print("Choice unclear. Please try again.")
                            choice = input(">> ")

                    if not choice in goodChoices:
                        print("Choice unclear. Please try again.")
                        choice = input(">> ")

            # special for Y3 and no towel       
            elif currentNode == gameNode[9] and towel == False:
                if choice == "1":
                    print()
                    print("Would you like to use your shirt to wrap your hands in? \n\n1)yes \n2)no")
                    choice = input(">> ")
                    if choice == "1":
                        currentNode = gameNode[currentNode.getLeft()]
                        choiceCycle = False
                        break
                    elif choice == "2":
                        currentNode = gameNode[currentNode.getMiddle()]
                        choiceCycle = False
                        break
                    if not choice in goodChoices:
                        print("Choice unclear. Please try again.")
                        choice = input(">> ")

                if not choice in goodChoices:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")
                    
            # special for I2 dependent on towel
            elif currentNode == gameNode[22]:
                if choice == "1":
                    if towel == True:
                        currentNode = gameNode[currentNode.getLeft()]
                        choiceCycle = False
                        break
                    else:
                        currentNode = gameNode[currentNode.getRight()]
                        choiceCycle = False
                        break
                elif choice == "2":
                    currentNode = gameNode[currentNode.getMiddle()]
                    choiceCycle = False
                    break

                if not choice in goodChoices:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")

            # regular run
            else:
                if choice == "1":
                    currentNode = gameNode[currentNode.getLeft()]
                    choiceCycle = False
                    break
                elif choice == "2":
                    currentNode = gameNode[currentNode.getMiddle()]
                    choiceCycle = False
                    break
                elif choice == "3":
                    currentNode = gameNode[currentNode.getRight()]
                    choiceCycle = False
                    break
                elif choice == 7:
                    keepGoing = False

                if not choice in goodChoices:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")

       
if __name__ == "__main__":
    main()

