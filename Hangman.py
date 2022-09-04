words = ['panda', 'is', 'the', 'best', 'rapper', 'alive', 'no', 'cap', 'and', 'it', 'is', 'my', 'hope', 'that', 'he', 'makes', 'it', 'in the', 'world-2', 'have', 'fun', 'dear']
import random
import string

def get_valid_words(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input('Guess your letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print('You have already guessed that letter. Please try again')
        else:
            print('Your guess is invalid')
    
    if lives == 0:
        print('You have died')
    else:
        print('You have guessed the word, ',' '.join(word))

hangman() 