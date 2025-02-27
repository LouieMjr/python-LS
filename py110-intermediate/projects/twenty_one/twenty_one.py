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

# def player_cards(card):
#     cards = []
#     cards.append(card)
#
# def dealer_cards(card):
#     cards = []
#     cards.append(card)

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

    print(suit, list(DECK[suit].keys()))
    card_key = choice(list(DECK[suit].keys()))
    print(card_key, 'cardkey')
    card = get_card_value(card_key, suit)


    remove_card_from_deck(suit, card_key)
    return card

def player_hit_or_stay(msg = 'Player would you like to Hit or Stay? '):
    response = input(msg)
    response = response[0].upper() + response[1:]

    if response in ('Hit', 'H'):
        return draw()

    return player_hit_or_stay('Please Enter hit or stay: ')

def score_over_twenty_one(score):
    if score > 21:
        return True
    return False

def play_twenty_one():
    user_turn = True

    while SCORE['User'] < 21 and SCORE['Dealer'] < 21:
        if user_turn:
            card_value = player_hit_or_stay()

            SCORE['User'] += card_value
            print(SCORE['User'], 'human score')
            if score_over_twenty_one(SCORE['User']):
                return 'You Bust. Dealer wins'

        else:
            card_value = draw()
            SCORE['Dealer'] += card_value
            print(SCORE['Dealer'], 'dealer score')
            if score_over_twenty_one(SCORE['User']):
                return 'Dealer Busts. You win'

        user_turn = not user_turn

play_twenty_one()
