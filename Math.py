"""Write a program that counts for the user.
Let the user enter the starting number, the ending number, and the amount by which to count.
"""



a = int(input("Initial nr:"))
b = int(input ("Final nr:"))
x = int(input ("Amount nr:"))

for i in range(a, b, x):
    print(i)
