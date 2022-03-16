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
# print(Alphabets[-20])
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
import random
import my_module
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
