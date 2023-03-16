import random
# Boilerplate
rock = '''
    ______
---'   ___)_
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ______
---'   ___)___
       _______)
       ________)
       _______)
---.________)
'''

scissors = '''
    _____
---'   __)____
       _______)
       ________)
       (____)
---.___(___)
'''

array = ["rock", "paper", "scissors"]

user_choice = int(input("Select rock, paper, or scissors (1, 2, 3): "))
computer_choice = round(random.random() * 3)

# So easy a caveman could do it
if user_choice == 1:
    if computer_choice == 1:
        print(f"{rock}\nYou tie!")
    elif computer_choice == 2:
        print(f"{paper}\nYou lose!")
    else:
        print(f"{scissors}\You win!")

elif user_choice == 2:
    if computer_choice == 1:
        print(f"{rock}\nYou win!")
    elif computer_choice == 2:
        print(f"{paper}\nYou tie!")
    else:
        print(f"{scissors}\nYou lose!")

elif user_choice == 3:
    if computer_choice == 1:
        print(f"{rock}\nYou lose")
    elif computer_choice == 2:
        print(f"{paper}\n You win!")
    else:
        print(f"{scissors}\nIt's a tie")

else:
    print("invalid number. you lose")
