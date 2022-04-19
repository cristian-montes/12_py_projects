import random

def play():
    user = input(" 'r' for ROCK, 'p' for paper, 's' for scissorts ")
    computer_choice = random.choice(['r', 'p', 's'])

    if user == computer_choice:
        return 'tie'

    if is_win(user, computer_choice):
        return 'You Won!'
    
    return 'You lost'

def is_win(player, opponent):
    if( player == 'r' and opponent == 's') or (player == 's' and opponent == 'p' ) \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())