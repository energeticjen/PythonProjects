# greet user and explain rules
print("Hello my new friend! Would you like to play a game? All you have to do is guess what number I'm thinking of, between 1 and 100!")
print("I'll tell you if your guess is too high, too low, or just right! I'll even tell you how many tries it took.")
print("Ready? Go!")

# generate random number
import random
number = random.randint(0, 100)

# set counter to 0
counter = 0

# set win = False
win = False

# start while loop
while (win == False):

    # add 1 to counter
    counter = counter + 1

    # have user guess
    guess = input("Guess a number! >> ")

    # convert input to integer
    guess = int(guess)

    # if high (guess > random), output high
    if guess > number:
        print("Your guess is too high!")

    # elif low (guess < random), output low
    elif guess < number:
        print("Your guess is too low!")

    # else right, output You win, counter count, and set win = True
    else:
        print("You got it! Great job! It took {} tries.".format(counter))
        win = True
    




