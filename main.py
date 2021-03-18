import random


def play():
    user = input("What's your choice \n 'r' for rock"
                 "or 's' for scissors or 'p' for paper :")


    computer = random.choice(['r', 'p','s'])
    print("computer's choice is " + computer)
    if user == computer:
        return "it's a tie"

    if is_win(user, computer):
        return "you win"

    return "you lost"

def is_win(player, opponent):
    # return true if player wins
    # s>p , p>r , r>s
    if (player == 's' and opponent=='p') or (player == 'p' and opponent =='r') or (player =='r' and opponent== 's'):
        return True

print (play())
