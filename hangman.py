import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    print('word', word)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # disply letters used
        print('You have', lives, 'lives and you have used these letters: ', ' '.join(used_letters))

        #what the current word is ie( W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:  # if the user's input is a valid alphabet character and it has been guessed/used yet
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 #takes away a life if wrong
                print('Letter is not in word')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again')
        
        else:
            print('Invalid character. Please try again')

    if lives == 0 :
        print('You have died, sorry. The word was', word)
    else:
        print('You have guessed the word', word)

hangman()