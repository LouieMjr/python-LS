from time import sleep
from os import system
from random import choice
import json

def open_json():
    with open('./rps_messages.json', 'r') as file:
        return json.load(file)

RPS_MSG = open_json()

def delay(time):
    sleep(time)

def print_with_typing_effect(message):
    for char in message:
        print(char, end='', flush=True)
        delay(0.02)

def get_user_choice(msg = RPS_MSG['choices']):
    print_with_typing_effect(msg)
    user_choice = input()

    user_choice = valid_choice(user_choice)
    while user_choice is False:
        return get_user_choice(RPS_MSG['simplified_choices'])

    return user_choice

def valid_choice(user_pick, choices = 
    {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }):
    
    try:
        user_pick = user_pick[0].upper()
        if user_pick in choices:
            system('clear')
            user_pick = choices[user_pick]
            if user_pick == 'Yes' or user_pick == 'No':
                return user_pick
            print_with_typing_effect('You picked: ' + user_pick + '\n')
            return user_pick

        system('clear')
        print_with_typing_effect(RPS_MSG['invalid'])
        return False
    except (IndexError, KeyError):
        system('clear')
        print_with_typing_effect(RPS_MSG['invalid'])
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
        draw = f'{RPS_MSG['draw']} {player_choice}!'
        print_with_typing_effect(draw + '\n')
        return

    for combo in winning_combinations:
        if [player_choice, computer_choice] == combo:
            win = f'{RPS_MSG['winner']}{player_choice} beats {computer_choice}!'
            print_with_typing_effect(win + '\n')
            return
    lose = f'{RPS_MSG['loser']}{computer_choice} beats {player_choice}!'
    print_with_typing_effect(lose + '\n')

def restart_game(msg = RPS_MSG['restart_rps']):
    delay(0.5)
    print_with_typing_effect(msg)
    response = input()

    options = {
        "N": "No",
        "Y": "Yes",
    }

    choice = valid_choice(response, options)

    match choice:
        case 'Yes':
            return play_rps('Here we go!\n')
        case 'No':
            print_with_typing_effect(RPS_MSG['thank_player'])
        case False:
            return restart_game(RPS_MSG['restart_options'])

def play_rps(msg = f'{RPS_MSG['welcome']}{RPS_MSG['rules']}'):
    print_with_typing_effect(msg)

    delay(0.5)
    print_with_typing_effect("Player, you pick first...")
    user_pick = get_user_choice()

    print_with_typing_effect("Computer, picks next...\n")
    delay(1.4)
    computer_pick = computer_selection()

    rps_game_logic(user_pick, computer_pick)
    restart_game()

play_rps()