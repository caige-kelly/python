import random
import hangman_art as art
import hangman_words as words
import os

def init(list):
    display = []
    word = random.choice(list)
    for _ in word:
        display += "_"
    return word, display

chosen_word, display = init(words.word_list)
end_of_game = False
lives = 6
already_guessed = []

while not end_of_game:
    print(f"{art.logo}")
    print(f"{display}")
    print(f"{art.stages[lives]}")
    if lives == 0:
        print("You lost!")
        end_of_game = True
        break 

    if "_" not in display:
        print("You won!")
        end_of_game = True
        break
    guess = input("Guess a letter: ").lower()
    os.system('clear') 

    if guess not in display:

        if guess not in chosen_word:
            print(f"{guess} is not in the word")
            lives -= 1
        else:
            for position in range(len(chosen_word)):
                if chosen_word[position] == guess:
                    display[position] = guess
    else:
        print("You have already guessed this letter.")