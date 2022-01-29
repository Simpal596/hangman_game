import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
life = 6
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []

for n in range(len(chosen_word)) :
    display.append("_")

check = display.count("_")
blanks = len(display)

while life > 0 and blanks > 0 :
    guess = input("Enter your letter")
    for i in range(len(chosen_word)) :
        if chosen_word[i] == guess :

            display[i] = guess
            check -= 1

    if blanks == check :
        life -= 1
    print(display)
    print(" ".join(display))
    print(stages[life])
    blanks = display.count("_")

if life > 0 :
    print("YOU WIN")

else :
    print("YOU LOOSE")







