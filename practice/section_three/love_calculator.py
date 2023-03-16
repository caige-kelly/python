print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

#use lower()
#use count()

true = ["t","r","u","e"]
love = ["l","o","v","e"]
 

first=0
second=0
for letter in true:
    first += name1.lower().count(letter)
    first += name2.lower().count(letter)

for letter in love:
    second += name1.lower().count(letter)
    second += name2.lower().count(letter) 

love_score = (first * 10) + second

if (love_score < 10) or (love_score > 90):
    print(f"Your score is %{love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is %{love_score},you are alright together")
else:
    print(f"Your score is %{love_score}")