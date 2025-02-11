from random import choice
from time import sleep
from os import system
import json
import pdb

with open('./TTT_messages.json') as file:
    MESSAGES = json.load(file)

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

def user_picks_cell(internal_board, board_options):
    if board_options == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        PRINT(MESSAGES['available_board_options'])

    row1, row2, row3 = board_options
    display_board_options = f'\n{row1}\n{row2}\n{row3}\n\n'
    PRINT(display_board_options)

    cell = input(MESSAGES['select_position'])

    if is_valid_board_position(cell, internal_board):
        system('clear')
        return int(cell)
    else:
        system('clear')
        PRINT(MESSAGES['unavailable'])
        return user_picks_cell(internal_board, board_options)

def is_valid_board_position(input, internal_board):
    return input in '123456789' and int(input) in internal_board.keys()

def random_computer_choice(remaining_options):
    return choice(remaining_options)

def update_board(display_board, list_coordinates, display_options_remaining,
                 marker):
    x, y = list_coordinates
    display_board[x][y] = marker
    display_options_remaining[x][y] = '-'

def check_for_winner(board, marker, current_player):
    # row winner
    for row in board:
        if all(ele if ele == marker else False for ele in row):
            return current_player

    top_left = board[0][0]
    top_center = board[0][1]
    top_right = board[0][2]
    center_left = board[1][0]
    center = board[1][1]
    center_right = board[1][2]
    bottom_left = board[2][0]
    bottom_center = board[2][1]
    bottom_right = board[2][2]

    # diagonal winner
    if top_left == marker and top_left == center and center == bottom_right  or top_right == marker and top_right == center and center == bottom_left:
        return current_player

    # column winner
    if top_left == marker and top_left == center_left and center_left == bottom_left or top_right == marker and top_right == center_right and center_right == bottom_right or top_center == marker and top_center == center and center == bottom_center:
        return current_player

    return False

def game_logic(display_board, player_marker, computer_marker):

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

    while INTERNAL_BOARD != {}:

        cell = user_picks_cell(INTERNAL_BOARD, board_options)

        if INTERNAL_BOARD.get(cell) is None:
            PRINT(f'Position {cell} is unavailable. Try again.\n')

        else:
            cell_coordinates = INTERNAL_BOARD[cell]
            del INTERNAL_BOARD[cell]
            update_board(display_board, cell_coordinates, board_options,
                         player_marker)
            result = check_for_winner(display_board, player_marker, 'Player')

            if result:
                print_board(display_board)
                display_winner(result)
                return

            positions_remaining = list(INTERNAL_BOARD.keys())

            cell = random_computer_choice(positions_remaining)
            cell_coordinates = INTERNAL_BOARD[cell]
            del INTERNAL_BOARD[cell]
            update_board(display_board, cell_coordinates, board_options,
                         computer_marker)
            result = check_for_winner(display_board, computer_marker, 'Computer')
            if result:
                print_board(display_board)
                display_winner(result)
                return
            print_board(display_board)

    PRINT('NO WINNER, GAME ENDS IN TIE')

def display_winner(input):
    PRINT(f'{input} WINNER\n')

def display_rules():

    winning_board1 = f'{['X', 'o', 'x']}-{['o', 'o', 'X']}-{['X', 'X', 'X']}\n'
    winning_board2 = f'{['X', 'o', 'o']}-{['o', 'X', 'X']}-{['o', 'o', 'x']}\n'
    winning_board3 = f'{['X', 'x', 'o']}-{['X', 'o', 'o']}-{['x', 'o', 'o']}'

    rules = MESSAGES['rules']
    PRINT(rules)

    win_ex_msg = MESSAGES['win_example_msg']
    PRINT(f'{win_ex_msg}{winning_board1}{winning_board2}{winning_board3}')

def restart_game(msg = MESSAGES['restart']):
    PRINT(msg)
    response = input()[0].upper()
    if response in ['Yes', 'Y']:
        system('clear')
        return play_tic_tac_toe()
    elif response in ['No', 'N']:
        PRINT('\nThank you for playing\n')
    else:
        return restart_game(MESSAGES['invalid_restart'])

def play_tic_tac_toe():

    player_pick = user_start_character()
    computer_pick = computer_start_character(player_pick)

    DISPLAY_BOARD = create_board()
    game_logic(DISPLAY_BOARD, player_pick, computer_pick)
    return restart_game()

def start_tic_tac_toe():
    PRINT('Lets play some Tic Tac Toe!\n')
    display_rules()

    play_tic_tac_toe()

start_tic_tac_toe()

