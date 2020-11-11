"""Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the
sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


# 0,1,1,2,3,5,8,13,21,34,55,
# 0, 1, 1+0, 1+1, 2+1, 2+3, 3+5,
import sys

from pip._vendor.distlib.compat import raw_input


def fibo(x):
    if x == 1:
        fib = [1]
    elif x == 2:
        fib = [1, 1]
    else:
        fib = [1, 1]
        a=1
        b=1
        for i in range(2, x, 1):
            c = a + b
            a=b
            b=c
            fib.append(c)
    return fib


while True:
    try:
        n = int(input("write a nr: "))
        print(fibo(n))
        i = input('Do you want to exit? ')
        if i == "":
            break
    except ValueError:
        print("Invalid number, introduce an integer")

