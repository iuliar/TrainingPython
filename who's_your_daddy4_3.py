dict = {
    "Florin Piersic": 'Florin Piersic JR',
    "Douglas": "Douglas JR",
    "Denzel Washinghton": "John Washington",
    "Stellan Skarsgard": "Alexander Skarsgard",
    "Quincy Jones": "Rashida Jones"
}

while True:
    print("Please type in your selection: \n"
          "- list: \n"
          "- get: \n"
          "- add: \n"
          "- replace: \n"
          "- delete: \n")
    user_input = input()
    if user_input == "list":
        print(input("Print the name of the Father: "))

# print("Enter the name of actor: ")
# father = input()
# print (dict.get(father))
# print("What do you want to do? Change or Delete")
# mod = input()
#
# print("Is this correct?(Yes/NO)")
# bool = input()
# if bool == "Yes":
#     print ("Cool")
# else:
#     print("Change the name of the son?(Yes/NO)")
#     a = input()
#     if a == "Yes":
#         dict["Florin Piersic"] = input("Enter the ", father, "son")
#         print("The son of", father, "is :", dict.get(father))
#     else:
#         print("Cool")
#
#
# #add, replace, and delete son- father pairs.}
