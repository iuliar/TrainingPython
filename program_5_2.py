"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

list1 = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]


def order():
    list2 = [list1[0], list1[-1]]
    return print(list2)


order()

