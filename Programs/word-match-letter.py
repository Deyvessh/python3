# Step 1

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.


chosen_word = random.choice(word_list)

# list_word = list(chosen_word) # doesn't need this
print(chosen_word)              # doesn't need this


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter in the word: ").lower()  

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


for letter in chosen_word:
    if guess == letter:      # letter == guess
        print("Right")
    else:
        print("Wrong")
      
    
