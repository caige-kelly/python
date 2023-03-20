import os
from art import logo


print(logo)
print("Welcome to the secret auction program.")

bidders = {}
other_bidders = True


def winner():
    winner = ""
    highest_bid = 0
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            winner = bidder   
    print(f"{winner} in the winner with the highest bid of ${bidders[winner]}!")


while other_bidders:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bidders[name] = bid

    additional = input("Are there any other bidders? type yes or no\n").lower()

    if additional == "no":
        other_bidders = False
        winner()

    else:
        os.system("clear")