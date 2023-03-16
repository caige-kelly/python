import random

names_string = input("Enter comma seperated list of names:\n")

names = names_string.replace(" ", "").split(",")

number = round((random.random()*len(names)))

print(f'{names[number]} has to pay the bill')