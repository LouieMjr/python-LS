from random import choice
from time import sleep
from os import system
import json
from typing import is_typeddict

with open('./TTT_messages.json') as file:
    MESSAGES = json.load(file)

board_options = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

INTERNAL_BOARD = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
}


def print_with_typing_effect(message, time = 0.02):
    for char in message:
        print(char, end='', flush=True)
        sleep(time)

PRINT = print_with_typing_effect

def create_board():
    board = []

    for _ in range(3):
        board.append(['-' for _ in range(3)])

    return board

DISPLAY_BOARD = create_board()

def print_board(board):
    for row in board:
        print(row)

def computer_start_character(user_pick):
    if user_pick == 'X':
        PRINT('Computer picked: O\n\n')
        return 'O'
    else:
        PRINT('Computer picked: X\n\n')
        return 'X'

def user_start_character(msg = MESSAGES['character_select']):
    PRINT(msg)
    pick = input().upper()

    if validate_user_character(pick):
        system('clear')
        PRINT(f'\nYou picked: {pick}\n')
        return pick
    else:
        return user_start_character(MESSAGES['invalid_character'])

def validate_user_character(input):
    if input != 'X' and input != 'O':
        return False
    return True

def display_rules():

    winning_board1 = f'{['X', 'o', 'x']}-{['o', 'o', 'X']}-{['X', 'X', 'X']}\n'
    winning_board2 = f'{['X', 'o', 'o']}-{['o', 'X', 'X']}-{['o', 'o', 'x']}\n'
    winning_board3 = f'{['X', 'x', 'o']}-{['X', 'o', 'o']}-{['x', 'o', 'o']}'

    rules = MESSAGES['rules']
    # PRINT(rules)

    win_ex_msg = MESSAGES['win_example_msg']
    # PRINT(f'{win_ex_msg}{winning_board1}{winning_board2}{winning_board3}')

def user_picks_square():
    if board_options == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        PRINT(MESSAGES['available_board_options'])

    row1, row2, row3 = board_options
    display_board_options = f'\n{row1}\n{row2}\n{row3}\n\n'
    PRINT(display_board_options)

    try:
        position = int(input(MESSAGES['select_position']))

        if is_valid_board_position(position):
            system('clear')
            return [position, board_options]
        else:
            PRINT(MESSAGES['unavailable'])
            return user_picks_square()

    except (ValueError, TypeError):
        PRINT(MESSAGES['unavailable'])
        return user_picks_square()


def is_valid_board_position(number):
    valid_number = number in [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if isinstance(number, int) and valid_number:
        return True
    return False


def random_computer_choice(remaining_options):
    pick = choice(remaining_options)
    return [pick, INTERNAL_BOARD[pick]]

def update_board(list_of_numbers, key, options_remaining, player = 'computer'):
    x, y = list_of_numbers
    character = 'O' if player == 'computer' else 'X'
    DISPLAY_BOARD[x][y] = character
    del INTERNAL_BOARD[key]
    options_remaining[x][y] = '-'



def game_logic():
    while INTERNAL_BOARD != {}:

        square, board_options = user_picks_square()

        if INTERNAL_BOARD.get(square) is None:
            PRINT(f'Position {square} is unavailable. Try again.\n')

        else:
            is_winner(DISPLAY_BOARD)
            user_x_and_y = INTERNAL_BOARD[square]
            update_board(user_x_and_y, square, board_options, 'user')

            positions_remaining = list(INTERNAL_BOARD.keys())

            computer_square, x_and_y = random_computer_choice(positions_remaining)
            update_board(x_and_y, computer_square, board_options)
            print_board(DISPLAY_BOARD)

def start_tic_tac_toe():
    PRINT('Lets play some Tic Tac Toe!\n')
    PRINT("Here are the rules before we begin.\n")
    display_rules()

    player_pick = user_start_character()
    computer_start_character(player_pick)

    game_logic()


start_tic_tac_toe()

