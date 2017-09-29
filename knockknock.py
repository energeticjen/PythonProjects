# Output a greeting and ask for a name. Input on a separate line.
name = input("Hello! What's your name?\n>> ")
# Output "Here's a joke, <name>. Knock knock!"
print("Here's a joke, {}. Knock knock!".format(name))
# Get input on a new line that hopefully says, "who's there?"
response1 = input(">> ")
# Output second line of joke.
print("Dishes")
# Get input on a new line that hopefully says, "Dishes who?"
response2 = input(">> ")
# Output punchline.
print("Dishes Sean Connery.")
