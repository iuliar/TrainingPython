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
#Varianta 1
i = 1
j = 2
for i in range(10):
    if i < 6:
        print(i * "* ")
    else:
        print ((i-j) * "* ")
        j += 2