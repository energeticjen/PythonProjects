# ask user how much item is and store as ItemCost.
ItemCost = input("How much money does your chosen item cost? ")

# convert input to a float from a string.
ItemCost = float(ItemCost)

# ask user for payment amount and store as Payment.
Payment = input("How much money are you using to pay for this? ")

# convert Payment to a float from a string.
Payment = float(Payment)

# subtract ItemCost from Payment and store as Change.
Change = Payment - ItemCost

# display Change (as float automatically).
print("Your change is ${0:.2f}.".format(Change))

# multiply Change by 100 to move the decimal over twice.
Change = Change * 100

# convert to an integer.
Change = int(Change)

# Change / 2000 and store in variable Twenties
Twenties = Change / 2000

# convert from float to int
Twenties = int(Twenties)

# modulus Change by 2000 and store as Change.
Change = Change%2000

# Change / 1000 and store as Tens
Tens = Change / 1000

# convert from float to int
Tens = int(Tens)

# modulus Change by Tens and store as Change.
Change = Change%1000

# Change / 500 and store as Fives
Fives = Change / 500

# convert from float to int
Fives = int(Fives)

# modulus Change by Fives and store as Change.
Change = Change%500

# Change / 100 and store as Ones.
Ones = Change / 100

# convert from float to int
Ones = int(Ones)

# modulus Change by Ones and store as Change.
Change = Change%100

# Change / 25 and store as Quarters.
Quarters = Change / 25

# convert from float to int
Quarters = int(Quarters)

# modulus Change by Quarters and store as Change.
Change = Change%25

# Change / 10 and store as Dimes.
Dimes = Change / 10

# convert from float to int
Dimes = int(Dimes)

# modulus Change by Dimes and store as Change.
Change = Change%10

# Change / 5 and store as Nickels.
Nickels = Change / 5

# convert from float to int
Nickels = int(Nickels)

# modulus Change by Nickels and store as Change.
Change = Change%5

# Change / 1 and store as Pennies.
Pennies = Change / 1

# convert from float to int
Pennies = int(Pennies)

# Display breakdown of Twenties, Tens, Fives, Ones, Quarters, Dimes, Nickels, and Pennies.
print("Twenties: {} \nTens: {} \nFives: {} \nOnes: {} \nQuarters: {} \nDimes: {} \nNickels: {} \nPennies: {}".format(Twenties, Tens, Fives, Ones, Quarters, Dimes, Nickels, Pennies))
