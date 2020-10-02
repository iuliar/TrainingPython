"""Write a program that counts for the user.
Let the user enter the starting number, the ending number, and the amount by which to count.
"""
import sys
# try:
#     a = int(input("Initial nr: "))
# except ValueError:
#     while int(a).is_integer():
#         print("The value introduced in not an integer. Try again")
#         a = int(input("Initial nr: "))

try:
    a = int(input("Initial nr: "))
    b = int(input ("Final nr: "))
    x = int(input ("Amount nr: "))

except ValueError:
    print("Not an integer: ")
    sys.exit()

while b < a:
    try:
        b = int(input("Please choose other number for final number bigger then %d " %a))
    except ValueError:
        print("The value introduced in not integer. Try again")
        b = int(input("Final nr: "))

for i in range(a, b, x):
    print(i)
