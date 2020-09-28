"""Write a program that counts for the user.
Let the user enter the starting number, the ending number, and the amount by which to count.
"""

a = int(input("Initial nr: "))
b = int(input ("Final nr: "))
x = int(input ("Amount nr: "))

while x <= 0:
    x = int(input("Amount nr should bigger then 0. Choose other one:  "))

while b < a:
    b = int(input("Please choose other number for final number bigger then %d " %a))


for i in range(a, b, x):
    print(i)
