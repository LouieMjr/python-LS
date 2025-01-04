from time import sleep
from os import system
from random import choice
import json

def open_json():
    with open('./rps_messages.json', 'r') as file:
        return json.load(file)

RPS_MSG = open_json()

RPS_CHOICES = {
    "R": "Rock",
    "P": "Paper",
    "SC": "Scissors",
    "L": "Lizard",
    "SP": "Spock"
}

WINNING_COMBOS = {
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

SCORE = {
    "player": 0,
    "computer": 0
}

def print_with_typing_effect(message):
    for char in message:
        print(char, end='', flush=True)
        sleep(0.02)

def get_user_choice(msg = RPS_MSG['options']):
    print_with_typing_effect(msg)
    user_choice = input()

    user_choice = valid_choice(user_choice)
    options = RPS_MSG['simplified_options']
    return user_choice if user_choice else get_user_choice(options)

def valid_choice(user_pick, choices = RPS_CHOICES):
    try:
        user_pick = user_pick.upper()
        if 'SC' in user_pick or 'SP' in user_pick:
            user_pick = user_pick[:2]
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
    computer_pick = choice(list(RPS_CHOICES.values()))
    print_with_typing_effect(f'The computer chose {computer_pick}\n')
    return computer_pick

def decide_winner_update_score(user_pick, comp_pick, winning_combos, score):

    battle_msg = None
    combo = (user_pick, comp_pick)

    if combo in winning_combos:
        score["player"] += 1
        battle_msg = f'{RPS_MSG['winner']}{winning_combos[combo]}!'
    elif user_pick == comp_pick:
        battle_msg = f'{RPS_MSG['draw']} {user_pick}!'
    else:
        combo = (comp_pick, user_pick)
        score["computer"] += 1
        battle_msg = f'{RPS_MSG['loser']}{winning_combos[combo]}!'

    return [score, battle_msg + '\n']

def restart_game(msg = RPS_MSG['restart_rps']):
    sleep(0.5)
    print_with_typing_effect(msg)
    response = input()
    selection = valid_choice(response, {"N": "No", "Y": "Yes"})

    match selection:
        case 'Yes':
            return start_game('Here we go!\n')
        case 'No':
            print_with_typing_effect(RPS_MSG['thank_player'])
        case False:
            return restart_game(RPS_MSG['valid_restart_options'])

MSG = f'{RPS_MSG['best_of_five_msg']}{RPS_MSG['best_of_five_options']}'
def best_of_five(msg = MSG):

    print_with_typing_effect(msg)
    response = input()
    games_to_play = valid_choice(response, {"1": "1", "5": "5"})

    if games_to_play is False:
        return best_of_five('\n' + RPS_MSG['best_of_five_options'])

    return int(games_to_play)

def display_score_msg(user_score, comp_score):
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
    sleep(0.5)
    print_with_typing_effect("Player, you pick first...")
    user_choice = get_user_choice()

    print_with_typing_effect("Computer, picks next...\n")
    sleep(1.4)
    computer_choice = computer_selection()
    parameters = [user_choice, computer_choice, WINNING_COMBOS, SCORE]
    return decide_winner_update_score(*parameters)

def start_game(msg = f'{RPS_MSG['welcome']}{RPS_MSG['rules']}'):
    print_with_typing_effect(msg)
    games_to_play = best_of_five()

    if games_to_play == 1:
        msg = f'{games_to_play} game!\nWinner takes all!\n\n'
        print_with_typing_effect(msg)
        _, battle_msg = gameplay()
        print_with_typing_effect(battle_msg)
    else:
        print_with_typing_effect(RPS_MSG['best_of_five_rules'])
        player_score = 0
        computer_score = 0

        while (player_score < 3 and computer_score < 3):
            score, battle_msg = gameplay()

            player_score = score['player']
            computer_score = score['computer']

            print_with_typing_effect(battle_msg)
            sleep(0.6)
            display_score_msg(player_score, computer_score)

    SCORE["computer"] = 0
    SCORE["player"] = 0
    restart_game()

start_game()