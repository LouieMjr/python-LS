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
    'Player': 0,
    'Dealer': 0
}

# def player_cards(card):
#     cards = []
#     cards.append(card)
#
# def dealer_cards(card):
#     cards = []
#     cards.append(card)

def remove_card_from_deck(suit, card):
    del DECK[suit][card]

def draw():
    all_suits = list(DECK.keys())
    suit = choice(all_suits)
    card = choice(list(DECK[suit].keys()))
    remove_card_from_deck(suit, card)
    return card

def player_hit_or_stay(msg = 'Player would you like to Hit or Stay? '):
    response = input(msg)
    response = response[0].upper() + response[1:]
    print(response)
    if response == 'Hit':
        card = draw()
        print(card)
        SCORE['Player'] += card
        print(SCORE['Player'])
    else:
        return player_hit_or_stay('Please Enter hit or stay: ')

def twenty_one_gameplay():
    player_hit_or_stay()

twenty_one_gameplay()
