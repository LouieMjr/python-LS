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
    while user_choice is False:
        return get_user_choice('\nRock(r), Paper(p), Scissors(s): ')

    return user_choice

def valid_choice(user_pick):
    choices = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }

    try:
        user_pick = user_pick[0].upper()
        if user_pick in choices:
            system('clear')
            user_pick = choices[user_pick]
            print_with_typing_effect('You picked: ' + user_pick + '\n')
            return user_pick

        system('clear')
        print_with_typing_effect('This selection is not a valid one.\nPlease pick one of the choices we suggest!\n')
        return False
    except (IndexError, KeyError):
        system('clear')
        print_with_typing_effect('This selection is not a valid one.\nPlease pick one of the choices we suggest!\n')
        return False

def computer_selection():
    computer_pick = choice(['Rock', 'Paper', 'Scissors'])
    print_with_typing_effect(f'The computer chose {computer_pick}\n')
    return computer_pick

def rps_game_logic(player_choice, computer_choice):
    winning_combinations = [
        ['Rock' , 'Scissors'],
        ['Paper' , 'Rock'],
        ['Scissors' , 'Paper']
    ]

    if player_choice == computer_choice:
        print_with_typing_effect(f'\nDraw! You both picked {player_choice}!\n')
        return

    for combo in winning_combinations:
        if [player_choice, computer_choice] == combo:
            print_with_typing_effect(f'\nYou win!\n{player_choice} beats {computer_choice}!\n')
            return
    print_with_typing_effect(f'\nYou lose!\n{computer_choice} beats {player_choice}!\n')

def play_rps():
    print_with_typing_effect("Welcome to Rock, Paper, Scissors Shoot.\nThis is a fun game and can get extremely intense!\nHere is how we determine a winner:\n\n(Rock beats Scissors), (Paper beats Rock), (Scissors beats Paper).\n\nThose are the winning combinations!\nLet's get started!\n\n")

    delay(0.5)
    print_with_typing_effect("Player, you pick first...")
    user_pick = get_user_choice()

    print_with_typing_effect("Computer, picks next...\n")
    delay(1.4)
    computer_pick = computer_selection()

    rps_game_logic(user_pick, computer_pick)

play_rps()