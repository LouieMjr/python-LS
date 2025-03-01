from random import choice

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

def update_ace_list(ace):
    return

def determine_ace_value(ace, player):
    one = ace[0]
    eleven = ace[1]
    current_score = SCORE[player]

    return one if current_score + eleven > 21 else eleven

def remove_suits_without_cards(suits):
    for suit in suits:
        if DECK.get(suit) == {}:
            suits.remove(suit)
            del DECK[suit]

    return suits

def remove_card_from_deck(suit, card_key):

    if card_key == 'Ace':
        print(card_key)

    del DECK[suit][card_key]

def get_card_value(card_key, suit):
    card = DECK[suit][card_key]
    return card

def draw():
    all_suits = list(DECK.keys())
    remaining_suits = remove_suits_without_cards(all_suits)
    suit = choice(remaining_suits)

    card_key = choice(list(DECK[suit].keys()))
    card = get_card_value(card_key, suit)

    remove_card_from_deck(suit, card_key)
    return card

def player_hit_or_stay(msg = 'Player would you like to (Hit/h) or (Stay/s)? '):
    response = input(msg)
    response = response[0].upper() + response[1:]

    if response in ('Hit', 'H'):
        return draw()
    if response in ('Stay', 'S'):
        return 0

    return player_hit_or_stay('Please Enter (hit/h) or (stay/s): ')

def dealer_hit_under_17():
    TARGET = 17
    dealer_score = SCORE['Dealer']

    if dealer_score < TARGET:
        return draw()

    return 0

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

def check_for_stay(card_value, stays):
    if card_value == 0:
        stays.append(True)

def determine_winner():
    user_score = SCORE['User']
    dealer_score = SCORE['Dealer']

    if dealer_score == user_score:
        return [user_score, dealer_score, 'Tie game!']
    elif user_score > dealer_score:
        return [user_score, dealer_score, 'Player wins!']
    else:
        return [user_score, dealer_score, 'Dealer wins!']

def display_winner(game_info):
    user_score, dealer_score, winner = game_info
    return f'{winner} With a score of {user_score} to {dealer_score}'

def play_twenty_one():

    while SCORE['User'] < 21 and SCORE['Dealer'] < 21:

            user_turn = True
            two_stays_in_same_turn = []

            card_value = player_hit_or_stay()
            check_for_stay(card_value, two_stays_in_same_turn)
            update_score(user_turn, card_value)
            user_turn = not user_turn

            print(SCORE['User'], 'human score')

            if score_over_twenty_one(SCORE['User']):
                return 'You Bust. Dealer wins'

            card_value = dealer_hit_under_17()
            check_for_stay(card_value, two_stays_in_same_turn)
            update_score(user_turn, card_value)

            print(SCORE['Dealer'], 'dealer score')
            print(two_stays_in_same_turn, 'how many stays')
            if score_over_twenty_one(SCORE['Dealer']):
                return 'Dealer Busts. You win'

            if len(two_stays_in_same_turn) == 2:
                break

    game_info = determine_winner()
    print(display_winner(game_info))

def initialize_game():
    print(play_twenty_one())

initialize_game()
