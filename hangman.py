import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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
word_list = ["aardvark", "baboon", "camel", "elephant", "giraffe", "kangaroo",
             "dolphin", "penguin", "rhinoceros", "flamingo", "alligator",
             "chimpanzee", "porcupine", "crocodile", "meerkat", "zebra",
             "hippopotamus", "lemur", "wombat", "platypus", "toucan",
             "koala", "cheetah", "jaguar", "panther", "ostrich",
             "antelope", "mongoose", "sloth", "armadillo"]

chosen_word = random.choice(word_list)
lives = 6
# print(chosen_word)
all_guessed_letters = []
correct_letters = []

game_over = False
while not game_over:
    print(stages[lives])
    print(f"You've got {lives} tries left.")

    placeholder = ""

    for letter in chosen_word:
        if letter in correct_letters:
            placeholder += letter
        else:
            placeholder += "_"
    print("Word: " + placeholder)

    guess = input("Guess a letter: \n").lower()

    while guess in all_guessed_letters:
        print("you've guessed this letter already")
        print("Word: " + placeholder)
        print(stages[lives])
        print(f"You've got {lives} tries left.")
        guess = input("Guess a letter: \n").lower()

    all_guessed_letters.append(guess)
    if guess in chosen_word:
        correct_letters.append(guess)
        print("Nice! You got a letter.")
    else:
        print("Ouch! Wrong letter.")
        lives -= 1

    if "_" not in placeholder:
        print("You won! The word was:", chosen_word)
        game_over = True

    if lives == 0:
        print(stages[lives])
        print("You died - game over")
        print("The correct word was:", chosen_word)
        game_over = True
