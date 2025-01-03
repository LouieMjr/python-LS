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
        "SC": "Scissors",
        "L": "Lizard",
        "SP": "Spock"
    }):

    try:
        user_pick = user_pick.upper()
        if 'SC' in user_pick or 'SP' in user_pick:
            user_pick = user_pick[0:2]
        else:
            user_pick = user_pick[0]

        if user_pick in choices:
            system('clear')
            user_pick = choices[user_pick]
            if user_pick in ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']:
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
    computer_pick = choice(['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock'])
    print_with_typing_effect(f'The computer chose {computer_pick}\n')
    return computer_pick

def rps_game_logic(player_choice, computer_choice):
    winning_combos = {
        ("Paper" , "Spock"): "Paper disproves Spock",
        ("Paper" , "Rock"): "Paper covers Rock",
        ("Rock" , "Lizard"): "Rock crushes Lizard",
        ("Rock" , "Scissors"): "Rock crushes Scissors",
        ("Scissors" , "Paper"): "Scissors cuts Paper",
        ("Scissors" , "Lizard"): "Scissors decapitates Lizard",
        ("Lizard" , "Paper"): "Lizard eats Paper",
        ("Lizard" , "Spock"): "Lizard poisons Spock",
        ("Spock", "Rock"): "Spock vaporizes Rock",
        ("Spock", "Scissors"): "Spock smashes Scissors"
    }

    score = {
        "player": 0,
        "computer": 0
    }

    if player_choice == computer_choice:
        draw = f'{RPS_MSG['draw']} {player_choice}!'
        print_with_typing_effect(draw + '\n')
        return score

    battle_msg = None
    combo = (player_choice, computer_choice)

    if combo in winning_combos:
        score["player"] += 1
        battle_msg = f'{RPS_MSG['winner']}{winning_combos[combo]}!'
    else:
        combo = (computer_choice, player_choice)
        score["computer"] += 1
        battle_msg = f'{RPS_MSG['loser']}{winning_combos[combo]}!'

    print_with_typing_effect(battle_msg + '\n')
    return score

def restart_game(msg = RPS_MSG['restart_rps']):
    delay(0.5)
    print_with_typing_effect(msg)
    response = input()

    options = {
        "N": "No",
        "Y": "Yes",
    }

    selection = valid_choice(response, options)

    match selection:
        case 'Yes':
            return start_game('Here we go!\n')
        case 'No':
            print_with_typing_effect(RPS_MSG['thank_player'])
        case False:
            return restart_game(RPS_MSG['valid_restart_options'])

def best_of_five(msg = f'{RPS_MSG['best_of_five_msg']}{RPS_MSG['best_of_five_options']}'):

    print_with_typing_effect(msg)
    response = input()

    options = {
        "1": "1",
        "5": "5"
    }

    games_to_play = valid_choice(response, options)
    if games_to_play is False:
        return best_of_five('\n' + RPS_MSG['best_of_five_options'])

    return int(games_to_play)

def score_logic(user_score, comp_score):
    msg = None
    if user_score == comp_score:
        msg = f'The score is tied: {user_score} to {comp_score}\n\n'
    if user_score > comp_score:
        msg = f"You're winning: {user_score} to {comp_score}\n\n"
    if user_score < comp_score:
        msg = f"You're losing: {user_score} to {comp_score}\n\n"
    if user_score == 3:
        msg = f"You won the Game! {user_score} to {comp_score}\n\n"
    if comp_score == 3:
        msg = f"Computer won the Game! {user_score} to {comp_score}\n\n"

    print_with_typing_effect(msg)

def gameplay():
    delay(0.5)
    print_with_typing_effect("Player, you pick first...")
    user_pick = get_user_choice()

    print_with_typing_effect("Computer, picks next...\n")
    delay(1.4)
    computer_pick = computer_selection()

    return rps_game_logic(user_pick, computer_pick)

def start_game(msg = f'{RPS_MSG['welcome']}{RPS_MSG['rules']}'):
    print_with_typing_effect(msg)

    games_to_play = best_of_five()

    if games_to_play == 1:
        msg = f'{games_to_play} game!\nWinner takes all!\n\n'
        print_with_typing_effect(msg)
        gameplay()
    else:
        player_score = 0
        computer_score = 0
        print_with_typing_effect(RPS_MSG['best_of_five_rules'])
        while (player_score < 3 and computer_score < 3):
            score = gameplay()
            delay(0.6)

            player_score += score['player']
            computer_score += score['computer']

            score_logic(player_score, computer_score)

    restart_game()

start_game()