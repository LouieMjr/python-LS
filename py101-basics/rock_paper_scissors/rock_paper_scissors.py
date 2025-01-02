# winning scenarios

# rock:
# rock > scissor

# paper:
# paper > rock

# scissors:
# scissors > paper
from time import sleep
from os import system
from random import choice

def delay(time):
    sleep(time)

def print_with_typing_effect(message):
    for char in message:
        print(char, end='', flush=True)
        delay(0.02)

def get_user_choice(msg = 'Make your selection: Rock(r), Paper(p), Scissors(s): '):
    print_with_typing_effect(msg)
    user_choice = input()

    user_choice = valid_choice(user_choice)
    while user_choice == False:
        return get_user_choice('\nRock(r), Paper(p), Scissors(s): ')

    return user_choice


def valid_choice(user_pick):
    user_pick = user_pick.upper()

    choices = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }

    try:
        if user_pick[0] in choices:
            system('clear')
            user_pick = choices[user_pick]
            print_with_typing_effect('You picked: ' + user_pick + '\n')
            return user_pick
        else:
            system('clear')
            print_with_typing_effect('This selection is not a valid one.\nPlease pick one of the choices we suggest!\n')
            return False
    except IndexError:
        system('clear')
        print_with_typing_effect('This selection is not a valid one.\nPlease pick one of the choices we suggest!\n')
        return False

def computer_choice():
    
computer_choice()