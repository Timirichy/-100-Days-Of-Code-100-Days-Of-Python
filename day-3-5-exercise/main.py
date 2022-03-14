# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#so we check through them alltogether  only ones
combined_string = name1 + name2 
#then we convert any case letter entered to lower case
lowercase_combined_string = combined_string.lower()
#now we count for TRUE LOVE
t = lowercase_combined_string.count("t")
r = lowercase_combined_string.count("r")
u = lowercase_combined_string.count("u")
e = lowercase_combined_string.count("e")

# then we add it up
true = t + r + u + e

# also
l = lowercase_combined_string.count("l")
o = lowercase_combined_string.count("o")
v = lowercase_combined_string.count("v")
e = lowercase_combined_string.count("e")

love = l + o + v + e
# we have to convert true and love to string so we can concatenate them without adding them
true_love = int(str(true) + str(love))
# print(type(true))
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
