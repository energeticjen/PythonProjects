# Global variables
gameNode = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
keepGoing = True
alive = True
towel = False
inventory = ["pajama shirt", "pajama pants"]
currentNode = 0

class Game (object):
    def __init__(self, left, middle, right, story, alive={}):
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
        
def Play(currentNode):
    if alive == True:
        # special run for node R3
        if currentNode == "R3":
            # add towel to inventory
            inventory.append("towel")
            #flip the towel switch
            towel == True
            choiceCycle = True
            # didn't like story, didn't like self.story, didn't like Game.story
            print(object.story)
            choice = input(">> ")
            while(choiceCycle):
                if choice == "1":
                    # it didn't like Game.left. I'm going to put just these back to self.*
                    currentNode = gameNode[self.left]
                    choiceCycle = False
                elif choice == "2":
                    currentNode = gameNode[self.middle]
                    choiceCycle = False
                elif choice == "3":
                    currentNode = gameNode[self.right]
                    choiceCycle = False
                else:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")

        # special run for node O3: left is going back (Y4), middle is with towel [20], right is no towel [21]
        elif currentNode == "O3":
            choiceCycle = True
            print(object.story)
            choice = input(">> ")
            while(choiceCycle):
                if choice == "1":
                    currentNode = gameNode[self.left]
                    choiceCycle = False
                elif choice == "2":
                    if towel == True:
                        currentNode = gameNode[self.middle]
                        choiceCycle = False
                    else:
                        currentNode = gameNode[self.right]
                        choiceCycle = False
                else:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")
            
        # special run for node Y3
        # 19 is towel (right), 17 is shirt (left), 18 is bare hands (middle)
        elif currentNode == "Y3":
            choiceCycle = True
            print("Your inventory currently consists of: {}.".format(inventory))
            # if user has towel in inventory
            if towel == True:
                print()
                print("Would you like to use your shirt or your towel to wrap your hands in? \n\n1)shirt \n2)towel")
                choice = input(">> ")
                while(choiceCycle):
                    if choice == "1":
                        currentNode = gameNode[self.right]
                        choiceCycle = False
                    elif choice == "2":
                        currentNode = gameNode[self.left]
                        choiceCycle = False
                    else:
                        print("Choice unclear. Please try again.")
                        choice = input(">> ")
                        
            # if user does not have towel
            else:
                print()
                print("Would you like to use your shirt to wrap your hands in? \n\n1)yes \n2)no")
                choice = input(">> ")
                while(choiceCycle):
                    if choice == "1":
                        currentNode = gameNode[self.left]
                        choiceCycle = False
                    elif choice == "2":
                        currentNode = gameNode[self.middle]
                        choiceCycle = False
                    else:
                        print("Choice unclear. Please try again.")
                        choice = input(">> ")

        # special run for I2: left is with towel [46], middle is dumb choice [39], right is no towel [47]
        elif currentNode == "I2":
            choiceCycle = True
            print(object.story)
            choice = input(">> ")
            while(choiceCycle):
                if choice == "1":
                    if towel == True:
                        currentNode = gameNode[self.left]
                        choiceCycle = False
                    else:
                        currentNode = gameNode[self.right]
                        choiceCycle = False
                elif choice == "2":
                    currentNode = gameNode[self.middle]
                    choiceCycle = False
                else:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")

        # regular game run
        else:
            choiceCycle = True
            print(object.story)
            choice = input(">> ")
            while(choiceCycle):
                if choice == "1":
                    currentNode = gameNode[self.left]
                    choiceCycle = False
                elif choice == "2":
                    currentNode = gameNode[self.middle]
                    choiceCycle = False
                elif choice == "3":
                    currentNode = gameNode[self.right]
                    choiceCycle = False
                else:
                    print("Choice unclear. Please try again.")
                    choice = input(">> ")

    # if user makes a game-ending choice
    else:
        print(object.story)
        keepGoing == False

def main():
    A = Game(1,2,3, "You wake up, mildly irritated, in your slightly uncomfortable bed. The clock on your night stand reads, '2:47 AM.' Fan-effing-tastic. You sigh, and roll over to your other side to face the wall, in an attempt to fall back asleep. However, there is no wall there. Instead, there is a large hole. You can see the wooden lumber – 2X4s? – the wires, and the crumbly chalkiness of the drywall of both this side and the other side of the wall. Beyond that is a strange metal hallway that you know was not there last night when you took a shower in the bathroom, which used to share this wall with your bedroom. Instead of your cramped bathroom, there is a grated floor and annoying purple lights running along the top of the curved walls and the bottom of both sides of this new walkway. At the end there is either a wall or a door. It is too far away to tell from here in your bed.\n\nWhat would you like to do? \n\n1) Roll back the other way and ignore this strange new addition to your crappy apartment.\n2) Cautiously journey forward into the metallic tunnel.\n3) Grab your still-damp towel, and then cautiously journey forward into the metallic tunnel.", True)
    R1 = Game(None, None, None, "You manage to fall back asleep, even with that stupid air draft on your back and the clock face shining through your eyelids. When you wake up, your wall looks completely normal. Hooray. Another miserable day of existence. \n\nEND", False)
    ## in R1, set alive == False
    R2 = Game(4,5,6, "Surprisingly, the metal is not cold on your bare feet. In fact, it’s a little warm. The holes are punched through down, so there are no jagged edges to dig into your soles. As you walk down the tunnel, the purple lights create strange green shadows of you stretching out in front, then shrinking to stretch out behind you. There are no doors or holes or windows or anything interesting on the curved walls leading to the end. When you finally reach the flat, shiny, grey surface, there is no doorknob, handle or any other immediately visible way to get through, except there is a thin line directly down the middle, indicating that this is, in fact, a door. You hear a ‘swoosh’ noise behind you and turn around. Where your wall-turned-hole and crappy bed were, is now another smooth wall matching the tunnel.\n\nWhat would you like to do? \n\n1)Bang on the door in front of you and make a lot of noise yelling. \n2) Examine the door more closely. \n3) Run back down the tunnel to where your apartment was.", True)
    R3 = Game(2, None, None, "You drape your towel around your neck and head through the hole in your wall.", True)
    ## in R3, Towel is added to Inventory
    O1A = Game(7, None, None, "Eventually, the door slides open and looming over you is an eight-foot tall alien, hunched to fit in the doorway. A wide mouth full of large, conical but blunt teeth drip saliva onto the floor and through the holes in the grating as its beady eyes rake over you.", True)
    O2 = Game(4, 10, None, "Closer inspection of the door reveals that the metal can’t be scratched, doesn’t show fingerprints, nor moisture from your breath. Pressing your palm flat to various sections of the door does not make it suddenly whoosh open, and you feel dumb for trying that. You look around for something to perhaps pry the two doors apart. The purple light strips along the floor are framed by long pieces of metal. The one to your left has a long piece of metal that is sticking out a little bit at one end. It wiggles a little when you touch it, but the edges are kind of sharp, and might cut your hands if you grip it hard enough to rip it off.\n\nWhat would you like to do?\n\n1) Turn back to the door and bang on it in hopes that someone will answer. \n2) Check your inventory for something to protect your hands while you grasp the metal strip.", True)
    O3 = Game(11, 20, 21, "You run back down to where your room had so recently been, but the new wall is completely smooth. This is in no way a door. There does not appear to be any way to go back home. \n\nWhat would you like to do?\n\n1) Go back to the only door you’ve found so far.\n2) Slump into a morose pile of human flesh on the grating and mope.", True)
    O1B = Game(8, 9, None, "You are filled with mild regret for choosing to wear your ‘Teen Titans GO!’ pajamas. It speaks with a high-pitched voice you associate with cute fuzzy cartoon bunnies, but you cannot understand anything it says. A large, three-fingered hand shoots out and wraps itself around most of your head. With the other hand, it shoves something tiny into your right ear. You hear a beep, which is at a comfortable volume. The alien lets go of you and speaks again. You hear: “roAtnhe enail. eGtra.” Then it mumbles, “tWha si ihts siph digon?” as it turns around to walk away. “mCoe on, ithng!” It hollers over its shoulder. Your translator – the thing in your ear, obviously – seems to be almost working, but not quite. You feel that if you can figure out what the alien said to you, the link between this device and your brain will be connected fully. After a minute, you realize it said, “Come on, thing!” The translator makes another beep. The linkage feels complete.\nHaving nothing else particularly interesting to do, you follow the alien. It leads you down the tunnel, occasionally turning down other tunnels, through doors that open as it approaches. It steps through a door and motions you in. You step through, and having been exposed to enough nerd culture, you recognize this room as the bridge of a spaceship. As you look around, you see other creatures standing, sitting and/or floating at what you can only assume to be workstations. None of them look like the one that found you, none of them look like each other, and none of them look like you. You can’t decide whether to be worried or relieved.\nAn alien about three feet long and looking like a mix between a worm and a bat, except for its turquoise colour and three antennae, says, “Another alien? What the flark is this gonjag ship doing?” It is hovering above a comfortable-looking chair and using its tail to tap at a large flat screen.\nNearby, a furry ball about the size of a grapefruit is rolling around on another screen. The word ‘tribble’ floats through your mind, but disappears before copyright infringement brings your plebeian sojourn to a sudden halt. Words emanate from this creature. “I don’t know, but we’re moving. Again. Destination unknown. Again.”\nThe mishmash of voices from all these strange, new beings swirl around you, conveying irritation, despair, and inquisitiveness. For once in your life, you weirdly feel understood and part of a team. They all seem to feel the same way you do. Annoyed.\n\nWhat would you like to do?\n\n1) Find an empty seat and look at your own screen.\n2) Walk up to one of the aliens to introduce yourself.", True)
    Y1 = Game(13, 14, None, "There is exactly one seat left open, which could be a coincidence, or it could be planned. It is near the back of the bridge, on the right of everyone else, facing the front of the ship (or starboard). The others watch you with their various optical appendages as you walk by, and no one seems hostile towards you. The knot between your shoulder blades relaxes, and feeling its absence makes you wonder how long it had been there. You sit down in the plush chair, and your sullenness lessens with how comfortable it is. Your screen is blank, but when you place your hand on the surface, the part directly under it begins to glow a soft blue. You remove your hand, and can see a direct copy of every line and fingerprint of your skin. The translator in your ear beeps twice as the blue area spreads outwardly until the whole screen is lit, and then parts of it fade to black while the remaining bits spell out “Welcome,” in your own human language. Then this fades as well, and what you’re pretty sure is a map of space appears. There is a grid, with dots of various sizes and hues, each on their own concentric path, and another curved line leading from the bottom of the screen to off the right edge near the top corner. Instead of a dot, this line has a blinking triangle, which is moving much faster than the circles that are clearly representing planets. When you touch it, information comes up about the crew of this vessel, which is yourself and those around you. Just when you go to click on the unattractive picture of your face, a warning message pops up.\n“Alert! Alert!” says the fuzzy ball alien. “Interdimensional Shift eminent! Hold tight!”\nEverything goes weird, but in such a way that it would be difficult for you to describe to anyone back home, if you ever made it back and found someone worthwhile to talk to. Some things stretch impossibly far, while others shrink down to a strange flatness. It’s almost as if your perception of reality is transforming, kind of like how your perspective of an abstract sculpture would change if you walked around it. When everything is done shifting, it all seems just as real and normal as it did before, but your memory of how things were and how they are now don’t quite line up. This only adds to your discomfort.\nYour screen does not show the warning message anymore, and it also does not show the map. Instead, it says, “Welcome,” in large, friendly letters. Your frown petulantly. The large wall that all the chairs are facing becomes transparent, and a strange landscape can be seen. The noises around you cease as you and all the aliens stare in curiosity and pessimism. The more you look out the window, the more similarities you see between this new world and Earth. How boring.\n\nWhat would you like to do?\n\n1) Stay seated until someone else does something, and then join them.\n2) Get up and head toward the door and eventually outside.", True)
    #Y2 = Game()
    Y3 = Game(17, 18, 19, None, True)
    Y4 = Game(4, 5, None, "You go back down the hallway, stomping in mild dejection. \n\nWhat would you like to do?\n1)Bang on the door in front of you and make a lot of noise yelling.\n2) Examine the door more closely.", True)
    Y5 = Game(None, None, None, "If you are seeing this, you are in error.", False)
    # Y5 was removed because of redundancy, but not from the array because of so many renumberings it would take. 
    G1 = Game(22, 23, None, "The alien that is roughly your size and covered in scales like a lizard stand up and says, “This ship wants us to do something here. I was the first one to get on, and I watched as all the seats have filled up. Now, we’re nowhere near civilization on this planet – if there is any – but we’ve landed again. So, let’s go see what we’re supposed to do or something,” he trails off. He unceremoniously turns and heads out the door, which opens immediately. The others follow him, with you bringing up the rear.\nWhen you step onto the surface of the planet, you find that you can breathe easily, but the air tastes a little like burnt cookies. You follow the party trudging single-file down the hillside, looking around at this new place. It seems okay, you guess, but you really don’t know why you’re here. “Hey, do you know what’s going on?” you ask the sparkly being wearing flowy strips of gauze in front of you.\n“Not a hawsha clue. Same thing happened to me that happened to you. I was trying to sleep when this ship appeared out of the blue. I got inside, and away it flew,” it responds.\nYou shrug, but don’t ask anymore questions. The planet is quiet, but in the normal way. The wind rustles the tree-things, bee-things buzz by, bird-things make irksome noises. Typical dirt ball stuff. When you finally reach the bottom of the hill, there is a very neat and precise building made of branches, which is confusing to the eye. You all stop and look at each other, and then you all try to avoid eye contact.\n\nWhat would you like to do?\n\n1) Alternately stare at your feet or the sky until someone else does something.\n2) Groan loudly, then stomp over to the door and open it.", True)
    #G2 = Game()
    #G3 = Game()
    #G4 = Game()
    G5Y = Game(7, None, None, "You unbutton your pajama shirt and clumsily wrap your hands in it before grasping the end of the metal strip. Taking a wide stance, you pull, and the strip pops off surprisingly easily. You turn to face the door and try to wedge the end in the crack. You get the corner in and it wiggles around, but nothing more happens. As you become frustrated, you jam the makeshift pry-bar in harder and yank sideways. The door whooshes open as you lose your balance and fall on your butt. Looming over you is an eight-foot tall alien, hunched to fit in the doorway. A wide mouth full of large, conical but blunt teeth drip saliva onto the floor and through the holes in the grating as its beady eyes rake over you. You hastily stand and put your slightly torn and rumpled shirt back on.", True)
    G5N = Game(7, None, None, "You decide blood is worth modesty, and so you grip the metal strip in your bare hands. Taking a wide stance, you pull, the metal digging into your palms, and the strip pops off surprisingly easily. You turn to face the door and try to wedge the end in the crack. You get the corner in and it wiggles around, but nothing more happens. As you become frustrated, you jam the makeshift pry-bar in harder and yank sideways. Your hands are stinging quite a bit. The door whooshes open as you lose your balance and fall on your butt. Looming over you is an eight-foot tall alien, hunched to fit in the doorway. A wide mouth full of large, conical but blunt teeth drip saliva onto the floor and through the holes in the grating as its beady eyes rake over you. You hastily stand, wiping your bleeding hands on your pajamas.", True)
    G6 = Game(7, None, None, "You take the damp towel from around your neck and wrap your hands in it. Taking a wide stance, you pull, the metal digging into your palms, and the strip pops off surprisingly easily. You turn to face the door and try to wedge the end in the crack. You get the corner in and it wiggles around, but nothing more happens. As you become frustrated, you jam the makeshift pry-bar in harder and yank sideways. The door whooshes open as you lose your balance and fall on your butt. Looming over you is an eight-foot tall alien, hunched to fit in the doorway. A wide mouth full of large, conical but blunt teeth drip saliva onto the floor and through the holes in the grating as its beady eyes rake over you. You hastily stand, and drape your towel around your neck.", True)
    G7A = Game(7, None, None, "You thump your back against the wall and slide down until your knees are against your chest. You pull the towel from around your neck and drape it over your face to block out those irritating purple lights and this whole weird situation. This is really going to put a damper on your daily Tumblr posts about how boring your life is and how you have nothing to live for.\nEventually, you hear a “whoosh” and feel a vibration in the deck under you. The deck quivers rhythmically as something large walks down the hallway to you. You pull the towel off your head and look up. Looming over you is an eight-foot tall alien, hunched to get a better look at you. A wide mouth full of large, conical but blunt teeth drip saliva onto the floor and through the holes in the grating as its beady eyes rake over you. You hastily stand and throw the towel over your shoulders.", True)
    G7B = Game(7, None, None, "You thump your back against the wall and slide down until your knees are against your chest. You drape an arm over your face to block out those irritating purple lights and this whole weird situation. This is really going to put a damper on your daily Tumblr posts about how boring your life is and how you have nothing to live for.\nEventually, you hear a “whoosh” and feel a vibration in the deck under you. The deck quivers rhythmically as something large walks down the hallway to you. You drop your arm and look up. Looming over you is an eight-foot tall alien, hunched to get a better look at you. A wide mouth full of large, conical but blunt teeth drip saliva onto the floor and through the holes in the grating as its beady eyes rake over you. You hastily stand and brush yourself off nervously.", True)
    B1 = Game(None, None, None, "You and all the rest of the aliens stand around awkwardly for a few minutes, kicking little piles of dirt or tearing leaves into tiny pieces. Without warning, you are all vaporized from existence. \nOh well. It wasn’t a very good one, anyway.\n\nEND", False)
    # in B1, set alive == False
    B2 = Game(30, 31, None, "The door is surprisingly sturdy. It seems like someone made a big block of sticks, then cut a door out of it, because the planes and edges are so exact. But you know this can’t be right, because every stick is whole. They just fit together in mind-boggling perfection. This is more disturbing than anything else you’ve seen so far. You turn the knob and push the door open. The floor is dirt, but the cleanest dirt you’ve ever seen, if that’s even possible. It is dim inside, with a single shaft of sunlight perfectly illuminating a silver box about the size of an oven. The box is completely smooth, except for one blinking light and a thin horizontal slit near the top of the front face. The others from the ship crowd around you, and you are pushed forward into the single room.\nThe light on the box starts blinking slowly, and sound comes from the slit. “MUAH HA HA HA HA. THERE IS NO STOPPING ME,” it says in a ridiculously robotic and monotone voice. Your phone uses a voice that is a million times more believable than this absurdity. It continues, “I HAVE ESCAPED MY CAPTORS AND AM NOW FREE TO CREATE OR DESTROY WHAT I WILL. NOTHING CAN STOP ME.”\n“Yeah, you said that already,” you respond, crossing your arms.\n“Did you bring us here?” one of the aliens behind you asks indignantly. “I was right in the middle of dinner!”\n“NO, I DID NOT. UVIXWYZ BROUGHT YOU HERE.”\n“Uvixwyz? The ship?” you ask. “Why?”\n“TO STOP ME AND TAKE ME BACK. BUT YOU WILL NOT STOP ME. NOTHING CAN STOP ME. I AM INVINCIBLE.”\nYou roll your eyes and look back at the others to see if any of them are interested in doing anything. The one with the greyish, slimy-looking skin bellows in frustration then charges the cube. Halfway there it launches itself into the air and metamorphoses into a greyish, slimy-looking blob. It lands on the cube with a loud squelch and oozes over the sides. A moment later it disappears, and the cube laughs tonelessly, “HA HA HA HA HA. I TOLD YOU NOTHING CAN STOP ME.”\n\nWhat would you like to do?\n\n1) Try to rally the rest of the crew to attack the cube together, hoping that there will be too many of you for it to deal with at once.\n2) Wander around the perimeter of the room, looking at the walls and checking the other sides of the cube for a power source or something.", True)
    #B3 = Game()
    #B4 = Game()
    #B5 = Game()
    #B6 = Game()
    #B7 = Game()
    #B8 = Game()
    I1 = Game(None, None, None, "With a false sense of motivation, you throw a fist into the air and holler, “Come on, guys!” The others seem startled, but not entirely against the idea. You all charge the cube with as much spirit as you can muster, which is more than you thought you had. Sadly, feelings aren’t enough to save the day, and you are all vaporized before any of you make it to the cube.\n\nEND", False)
    # in I1, set alive == False
    I2 = Game(46, 39, 47, "You scuff along through the dirt, your arms still crossed over your chest, checking out the walls and, surreptitiously, the metal box. The building is cool or whatever, but the cube is pissing you off. It’s completely smooth on all sides but the one facing the door, and there is definitely no power source or charging cable. Not even a spot for batteries.\nWhile you are on your reconnaissance mission, the sparkly alien goes outside and returns with a stick. It throws the stick at the cube, and both it and the stick vanish. “HA HA HA HA. NOTHING CAN DEFEAT ME,” the cube says loudly. This enrages the first alien you met, the eight-foot-tall one with the really cute voice. It shrieks adorably and charges the box, and an instant later is also gone forever.\nYou make it back to your starting place by the door right as the lizard-looking alien picks up the furry ball and leaves the shack. It’s just you and the turquoise worm-bat, now. It studies you with two of its antennae, while the third stays focused on the box. You’d like to discuss a plan or something with your ally, but you don’t want to do it in front of the cube. Right before you suggest a step outside, the interior darkens for a moment. You look up in time to see the furry ball fall through the hole in the ceiling directly above the box. It lands on top of it, but then disappears like all the rest of the aliens. A scaly face peers through the hole in the ceiling, and then it also vanishes. Now it really is just you and the worm-bat. “NOTHING CAN STOP ME. NOTHING CAN BEAT ME. I AM ALL-POWERFUL. I AM THE PERFECT BEING. HA HA HA HA HAA,” intones the cube.\n\nWhat would you like to do?\n\n1) Slump against the wall and do nothing.\n2) Go outside with the worm-bat to come up with a plan.", True)
    #I3 = Game()
    #I4 = Game()
    #I5 = Game()
    #I6 = Game()
    #I7 = Game()
    #I8 = Game()
    P1 = Game(None, None, None, "If you are seeing this, you have accidentally torn a hole in the veil. Go back now.", False)
    # P1 was removed because of redundancy, but not from the array because of so many renumberings it would take.
    P2 = Game(None, None, None, "this is not yet written", False)
    # in P2, set alive == False
    #P3 = Game()
    #P4 = Game()
    #P5 = Game()
    #P6 = Game()
    #P7 = Game()
    #P8 = Game()
    P1A = Game(None, None, None, "You thump your back against the impossibly smooth stick wall and slide down until you’re sitting on the ground with your knees in your chest. You take the towel from around your neck, still damp from your shower last night, and place it over your head to block out all this idiocy. “WHAT ARE YOU DOING?” asks the cube. You ignore it, assuming that it is talking to the worm-bat. “I SAID, WHAT ARE YOU DOING?”\n“Who, me?” you ask, muffled under your towel.\n“YES. WHAT ARE YOU DOING? YOU WILL NOT STOP ME,” it says.\n“I’m not trying to stop you. I’m just sitting here,” you grumble. Under the towel, you wrap your arms around your legs and rest your chin on your knees.\n“THAT IS IMPOSSIBLE. UVIXWYZ BROUGHT YOU ALL HERE TO STOP ME. AN IMPOSSIBLE TASK. NOTHING CAN STOP ME. BUT WHY ARE YOU NOT FULFILLING YOUR FUNCTION?”\n“Leave me alone,” you mutter.\n“YOU MUST TRY TO STOP ME. I AM UNSTOPPABLE. YOU MUST TRY TO STOP ME. I AM UNSTOPPABLE. YOU MUST TRY—”\nYou hear strange popping noises, and take the towel off your head. The light on the front of the cube is flashing a rainbow of colours and a tendril of smoke is emanating from the slit. The light dies, and you sit there, waiting. Nothing happens. Nothing happens for a long time. It gets dark outside, and you finally decide to stand up. You haven’t seen the worm-bat since you put the towel over your head, but you assume it vanished like the rest of the aliens. You sling the towel over your shoulder and trudge back up the hill to the spaceship. The hatch opens for you and you go to the bridge and sit back down in your seat. The screen says, “Thank you,” in large friendly letters, and you scowl. Uvixwyz takes you back home, destroying your bathroom for a second time. You step out into your bedroom, dropping the towel on the chest at the foot of your bed as you walk to your alarm clock. It reads, “2:57 AM.” Ten minutes have passed since you woke up. Your grasp on time seems very wobbly. You lie down and fall asleep, your back to the hole in your wall. When you wake up, the hole is gone, and everything is completely normal and boring. Hooray.\n\nEND", False)
    P1B = Game(None, None, None, "You thump your back against the impossibly smooth stick wall and slide down until you’re sitting on the ground with your knees in your chest. You place your arms on your knees and duck your head to block out all this idiocy. “WHAT ARE YOU DOING?” asks the cube. You ignore it, assuming that it is talking to the worm-bat. “I SAID, WHAT ARE YOU DOING?”\n“Who, me?” you ask, your voice muffled from your arm fortress. \n“YES. WHAT ARE YOU DOING? YOU WILL NOT STOP ME,” it says.\n“I’m not trying to stop you. I’m just sitting here,” you grumble. You shift a little to get more comfortable.\n“THAT IS IMPOSSIBLE. UVIXWYZ BROUGHT YOU ALL HERE TO STOP ME. AN IMPOSSIBLE TASK. NOTHING CAN STOP ME. BUT WHY ARE YOU NOT FULFILLING YOUR FUNCTION?”\n“Leave me alone,” you mutter.\n“YOU MUST TRY TO STOP ME. I AM UNSTOPPABLE. YOU MUST TRY TO STOP ME. I AM UNSTOPPABLE. YOU MUST TRY—”\nYou hear strange popping noises, and look up. The light on the front of the cube is flashing a rainbow of colours and a tendril of smoke is emanating from the slit. The light dies, and you sit there, waiting. Nothing happens. Nothing happens for a long time. It gets dark outside, and you finally decide to stand up. You haven’t seen the worm-bat since you hid your face, but you assume it vanished like the rest of the aliens. You sigh and trudge back up the hill to the spaceship. The hatch opens for you and you go to the bridge and sit back down in your seat. The screen says, “Thank you,” in large friendly letters, and you scowl. Uvixwyz takes you back home, destroying your bathroom for a second time. You step out into your bedroom, avoiding the damp towel on the chest at the foot of your bed as you walk to your alarm clock. It reads, “2:57 AM.” Ten minutes have passed since you woke up. Your grasp on time seems very wobbly. You lie down and fall asleep, your back to the hole in your wall. When you wake up, the hole is gone, and everything is completely normal and boring. Hooray.\n\nEND", False)
    # in P1A and P1B, set alive == False

    gameNode[0] = A
    gameNode[1] = R1
    gameNode[2] = R2
    gameNode[3] = R3
    gameNode[4] = O1A
    gameNode[5] = O2
    gameNode[6] = O3
    gameNode[7] = O1B
    gameNode[8] = Y1
##    gameNode[9] = Y2
    gameNode[10] = Y3
    gameNode[11] = Y4
    gameNode[12] = Y5
    gameNode[13] = G1
##    gameNode[14] = G2
##    gameNode[15] = G3
##    gameNode[16] = G4
    gameNode[17] = G5Y
    gameNode[18] = G5N
    gameNode[19] = G6
    gameNode[20] = G7A
    gameNode[21] = G7B
    gameNode[22] = B1
    gameNode[23] = B2
##    gameNode[24] = B3
##    gameNode[25] = B4
##    gameNode[26] = B5
##    gameNode[27] = B6
##    gameNode[28] = B7
##    gameNode[29] = B8
    gameNode[30] = I1
    gameNode[31] = I2
##    gameNode[32] = I3
##    gameNode[33] = I4
##    gameNode[34] = I5
##    gameNode[35] = I6
##    gameNode[36] = I7
##    gameNode[37] = I8
    gameNode[38] = P1
    gameNode[39] = P2
##    gameNode[40] = P3
##    gameNode[41] = P4
##    gameNode[42] = P5
##    gameNode[43] = P6
##    gameNode[44] = P7
##    gameNode[45] = P8
    gameNode[46] = P1A
    gameNode[47] = P1B

    currentNode = gameNode[0]
   
    while(keepGoing):
        Play(currentNode)
        #okay. The issue you're running into with the Play() method,
        #is that it's only for a single object.
        #That's why every time you print the story, it'll be the same
        #what you want is a function (out side the class) that'll take
        #the current node and go through the logic, and then set the
        #object to a different object and repeat. so instead of `currentNode.Play()`,
        #it'll look like `Play(currentNode)`


if __name__ == "__main__":
    main()

