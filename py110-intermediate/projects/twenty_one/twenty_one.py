from random import choice
from os import system
from time import sleep
import sys
import re
import json

DECK = {
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
    },
}

GAME_STATS = {
    'User': {
        'Score': 0,
        'Cards': [],
        'turn': True
    },
    'Dealer': {
        'Score': 0,
        'Cards': [],
        'Hidden_card': 0
    },
}

BEGINNING_OF_GAME = True

with open('./game_messages.json', encoding="utf-8") as file:
    MESSAGES = json.load(file)

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

def add_newlines_to_msgs(messages):
    for key in messages:

        new_message = ''
        multiple_of_80 = 1
        message_list = messages[key].split(' ')

        for word in message_list:
            new_message += word + ' '

            if len(new_message) > 80 * multiple_of_80:

                if new_message[-1] == ' ':
                    new_message = remove_end_of_line_empty_spaces(new_message)

                new_message += '\n'
                multiple_of_80 += 1

        messages[key] = new_message
    return messages

MESSAGES = add_newlines_to_msgs(MESSAGES)

def determine_ace_value(ace_values, player_turn):
    one = ace_values[0]
    eleven = ace_values[1]

    current_score = (GAME_STATS['User']['Score']
                     if player_turn else GAME_STATS['Dealer']['Score'])

    return one if current_score + eleven > 21 else eleven

def remove_suits_without_cards(suits):
    for suit in suits:
        if DECK.get(suit) == {}:
            suits.remove(suit)
            del DECK[suit]

    return suits

def remove_card_from_deck(suit, card_key, card):

    if card_key == 'Ace':
        ace_list = DECK[suit][card_key]
        ace_list.remove(card)
        if not ace_list:
            del DECK[suit][card_key]
            return

    del DECK[suit][card_key]

def get_card_value(card_key, suit):
    card_value = DECK[suit][card_key]
    if card_key == 'Ace':
        card_value = determine_ace_value(card_value,
                                         GAME_STATS['User']['turn'])
    return card_value

def draw_card():
    deal_amount = 2 if BEGINNING_OF_GAME else 1
    cards = []
    current_turn = 'User' if GAME_STATS['User']['turn'] else 'Dealer'

    while deal_amount > 0:

        all_suits = list(DECK.keys())
        remaining_suits = remove_suits_without_cards(all_suits)
        suit = choice(remaining_suits)

        card_key = choice(list(DECK[suit].keys()))
        GAME_STATS[current_turn]['Cards'].append(card_key)

        card_value = get_card_value(card_key, suit)
        cards.append(card_value)

        remove_card_from_deck(suit, card_key, card_value)
        deal_amount -= 1

    return cards

def player_hit_or_stay(msg = 'Player would you like to (Hit/h) or (Stay/s)? ',
                       time = 1):
    sleep(time)
    response = input(msg)
    system('clear')
    if response in ('Hit', 'H', 'hit', 'h'):
        return draw_card()
    if response in ('Stay', 'S', 'stay', 's'):
        return [0]

    return player_hit_or_stay('Please Enter (hit/h) or (stay/s): ', 0)

def dealer_hit_under_17():
    target = 17
    dealer_score = GAME_STATS['Dealer']['Score']

    if dealer_score < target:
        return draw_card()

    return [0]

def update_score(user_turn, card_value):
    if user_turn:
        GAME_STATS['User']['Score'] += sum(card_value)
        return

    GAME_STATS['Dealer']['Score'] += sum(card_value)
    return

def starts_with_vowel(card):
    if isinstance(card, str):
        if card[0] in 'aeiouAEIOU' or card[0] == 8:
            return 'an'
    return 'a'

def display_card_message(card_keys, player_turn):

    player = 'User' if player_turn else 'Dealer'
    cards = GAME_STATS[player]['Cards']

    drew = f'drew {starts_with_vowel(card_keys[0])}'

    card_msg = ''

    for i, card in enumerate(cards):
        if player == 'Dealer' and i == 1:
            GAME_STATS[player]['Hidden_card'] = card
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
    user_score = GAME_STATS['User']['Score']
    dealer_score = GAME_STATS['Dealer']['Score']

    if dealer_score > 21 and user_score > 21:
        return 'Both of you bust. No winner!'
    if user_score > 21:
        return "That's a Bust. Dealer wins!"
    if dealer_score > 21:
        return 'Dealer Busts. You win!'

    if dealer_score == user_score:
        return 'Tie game!'
    if user_score > dealer_score:
        return 'You win!'

    return 'Dealer wins!'

def display_hidden_card():
    typing_effect('The dealers hidden card was ')
    for _ in range(3):
        typing_effect('...', 0.10)
        sleep(0.2)
        sys.stdout.write("\033[3D") # Move cursor back 3 positions
        sys.stdout.write("\033[0K") # Clear from cursor position to end of line
        sys.stdout.flush() # forces output but for this case it will work without

def display_winner(winner):
    game_info = [[GAME_STATS[player][stat]] for player in GAME_STATS
                                            for stat in GAME_STATS[player]
                                            if stat != 'turn']

    player_score, _, dealer_score, _, dealer_hidden_card = game_info

    hidden_card_msg = ''

    card = dealer_hidden_card[0]
    hidden_card_msg = f'{starts_with_vowel(card)}: {dealer_hidden_card[0]}'

    msg = (f'{winner} The score was '
           f'{player_score[0]} to {dealer_score[0]}.')

    display_hidden_card()
    print(f'{typing_effect(hidden_card_msg, 0.06)}\n{msg} ')

def play_twenty_one():
    global BEGINNING_OF_GAME
    two_stays = []
    card_values = 0

    while (GAME_STATS['User']['Score'] < 21 and
           GAME_STATS['Dealer']['Score'] < 21):

        if len(two_stays) == 2:
            break

        GAME_STATS['User']['turn'] = True
        user_turn = GAME_STATS['User']['turn']

        if 'User' not in two_stays:
            card_values = player_hit_or_stay()
            check_for_stay(card_values, two_stays, 'User')

        card_keys = GAME_STATS['User']['Cards']
        display_card_message(card_keys, user_turn)
        update_score(user_turn, card_values)

        sleep(1)

        card_keys = GAME_STATS['Dealer']['Cards']
        GAME_STATS['User']['turn'] = False
        user_turn = GAME_STATS['User']['turn']

        if 'Dealer' not in two_stays:
            card_values = dealer_hit_under_17()
            check_for_stay(card_values, two_stays, 'Dealer')

        display_card_message(card_keys, user_turn)
        update_score(user_turn, card_values)
        BEGINNING_OF_GAME = False

    results = determine_winner()
    return results

def how_to_play():
    goal, setup, deck, card_values = (MESSAGES[key] for key in MESSAGES)
    print(f'{goal}\n\n{setup}\n\n{deck}\n\n{card_values}\n')

def initialize_game():
    how_to_play()
    game_results = play_twenty_one()
    return display_winner(game_results)

print(initialize_game())
