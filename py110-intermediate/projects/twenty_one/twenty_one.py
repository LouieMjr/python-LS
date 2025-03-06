from random import choice
from os import system
from time import sleep
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

SCORE = {
    'User': 0,
    'Dealer': 0
}

BEGINNING_OF_GAME = True

with open('./game_messages.json', encoding="utf-8") as file:
    MESSAGES = json.load(file)

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

    current_score = SCORE['User'] if player_turn else SCORE['Dealer']

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
        card_value = determine_ace_value(card_value, SCORE['User_turn'])
    return card_value

def draw_card():
    draw_amount = 2 if BEGINNING_OF_GAME else 1
    cards = []

    while draw_amount > 0:

        all_suits = list(DECK.keys())
        remaining_suits = remove_suits_without_cards(all_suits)
        suit = choice(remaining_suits)

        card_key = choice(list(DECK[suit].keys()))
        cards.append(card_key)
        card = get_card_value(card_key, suit)
        cards.append(card)

        remove_card_from_deck(suit, card_key, card)
        draw_amount -= 1

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
    dealer_score = SCORE['Dealer']

    if dealer_score < target:
        return draw_card()

    return [0]

def score_over_twenty_one(score):
    if score > 21:
        return True
    return False

def update_score(user_turn, card_value):

    if user_turn:
        SCORE['User'] += card_value
        return

    SCORE['Dealer'] += card_value
    return

def display_current_card(card, player_turn):
    player = None
    if card > 1:
        if player_turn:
            player = 'You'
        else:
            player = 'Dealer'

        return f'{player} drew a {card}.\n'
    return ''

def check_for_stay(card_value, stays):
    if card_value == 0:
        stays.append(True)

def determine_winner():
    user_score = SCORE['User']
    dealer_score = SCORE['Dealer']

    if dealer_score == user_score:
        return [user_score, dealer_score, 'Tie game!']
    if user_score > dealer_score:
        return [user_score, dealer_score, 'Player wins!']

    return [user_score, dealer_score, 'Dealer wins!']

def display_winner(game_info):
    user_score, dealer_score, winner = game_info
    print(f'{winner} With a score of {user_score} to {dealer_score}')

def play_twenty_one():

    while SCORE['User'] < 21 and SCORE['Dealer'] < 21:

        SCORE['User_turn'] = True
        user_turn = SCORE['User_turn']
        two_stays_in_same_turn = []

        card_value = player_hit_or_stay()
        display_card = display_current_card(card_value, SCORE['User_turn'])
        check_for_stay(card_value, two_stays_in_same_turn)
        update_score(user_turn, card_value)

        user_turn = not user_turn
        SCORE['User_turn'] = user_turn

        print((
            f'{display_card}'
            f'Your current total is: {SCORE['User']}\n'
        ))

        if score_over_twenty_one(SCORE['User']):
            return "That's Bust. Dealer wins!"

        sleep(1)

        card_value = dealer_hit_under_17()
        display_card = display_current_card(card_value, SCORE['User_turn'])
        check_for_stay(card_value, two_stays_in_same_turn)
        update_score(user_turn, card_value)

        print((
            f'{display_card}'
            f'Dealers current total is: {SCORE['Dealer']}\n'
        ))

        if score_over_twenty_one(SCORE['Dealer']):
            return 'Dealer Busts. You win!'

        if len(two_stays_in_same_turn) == 2:
            break

    game_info = determine_winner()
    return display_winner(game_info)

def how_to_play():
    goal, setup, deck, card_values = (MESSAGES[key] for key in MESSAGES)
    print(f'{goal}\n\n{setup}\n\n{deck}\n\n{card_values}\n')


def initialize_game():
    how_to_play()
    print(play_twenty_one())

initialize_game()
