"""Create a game where the computer picks a random word and the player has to guess that word.
The computer tells the player how many letters are in the word.
Then the player gets five chances to ask if a letter is in the word.
 The computer can only respond with “yes” or “no”. Then, the player must guess the word.
 """
import random

words = ["masa", "casa", "scaun", "tabla", "televizor", "mobila", "creion", "noptiera", "candelabru"]


#random.choice()

print("Welcome to the game!")
word = random.choice(words)

number_of_chars = len(word)
print (number_of_chars)
print("The word has: %d letters" %(number_of_chars))
print (word)
i = 0
while i < 5:
    letter = input("Say letter:")
    for char in word:
        if char == letter:
            print("este")
        else:
            print("nu este")
    i +=1
#
# print("Guess the characters")
#
# guesses = ''
#
# # any number of turns can be used here
# turns = 12
#
# while turns > 0:
#
#     # counts the number of times a user fails
#     failed = 0
#
#     # all characters from the input
#     # word taking one at a time.
#     for char in word:
#
#         # comparing that character with
#         # the character in guesses
#         if char in guesses:
#             print(char)
#
#         else:
#             print("_")
#
#             # for every failure 1 will be
#             # incremented in failure
#             failed += 1
#
#         if failed == 0:
#             # user will win the game if failure is 0
#             # and 'You Win' will be given as output
#             print("You Win")
#
#             # this print the correct word
#             print("The word is: ", word)
#             break
#
#         # if user has input the wrong alphabet then
#         # it will ask user to enter another alphabet
#         guess = input("guess a character:")
#
#         # every input character will be stored in guesses
#         guesses += guess
#
#         # check input with the character in word
#         if guess not in word:
#
#             turns -= 1
#
#             # if the character doesn’t match the word
#             # then “Wrong” will be given as output
#             print("Wrong")
#
#             # this will print the number of
#             # turns left for the user
#             print("You have", + turns, 'more guesses')
#
#             if turns == 0:
#                 print("You Loose")