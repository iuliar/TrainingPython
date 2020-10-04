"""Create a game where the computer picks a random word and the player has to guess that word.
The computer tells the player how many letters are in the word.
Then the player gets five chances to ask if a letter is in the word.
 The computer can only respond with “yes” or “no”. Then, the player must guess the word.
 """
import random

words = ["masa", "casa", "scaun", "tabla", "televizor", "mobila", "creion", "noptiera", "candelabru"]

random.choice(words)

print("Welcome to the game!")
word = random.choice(words)

number_of_chars = len(word)
print("The word has: %d letters" %(number_of_chars))

count = 0
lista = list(word)
lista2 = []
for j in range(number_of_chars):
    lista2.append("-")

while count < len(word) and count < 5:
    letter = input("write a letter: ")
    k = 0
    for i in lista:
        if letter == i:
            lista2[k] = letter
        k = k+1
    print(lista2)
    count = count + 1
    if "-" in lista2:
        continue
    else:
        break

guess = input("\nGuess the word: ")
if guess == word:
    print("Yes, you are right. The word is: ", word)
else:
    print("Sorry, you are not right. The word is: ", word)

