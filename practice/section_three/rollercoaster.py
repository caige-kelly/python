print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster ")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 & age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 15
    
    photo = input("Would would you like a photo? y/n ")
    if (photo == "y"):
        bill += 3
        print("Please pay $" + str(bill))
    else:
        print("Please pay $" + str(bill))
else:
    print("Sorry, you have to grow taller before you can ride ")
    