from random import choice
from os import system
from time import sleep
import sys
import re
import json

game_stats = {
    'Deck': {
        'Hearts': {
            2: 2, 3: 3, 4: 4,
            5: 5, 6: 6, 7: 7,
            8: 8, 9: 9, 10: 10,
            'Jack': 10, 'Queen': 10,
            'King': 10, 'Ace': [1, 11]
        },
        'Diamonds': {
            2: 2, 3: 3, 4: 4,
            5: 5, 6: 6, 7: 7,
            8: 8, 9: 9, 10: 10,
            'Jack': 10, 'Queen': 10,
            'King': 10, 'Ace': [1, 11]
        },
        'Clubs': {
            2: 2, 3: 3, 4: 4,
            5: 5, 6: 6, 7: 7,
            8: 8, 9: 9, 10: 10,
            'Jack': 10, 'Queen': 10,
            'King': 10, 'Ace': [1, 11]
        },
        'Spades': {
            2: 2, 3: 3, 4: 4,
            5: 5, 6: 6, 7: 7,
            8: 8, 9: 9, 10: 10,
            'Jack': 10, 'Queen': 10,
            'King': 10, 'Ace': [1, 11]
        }
    },
    'User': {
        'Score': 0,
        'Cards': [],
        'turn': True
    },
    'Dealer': {
        'Score': 0,
        'Cards': [],
        'Hidden_card': 0
    }
}

END_OF_GAME = 21

with open('./game_messages.json', encoding="utf-8") as file:
    game_messages = json.load(file)

def typing_effect(message, time = 0.02):
    for char in message:
        print(char, end='', flush=True)
        sleep(time)
        if char == ',':
            sleep(0.10)
        if char == '.':
            sleep(0.70)
    return '\n'

def remove_end_of_line_empty_spaces(message):
    msg = message.split(' ')
    msg[-1] = ''
    message = ' '.join(msg)

    return message

# makes sure the messages from the json file are no longer than 80 lines
def add_newlines_to_msgs(messages):
    for key in messages:

        new_message = ''
        multiplyer = 1
        message_list = messages[key].split(' ')

        for word in message_list:
            new_message += word + ' '
            multiple_of_80 = 80 * multiplyer

            if len(new_message) > multiple_of_80:

                if new_message[-1] == ' ':
                    new_message = remove_end_of_line_empty_spaces(new_message)

                new_message += '\n'
                multiplyer += 1

        messages[key] = new_message
    return messages

game_messages = add_newlines_to_msgs(game_messages)

def determine_ace_value(ace_values, player_turn):
    one = ace_values[0]
    eleven = ace_values[1]

    current_score = (game_stats['User']['Score']
                     if player_turn else game_stats['Dealer']['Score'])

    return one if current_score + eleven > END_OF_GAME else eleven

def remove_suits_without_cards(suits):
    for suit in suits:
        if game_stats['Deck'].get(suit) == {}:
            suits.remove(suit)
            del game_stats['Deck'][suit]

    return suits

def remove_card_from_deck(suit, card_key, card):

    if card_key == 'Ace':
        ace_list = game_stats['Deck'][suit][card_key]
        ace_list.remove(card)
        if not ace_list:
            del game_stats['Deck'][suit][card_key]
            return

    del game_stats['Deck'][suit][card_key]

def get_card_value(card_key, suit):
    card_value = game_stats['Deck'][suit][card_key]
    if card_key == 'Ace':
        card_value = determine_ace_value(card_value,
                                         game_stats['User']['turn'])
    return card_value

def draw_card(start_of_game):
    deal_amount = 2 if start_of_game else 1
    cards = []
    current_turn = 'User' if game_stats['User']['turn'] else 'Dealer'

    while deal_amount > 0:

        all_suits = list(game_stats['Deck'].keys())
        remaining_suits = remove_suits_without_cards(all_suits)
        suit = choice(remaining_suits)

        card_key = choice(list(game_stats['Deck'][suit].keys()))
        game_stats[current_turn]['Cards'].append(card_key)

        card_value = get_card_value(card_key, suit)
        cards.append(card_value)

        remove_card_from_deck(suit, card_key, card_value)
        deal_amount -= 1

    return cards

def player_hit_or_stay(start_of_game,
                       msg = 'Player would you like to (Hit/h) or (Stay/s)? ',
                       time = 1):
    sleep(time)
    response = input(msg)
    system('clear')
    if response in ('Hit', 'H', 'hit', 'h'):
        return draw_card(start_of_game)
    if response in ('Stay', 'S', 'stay', 's'):
        return [0]

    return player_hit_or_stay(start_of_game,
                              'Please Enter (hit/h) or (stay/s): ',
                               0)

def dealer_hit_under_17(start_of_game):
    target = 17
    dealer_score = game_stats['Dealer']['Score']

    if dealer_score < target:
        return draw_card(start_of_game)

    return [0]

def update_score(user_turn, card_value):
    if user_turn:
        game_stats['User']['Score'] += sum(card_value)
        return

    game_stats['Dealer']['Score'] += sum(card_value)
    return

# uses correct word (a or an) before card depending if card starts with vowel
def starts_with_vowel(card):
    if isinstance(card, str):
        if card[0] in 'aeiouAEIOU' or card[0] == 8:
            return 'an'
    return 'a'

def display_card_message(card_keys, player_turn):

    player = 'User' if player_turn else 'Dealer'
    cards = game_stats[player]['Cards']

    drew = f'drew {starts_with_vowel(card_keys[0])}'

    card_msg = ''

    for i, card in enumerate(cards):
        if player == 'Dealer' and i == 1:
            game_stats[player]['Hidden_card'] = card
            card_msg += 'and an unknown card'
            continue
        if player == 'Dealer' and i == 2:
            card_msg += ', '
        if i < len(cards) - 1:
            card_msg += str(card) + ', '
        else:
            card_msg += str(card)

    if player == 'User':
        print(f'You {drew} {card_msg}\n')
    else:
        phrase = ', and an unknown card'
        if phrase in card_msg:
            card_msg = re.sub(phrase, '', card_msg)
            card_msg += phrase

        print(f'{player} {drew} {card_msg}\n')

def check_for_stay(card_value, stays, current_player):
    if 0 in card_value:
        stays.append(current_player)

def determine_winner():
    user_score = game_stats['User']['Score']
    dealer_score = game_stats['Dealer']['Score']

    if dealer_score > END_OF_GAME and user_score > END_OF_GAME:
        return 'Both of you bust. No winner!'
    if user_score > END_OF_GAME:
        return "That's a Bust. Dealer wins!"
    if dealer_score > END_OF_GAME:
        return 'Dealer Busts. You win!'

    if dealer_score == user_score:
        return 'Tie game!'
    if user_score > dealer_score:
        return 'You win!'

    return 'Dealer wins!'

# cool loading effect before displaying dealers hidden card
def display_hidden_card():
    typing_effect('The dealers hidden card was ')
    for _ in range(3):
        typing_effect('...', 0.08)
        sleep(0.2)
        # Move cursor back 3 positions
        sys.stdout.write("\033[3D")
        # Clear from cursor position to end of line
        sys.stdout.write("\033[0K")
        # forces output. For this case it could work without
        sys.stdout.flush()

def display_winner(winner):
    game_info = [[game_stats[player][stat]] for player in game_stats
                                            for stat in game_stats[player]
                                            if stat != 'turn']

    player_score, _, dealer_score, _, dealer_hidden_card = game_info

    hidden_card_msg = ''

    card = dealer_hidden_card[0]
    hidden_card_msg = f'{starts_with_vowel(card)}: {dealer_hidden_card[0]}'

    msg = (f'{winner} The score was '
           f'{player_score[0]} to {dealer_score[0]}.')

    display_hidden_card()
    print(f'{typing_effect(hidden_card_msg, 0.06)}\n{msg} \n')

def play_twenty_one():
    system('clear')
    msg = "Here we go. We're going to deal you your first two cards!\n\n"
    typing_effect(msg)

    beginning_of_game = True
    two_stays = []
    card_values = 0

    while (game_stats['User']['Score'] < END_OF_GAME and
           game_stats['Dealer']['Score'] < END_OF_GAME):

        if len(two_stays) == 2:
            break

        game_stats['User']['turn'] = True
        user_turn = game_stats['User']['turn']

        if 'User' not in two_stays:
            if beginning_of_game:
                card_values = draw_card(beginning_of_game)
            else:
                card_values = player_hit_or_stay(beginning_of_game)

            check_for_stay(card_values, two_stays, 'User')
            card_keys = game_stats['User']['Cards']
            display_card_message(card_keys, user_turn)
            update_score(user_turn, card_values)

        sleep(1)

        card_keys = game_stats['Dealer']['Cards']
        game_stats['User']['turn'] = False
        user_turn = game_stats['User']['turn']

        if 'Dealer' not in two_stays:
            card_values = dealer_hit_under_17(beginning_of_game)
            check_for_stay(card_values, two_stays, 'Dealer')

            display_card_message(card_keys, user_turn)
            update_score(user_turn, card_values)
            beginning_of_game = False

    results = determine_winner()
    return results

def how_to_play():
    goal, setup, deck, card_values = (game_messages[key]
                                      for key in game_messages)
    msg = (f"{goal}\n\n{setup}\n\n{deck}\n\n{card_values}\n\n")
    typing_effect(msg)
    sleep(1)
    system('clear')

def restart_game(msg = 'Do you want to play again?'):
    typing_effect(msg)
    typing_effect('\nEnter yes/y or no/n: ')
    response = input()
    if response in ('Yes', 'Y', 'yes', 'y'):
        reset_game_obj()
        return start_game()
    if response in ('No', 'N', 'no', 'n'):
        return typing_effect('\nThank you for playing!\n')
    system('clear')
    return restart_game('That input is not valid.')

def reset_game_obj():
    global game_stats
    game_stats = {
        'Deck': {
            'Hearts': {
                2: 2, 3: 3, 4: 4,
                5: 5, 6: 6, 7: 7,
                8: 8, 9: 9, 10: 10,
                'Jack': 10, 'Queen': 10,
                'King': 10, 'Ace': [1, 11]
            },
            'Diamonds': {
                2: 2, 3: 3, 4: 4,
                5: 5, 6: 6, 7: 7,
                8: 8, 9: 9, 10: 10,
                'Jack': 10, 'Queen': 10,
                'King': 10, 'Ace': [1, 11]
            },
            'Clubs': {
                2: 2, 3: 3, 4: 4,
                5: 5, 6: 6, 7: 7,
                8: 8, 9: 9, 10: 10,
                'Jack': 10, 'Queen': 10,
                'King': 10, 'Ace': [1, 11]
            },
            'Spades': {
                2: 2, 3: 3, 4: 4,
                5: 5, 6: 6, 7: 7,
                8: 8, 9: 9, 10: 10,
                'Jack': 10, 'Queen': 10,
                'King': 10, 'Ace': [1, 11]
            }
        },
        'User': {
            'Score': 0,
            'Cards': [],
            'turn': True
        },
        'Dealer': {
            'Score': 0,
            'Cards': [],
            'Hidden_card': 0
        }
    }

def start_game():
    game_results = play_twenty_one()
    display_winner(game_results)
    restart_game()

def initialize_game():
    # if you dont want to wait for rules of the game to display
    # comment out line below
    how_to_play()
    start_game()

initialize_game()
