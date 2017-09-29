#Output a greeting and ask for a name. Input on a separate line.
name = input("Hello! What's your name?\n>> ")

# Offer user a menu selection of jokes
print("\nIt's really nice to meet you! My name is ********."
    "\nI have here a selection of jokes for you, {}. Please input the number corresponding to the joke you'd like to hear:\n".format(name))

# Output the menu
print("\t1. Knock Knock Joke", "\t2. Lightbulb Joke", "\t3. One-Liner",
    "\t4. A Stupid Joke", "\t5. A Limerick", "\t6. A Pun", "\t7. 6 Afraid of 7 Joke",
    "\t8. Ham Joke", "\t9. Software Developer Joke", "\t10. My Favourite Joke", sep="\n")

# Get user's choice
choice = input(">> ")

# If 1, knock knock joke
if choice == "1":# The End Function

    # Output Introduction and "Knock knock!" on a separate line
    print("An excellent selection, {}.\n\nKnock knock!".format(name))

    # Get input on a new line that hopefully says, "who's there?"
    knockResponse1 = input(">> ")

    #Output second line of joke.
    print("Dishes")

    # Get input on a new line that hopefully says, "Dishes who?"
    knockResponse2 = input(">> ")

    # Output punchline.
    print("Dishes Sean Connery.\n")

# This was an attempt at a loop back to the menu outside of this if statement. I couldn't get
# it to work. I attempted to define some functions [menu, end, main], but I think I need a while loop.
# I don't know how to make one that "big"

    # Output an option to go back to the menu.
    #print("Would you like to hear another joke, {}? Please type 'yes' or 'no'".format(name))

    # Get choice input from user
    #choice2 = input(">> ")

    # If yes, loop back to the menu
    #if choice2 == "yes":
        #menu()

        # Get user's choice
        #choice = input(">> ")

    # If no, go to end
    #elif choice2 == "no":
        #end()

    # If not one of the choices, display error message and ask again.
    #else:
        #print("I'm sorry, {}, but I didn't understand what you said. Could you repeat that?".format(name))

# If 2, lightbulb joke
elif choice == "2":

    # Output introduction and the first part of the joke
    print("Ah, I see you'd like to hear a lightbulb joke! Wonderful, {}.\nHow many software engineers does is take to change a lightbulb?".format(name))

    # Get input on a new line that hopefully says something like, "How many?" or a guess of some sort.
    lightbulbResponse = input(">> ")

    # Output punchline of joke
    print("None. That's a hardware issue.")

# If 3, one-liner joke
elif choice == "3":

    # Output introduction
    print("{}, I just want you to know that this joke is a little different than the others, because it's all in one line. Is that alright?".format(name))

    # Get input on a new line that says something like, "Yes."
    oneLinerResponse = input(">> ")

    # Output joke
    print("Here it is! \nThank you, student loans for getting me through university. I don't think I can ever repay you.")

# If 4, stupid joke
elif choice == "4":

    # Output introduction and joke
    print("Just because this says it's a stupid joke, doesn't mean that either one of us are stupid, {}. Just a little reasurrance."
    "\n\nThe word 'Diputseromneve' may look ridiculous, but backwards it's even more stupid.".format(name))

# If 5, limerick joke
elif choice == "5":

    # Output introduction and limerick
    print("This limerick will probably look a little funny to you, {}."
    "\n\n(12+144+20+3sqrt4)/7 + (5*11) = 9^2 + 0"
    "\n\nWould you rather have it in words?".format(name))

    # Get response from user
    limerickResponse = input(">> ")

    print("\nOkay, {}. Here it is another way:"
    "\n\nA dozen, a gross, and a score \nPlus three times the square root of four"
    "\nDivided by seven \nPlus five times eleven \nIs nine squared and not a bit more!".format(name))

# If 6, a pun
elif choice == "6":

    # Pun Introduction
    print("You know {}, puns get a bad rap, but I happen to adore them. Here is a pun for you!".format(name))

    # Output pun
    print("\nOne guacamole is equal to 6.0221415 x 10^23 guacas. \nSomeone might even call it..."
        "\n\tAvocado's Number.")

# If 7, 6 afraid of 7 joke
elif choice == "7":

    # Introduction
    print("Now this joke is one that just about everyone knows. Do you know this joke, {}?"
        "\n\nWhy was six afraid of seven?".format(name))

    # Get user input, hopefully a guess or "why?"
    sixResponse = input(">> ")

    # Output punchline of joke
    print("\nIt wasn't. Numbers are not sentient and thus incapable of feeling fear.")

    # Output joke information
    print("\nThis is called an anti-joke. Did you get the answer right?"
    "\nDon't feel bad if you didn't, {}. It was really meant for the Vulcans.".format(name))

# If 8, what a ham joke
elif choice == "8":

    # Joke
    print("That's an awfully nice ham you've got there, {}."
    "\nIt would be a shame if someone put an 's' at the front and an 'e' at the end.".format(name))

# If 9, software developer joke
elif choice == "9":

    # Joke Introduction
    print("Who wouldn't want to hear a joke about a software developer? They're such funny people, am I right, {}?".format(name))

    # Get user's feeling on software developers
    sdResponse = input(">> ")

    # Output the joke
    print("Ah, I see. Well anyway, there once was a woman whose husband was a software developer."
    "\nOne day she said to him, 'Would you please go to the store and buy a loaf of bread? And if there's eggs,"
    " bring home a dozen.' \nThe husband returned with twelve loaves of bread.")

# If 10, my favourite joke
elif choice == "10":

    # Favourite Joke Introduction
    print("I'm sure you didn't think that I'd have a favourite joke, but I do, and this is it."
    "\nI don't think I could tell you why; those subroutines are missing, {}."
    "\nBut here's the joke anyway:".format(name))

    # First line of favourite joke
    print("\nWhat did the hotdog way when it won the race?")

    # Get user response
    favResponse = input(">> ")

    # Punchline of the joke
    print("'I'm the wiener!'")

#If not one of the choices offered
else:

    # Error response
    print("Oh, I'm sorry, {}, but I don't know what you said. I guess you'll have to restart my program.".format(name))
