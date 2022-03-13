#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
# print(total_bill)
#Each person should pay (150.00 / 5) * 1.12 = 33.6
tip_to_give = input("How much tip would you like to give? 10, 12, 15? ")
# print(tip_to_give)
#Format the result to 2 decimal places = 33.60
no_of_people = input("How many people to split the bill? ")
# print(no_of_people)
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# calculation
result = (float(total_bill) / int(no_of_people)) * (1 + (int(tip_to_give) / 100))
new_result = round(result, 2)
new_result = "{:.2f}".format(result) #this helps approximate all calculated result to
# 2 decimal places, even if the result is a whole number which the round function cannot do
print(f"Each person should pay: ${new_result}")

#Write your code below this line 👇