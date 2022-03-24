#conditional statement

#water_level = 50
#if water_level > 80:
#    print("Drain water")
#else:
#    print("Continue")
    
#print("Welcome to the rollercoaster")
#height = int(input("What is your height in cm? "))
#bill = 0

#This is a conditional statement
#if height >= 120:
#    print("You can ride the rollercoaster!") #if condition is true do this line
    #this is a nested conditional statement
#    age = int(input("What is your age? "))
#    if age < 12:
        #if this true, do next line
#        bill = 5
#        print("Child Tickets are $5.")
#    elif age <= 18:
#        bill = 7
    #this mean that ages between 12 and 18 is cleared to do the next line
#        print("Youth Tickets are $7.")
#    else:
#        bill = 12
        #if nested main condition is false, then do next line
#        print("Adult Tickets are $12.")
        
    #After finishing the statement up it then moves
    #to the statement down because they have the same indentation
#    want_photo = input("Do you want a photo taken? Y or N. ")
#    if want_photo == "Y":
        #add $3 to their bill
#        bill += 3
#    if age > 45 and age < 55:
#        bill = 0
        #no need for else since we want it to do nothing if no
    # it then moves to the next line after answering above
#    print(f"Your final bill is ${bill}")
    
#else: #if the main is not true then do the next line
#    print("Sorry, you have to grow taller before you can ride.")
        
#comparison operators
#    >    Greater than
#    <    Lesser than
#    >=   Greater than or equal to
#    <=   Lesser than or equal to
#    ==   Equal to
#    !=   Not equal to

#number = int(input("Which number do you want to check? "))

#if number % 2 == 0:
#    print("This is an even number.")
#else:
#    print("This is an odd number.")

#BMI Calculator 2.0

#height = float(input('enter your height in m: '))
#weight = float(input('enter yout wight in kg: '))

#bmi = round(weight / (height ** 2))

#if bmi < 18.5:
 #   print(f"Your bmi is {bmi}, you are underwight")
#elif bmi < 25:
 #   print(f"Your bmi is {bmi}, you are normal weight")
#elif bmi < 30:
 #   print(f"Your bmi is {bmi}, you are overweight")
#elif bmi < 35:
 #   print(f"Your bmi is {bmi}, you are obese")
#else:
 #   print(f"Your bmi is {bmi}, you are clinically obese")
 
#Leap year calculator
#year = int(input("Which year do you want to check? "))

#if year % 4 == 0:
#    if year % 100 == 0:
 #       if year % 400 == 0:
  #          print("Leap year.")
   #     else:
    #        print("Not leap year.")
    #else:
     #   print("Leap year.")
#else:
 #   print("Not leap year.")
 
 
 #Pizza Order Practice
 
#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")

#bill = 0
#if size == "S":
#    bill += 15
#elif size == "M":
#    bill += 20
#else:
#    bill += 25
#else statement not needed
#if add_pepperoni == "Y":
#    if size == "S":
#        bill += 2
#    else:
#        bill += 3
    
#if extra_cheese == "Y":
#    bill += 1
    
#print(f"Your final bill is ${bill}.")

#LOGICAL OPERATORS

#Love Calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 
# #so we check through them alltogether  only ones
# combined_string = name1 + name2 
# #then we convert any case letter entered to lower case
# lowercase_combined_string = combined_string.lower()
# #now we count for TRUE LOVE
# t = lowercase_combined_string.count("t")
# r = lowercase_combined_string.count("r")
# u = lowercase_combined_string.count("u")
# e = lowercase_combined_string.count("e")
# 
# # then we add it up
# true = t + r + u + e
# 
# # also
# l = lowercase_combined_string.count("l")
# o = lowercase_combined_string.count("o")
# v = lowercase_combined_string.count("v")
# e = lowercase_combined_string.count("e")
# 
# love = l + o + v + e
# # we have to convert true and love to string so we can concatenate them without adding them
# true_love = int(str(true) + str(love))
# # print(type(true))
# if true_love < 10 or true_love > 90:
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif true_love >= 40 and true_love <= 50:
#     print(f"Your score is {true_love}, you are alright together.")
# else:
#     print(f"Your score is {true_love}.")

# TREASURE ISLAND

print('''
                                            |
                                      --====|====--
                                            |  
                                        .-"""""-. 
                                      .'_________'. 
                                     /_/_|__|__|_\_\
                                    ;'-._       _.-';
               ,--------------------|    `-. .-'    |--------------------,
                ``""--..__    ___   ;       '       ;   ___    __..--""``
                 jgs      `"-// \\.._\             /_..// \\-"`
                             \\_//    '._       _.'    \\_//
                              `"`        ``---``        `"`

''')
print("Welcome To Treasure Island.")
print("Your mission is to find the treasure.")
old_road = input("You are at a cross road. Where do you want to go? 'left' or 'right'\n")
road = old_road.lower()

if road == "left":
    o_choice = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    choice = o_choice.lower()
    if choice == "wait":
        o_door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        door = o_door.lower()
        if door == "yellow":
            print("Game Won")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")

    