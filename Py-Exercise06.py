# Task 1

import random

# generate a random number between 1 and 10
number = random.randint(1, 10)

# ask the user to guess the number
guess = int(input("Guess the number between 1 and 10: "))

# use a while loop to keep asking for guesses until the user gets it right
while guess != number:
    print("Sorry, that's not it.")
    guess = int(input("Guess again: "))

# congratulate the user once they guess correctly
print("Congratulations! You guessed the number!")


# generate a random number between 1 and 10
number = random.randint(1, 10)

# initialize variables for tracking the number of guesses and the player's guess
guesses = 0
guess = None

# use a while loop to keep asking for guesses until the player guesses the correct number
while guess != number:
    # prompt the player to make a guess and convert their input to an integer
    guess = int(input("Guess the number between 1 and 10: "))
    guesses += 1

    # compare the player's guess to the target number and give feedback
    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")

# print a message congratulating the player on their guess and telling them how many guesses it took
print(f"Congratulations! You guessed the number in {guesses} guesses.")

# Task 2

# initialize the first two numbers in the series
a, b = 1, 1

# print out the first two numbers
print(a)
print(b)

# use a loop to generate and print the remaining numbers in the series
for i in range(2, 50):
    # calculate the next number in the series as the sum of the previous two
    c = a + b
    
    # print out the next number in the series
    print(c)
    
    # update the previous two numbers to prepare for the next iteration
    a, b = b, c