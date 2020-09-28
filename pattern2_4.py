"""Write a Python program to construct the following pattern:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
"""

i = 1
for i in range(6):
    print(i * "* ")

j = 5
while j > 2:
    print((j-1) * "* ")
    j = j-1
