import random
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in you password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

r_letters = random.choice(n_letters)
print(r_letters)

# print(f"Here is your password: {}")