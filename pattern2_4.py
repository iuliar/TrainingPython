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
# i = 1
# j = 2
# for i in range(9):
#     if i < 6:
#         print(i * "* ")
#     else:
#         print ((i-j) * "* ")
#         j += 2


#Varianta 2
i = 1
for i in range(6):
    print(i * "* ")

j = 5
while j > 2:
    print((j-1) * "* ")
    j = j-1
