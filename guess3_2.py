"""Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess.
If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess,
user will get a "Well guessed!" message, and the program will exit.
"""

import random
import sys

#nr = [1,2,3,4,5,6,7,8,9]
#nr_random = random.choice(nr)
print("Welcome to the game!")
nr_random = random.randint(1, 10)

print(nr_random)


while True:
    try:
        nr_entered = int(input("Please enter a number: "))
        if nr_entered == nr_random:
            print(nr_entered)
            print("Well guessed")
            break
        else:
            print("The number is not correct.")
    except ValueError:
        print("Not an integer. Try again")

