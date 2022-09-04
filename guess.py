import random
from re import X

#User guess
#def user_guess(x):
#    random_number = random.randint(1, x)
#    guess = 0
#    while guess != random_number:
#        guess = int(input('Guess the lucky number: '))
#        if guess > random_number:
#            print('Too high')
#        elif guess < random_number:
#            print('Too low')
#    print(f'Congrats, You have guessed the number {guess} correctly!!')

#user_guess(10)

#Computer guess
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'Is the guess number {guess} too high(H), too low(L), or correct(C)?').lower()
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
    
    print('Yay, the computer guessed the correct number!!')
    
computer_guess(10)
