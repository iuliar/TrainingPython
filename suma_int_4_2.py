"""
Create a program that computes the sum of all float and integer numbers from a list.
The given list contains other data types as well: strings, tuples, list of lists, etc.
 (e.g: at least one list element from each data type +
"""


initial_list = [1, 2, "unu", (3,4,5), "word", ['a', 'b', 'c'], 3, 6, 7.8, 9.2 ]
length_of_the_list = len(initial_list)
suma = 0
for i in range(length_of_the_list):
    if type(initial_list[i]) == int or type(initial_list[i]) == float:
        suma = suma + initial_list[i]

print("The sum of the integer and float values from the list is: ", suma)
