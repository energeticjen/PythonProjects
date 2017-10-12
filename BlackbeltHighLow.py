#import pdb
#pdb.set_trace()

goodAnswers = ['h','l','y']

def end(counter):

    # celebratory statement and display counter
    print("Woo hoo! I got it! And it only took me {} tries!".format(counter))

def lowerThan50(answer):

    # set the upper limit and lower limit for math purposes
    upperLimit = 50
    lowerLimit = 1

    # set guess to 25, halfway within this section
    guess = 25

    # output guess
    print("My guess is {}!".format(guess))

    # set counter to 2
    counter = 2

    # get input as a different variable to keep branching within this section
    answer = input("How did I do?   >> ")

    while (answer != 'y'):

        # if guess is too high, use this branch
        if (answer == 'h'):

            # if the guess is too high, set the upper limit to the guess
            #so numbers above that won't be checked
            upperLimit = guess

            # make the guess an integer halfway between the upper and lower limits
            guess = int((guess + lowerLimit)/2)

            # display guess
            print("My guess is {}!".format(guess))

            # add 1 to counter
            counter = counter + 1

            # get input
            answer = input("How did I do?   >> ")

        # if the guess is too low, use this branch
        if (answer == 'l'):

            # if the guess is too low, set the lower limit to the guess
            # so numbers below it won't be checked
            lowerLimit = guess

            # make the guess an integer halfway between the upper and lower limits
            guess = int((guess + upperLimit)/2)

            # display guess
            print("My guess is {}!".format(guess))

            # add 1 to counter
            counter = counter + 1

            # get input
            answer = input("How did I do?   >> ")

        # if the answer is correct
        if (answer == 'y'):

           # call end function while carrying counter variable
           end(counter)

           #set win to True
           win = True

           #return to main function
           return win

        # if there is an error
        if not answer in goodAnswers:
           answer = input("I'm sorry, could you repeat that?   >> ")

    # if 25 is correct
    if (answer == 'y'):

        # call end function while carrying counter variable
        end(counter)

        # set win to True
        win = True

        # return to main function
        return win

def higherThan50(answer):

    # set upper limit and lower limit for math purposes
    upperLimit = 101
    lowerLimit = 50

    # set guess to 75, halfway within this section
    guess = 75

    # output guess
    print("My guess is {}!".format(guess))

    # set counter to 2
    counter = 2

    # get input as a different variable to keep branching within this section
    answer = input("How did I do?   >> ")

    while (answer!= 'y'):

        # if guess is too high, use this branch
        if (answer == 'h'):

            # if the guess is too high, set the upper limit to the guess
            #so numbers above that won't be checked
            upperLimit = guess

            # make the guess an integer halfway between the upper and lower limits
            guess = int((guess + lowerLimit)/2)

            # display guess
            print("My guess is {}!".format(guess))

            # add 1 to counter
            counter = counter + 1

            # get input
            answer = input("How did I do?   >> ")

        # if the guess is too low, use this branch
        if (answer == 'l'):

            # if the guess is too low, set the lower limit to the guess
            # so numbers below it won't be checked
            lowerLimit = guess

            # make the guess an integer halfway between the upper and lower limits
            guess = int((guess + upperLimit)/2)

            # display guess
            print("My guess is {}!".format(guess))

            # add 1 to counter
            counter = counter + 1

            # get input
            answer = input("How did I do?   >> ")

        # if the answer is correct
        if (answer == 'y'):

            # call end function while carrying counter variable
            end(counter)

            # set win to True
            win = True

            # return to main function
            return win

        # if there is an error
        if not answer in goodAnswers:
           answer = input("I'm sorry, could you repeat that?   >> ")

    # if 75 is correct
    if (answer == 'y'):

        # call end function while carrying counter variable
        end(counter)

        #set win to True
        win = True

        #return to main function
        return win

def main():
    # greet user and explain the rules
    print("Hello! Let's play a game where you pick a number between 1-100, and I'll guess!"
          "\nIf my guess is too high, put 'h'. If my guess is too low, put 'l'. "
          "If I get it right, put 'y'. That means, 'Yes! You got it!' \nI'll let you know "
          "how many tries it took me.")

    # set counter to 1
    counter = 1

    #set initial guess to 50
    guess = 50

    # set win = False
    win = False

    # output guess
    print()
    print("My guess is {}!".format(guess))

    # get answer1 to determine which half of main branch to use (above 50 or below 50)
    answer1 = input("How did I do?   >> ")

    # start while loop for guessing number - while win = False
    while (win == False):

        # if the number is somewhere above 50 call higherThan50 function
        if (answer1 == 'l'):

            higherThan50('l')
            win = True

        # if the number is somewhere below 50 call lowerThan50 function
        if (answer1 == 'h'):

            lowerThan50('h')
            win = True

        # if the first answer is correct
        if (answer1 == 'y'):

            # call end function while carrying counter variable
            end(counter)
            win = True

        # if there is an error
        if not answer1 in goodAnswers:
           answer1 = input("I'm sorry, could you repeat that?   >> ")

main ()

