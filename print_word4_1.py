"""Create a program that prints a list of random words.
The program should print all the words and not repeat any.
"""

#This should be discuss
import random
words = ["Ana", "are", "mere", "si", "pere", "si", "mai", "are", "si", "Alune", "mere", "pere"]
#anyway.. asta e lista cu random words.

print(random.sample(words, len(words))) # print list of random words
print(set(random.sample(words, len(words)))) # asta e folosita pentru partea a doua - "not repeat any"
