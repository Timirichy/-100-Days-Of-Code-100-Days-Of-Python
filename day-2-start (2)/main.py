#Data Types

#String
#Subscripting or indexing
# print("Hello"[4])

#Integer
# underscore in python integer is treated as a invincible
# it is just to assist humans differentiate our large numbers
# print(123_556_4923 + 394_439)

# Float
# numbers with decimal point
3.14159

# Boolean
# has only two inputs = which always starts with capital letter
True
False

# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)  #data type changing from int to string
# print("Your name has " + new_num_char + " characters.")

#type checking
# print(type(num_char))

#data type changing
a = float(100)
print(a)

print(70 + float("200"))

print(str(79) + str(599))


#       Arithmetizm
# PEMDASLR (more like BODMAS but for python)
#       Order of importance
# Parenthesis ()
# Exponential **
# Multiplication *
# Division /
# Addition +
# Subtraction -
# from Left
# to Right

5 + 5 # Addition
5 - 3 # Subtraction
6 / 2 # Division (akways comes as a float)
3 * 5 # Multiplication
2 ** 5 # Exponential

# e.g
print(3 * (3 + 3) / 3 - 3)
# * is executed first then / follows
# but if / comes first then it is executed first before *
# + is executed first before - 
# but if - comes first, then it is executed first before +

# Approximation
print(round(8/3, 2))  #this divides 8 by 3 and round up the float answer to 2 decimal place

# floor division
print(8 // 3) #this just divide and convert the result to an integer without rounding

# Number manipulation
result = 0
result += 1 #could be /=, -=, *= and so on
print(result)


#fstring

score = 2
height = 4
bright = 88

# in f string , f always comes before the quote that envelopes everything
# then the curly brackets install what it carries into that position
print(f"Your score is {score} ,your height is {height} and your future is {bright} ")