"""Write a program that counts for the user.
Let the user enter the starting number, the ending number, and the amount by which to count.
"""
import sys
while True:
    try:
        a = int(input("Initial nr: "))
        break
    except ValueError:
        print("The value introduced in not an integer. Try again")
        continue


while True:
    try:
        b = int(input("Final nr: "))
        if a < b:
            break
        else:
            print ("Please insert a value bigger then initial one")
    except ValueError:
        print("The value introduced in not an integer. Try again")
        continue

while True:
    try:
        x = int(input("Amount nr: "))
        if  x > 0:
            break
        else:
            print ("Please insert a value bigger then 0")
    except ValueError:
        print("The value introduced in not an integer. Try again")
        continue

for i in range(a, b, x):
    print(i)
