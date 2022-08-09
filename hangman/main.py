from ast import If
import random
import string
from words import words

word = random.choice(words).upper()

def hangman(word):
  lives = 6

  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  while len(word_letters) > 0 and lives > 0:
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else: 
        lives = lives - 1
        print(f"you have {lives} lives")
    elif user_letter in used_letters:
      print("You've already guessed this letter!")
    else: print('Invalid character')
    print(' ')
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('used letters: ', ' '.join(used_letters))
    print('Current word: ', ' '.join(word_list))
    #end of the while (word_letters == 0)
  if lives == 0:
    print("Sorry, you died. The word was ", word)
  else:
    print("Congratulations, you guessed the word ", word)
hangman(word)