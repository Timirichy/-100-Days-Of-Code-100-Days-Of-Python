# Randomisation and Python List

# (A) Randomisation

# 040
# Random Module

# import random
# random_integer = random.randint(1, 10)
# print(random_integer)
# 
# #this enerates number between 0 and 1, with as many
# # decimal places it can
# random_float = random.random()
# print(random_float)
# 
# # radom decimal btw 0 and 5
# random_decimal = random.random() * 5
# print(random_decimal)

#                     Moduling
# import my_module
#             where my_module is another .py file created in the same folder withe that name
#             so to call it, you say the name of the .py file the .(the name of a variable in it)
# print(my_module.pi)

# 041
# Heads or Tails exercise

# import random
# test_seed = input("Heads or Tails: ")
# 
# number = random.randint(0,1)
# if number == 1:
#     print("Heads")
# else:
#     print("Tails")

# (B) LISTS

# 042
# List is always enclosed in a square bracket []
# +ve index count from left of the list to thr right,
# -ve index counts from the right to the left of the list
# starting from -1
# Alphabets = ['A','B','C','D','E','9','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
# print(Alphabets[-20]) #This is for displaying the element in alphabets at the position in []
# # correcting element on a list
# Alphabets[5] = 'F'
# # adding  elements to a list
# Alphabets.append('U')
# # adding a bunch of elements to the list
# Alphabets.extend(['V','W','X','Y','Z'])
# print(Alphabets)

# 043
# Banker Roulette Excercise

# Split string method
# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # print(names)
# lenght = len(names)
# # print(lenght)
# random = random.randint(0, lenght - 1)
# # print(random)
# # print(type(lenght))
# final = names[random]

# This can simply be written as a one line code:
# final = random.choice(names)
# print(final + " is going to pay for our meal")

# 044
# Nested List
# Digits= [0,1,2,3,4,5,6,7,8,9]
# print(Digits)
# Now nesting Alphabets and Digits together
# Alphabets_Digits = [Alphabets,Digits]
# print(Alphabets_Digits)

# 045
# Treasure Map Exercise

# row1 = ["@","@","@"]
# row2 = ["@","@","@"]
# row3 = ["@","@","@"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 
# # example 23 i.e column 2 and row 3
# horizontal = int(position[0]) #2
# vertical = int(position[1]) #3
# 
# # selected_row = map[vertical - 1]
# # selected_row[horizontal - 1] = "X"
# # # this line can also be written single
# map[vertical - 1][horizontal - 1] = "X"
# 
# print(f"{row1}\n{row2}\n{row3}")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[1][1])
# print(dirty_dozen[0])
# print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])