### BOILERPLATE ###
import random

letters = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
let_num_sym = ["letters", "numbers", "symbols"]
let_sym = ["letters", "symbols"]
let_num = ["letters", "numbers"] 
### BOILERPLATE ###

c_letters = int(input("How many letters would you like in your password?\n"))
c_symbols = int(input("How many symbols would you like?\n"))
c_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for i in range(0, c_letters):
    password_list.append(random.choice(letters))

for i in range(0, c_symbols):
    password_list.append(random.choice(symbols))

for i in range(0, c_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(f"{password}")