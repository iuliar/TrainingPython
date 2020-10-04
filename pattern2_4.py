"""Write a Python program to construct the following pattern:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""


#Varianta 1

for i in range(6):
    print(i * "* ")

j = 4
while j > 0:
    print(j * "* ")
    j = j-1


