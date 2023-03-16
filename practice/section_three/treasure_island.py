import os
os.system('clear')

print("Welcome to Treaure Island! Your mission is to find the treasure.\n")

dungeon =input("You entered a dungeon. Your options are to go left or right. left/right\n")
if dungeon.lower() == "right":
    print("You went right and ran into a minator that rips your head off\n")
    print("GAME OVER!")
    quit()
print()
print("You go left and come out of the dungeon to the river Styx.")
print("At the mouth of the dungeon you see two pennies on the ground and pick them up.")
print("You approach the the edge of the water and look out")
print("In the fog a raft slowly appear; atop of it... the ferry man.") 
print()


river =input("Do you wait from him to take your across or swim? ride/swim\n")
if river.lower() == "swim":
    print("")
    print("You see the ferry man lock eyes on you")
    print("In a panic you jump into the water")
    print("You try and swim as hard as you can but")
    print("put the souls of the dead grab you and drag you under...")
    print("Game over")
    exit()

print('''
You freeze as the ferryman locks eyes with you. He reaches the shore and extends his hand
without saying a word. You stare at each other for a moment. You can think of any else
to do but hand him the two pennies you found on the ground early. He takes them without
saying a would and waves you on the raft. He pushes off and slowely farries you across
the river...

You arrive on the river. Steppin off the raft and walking forward three doors appear.
Green...
Red...
Yellow..
''')

door = input("Which door do you choose? Red/Green/Yellow\n")

if door.lower != "yellow":
    print("You open the door and fall into an endless abyess")
    print("Game Over!")
    exit()

print("You open the Yellow door... and... wake up... dreaming this entire time.")

