import random

user = input('What is your choice?\nrock(r), paper(p), or scissors(s): ')
computer = random.choice(['r', 'p', 's'])

def play():
    if user == computer:
        return 'Its a tie'
    elif is_win(user, computer):
        return 'You win'
    
    return 'You Lost'

def is_win(player, opponent):
    # r>p, p>s, s>r
    if(player == 'r' and opponent == 'p') or (player == 'p' and opponent == 's') or (player == 's' and opponent == 'r'):
        return True

print(play())