from pprint import pprint
from random import randrange, choice
from time import sleep

position_on_board = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

x_and_y_axis_on_board = {
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

def print_with_typing_effect(message):
    for char in message:
        print(char, end='', flush=True)
        sleep(0.02)

PRINT = print_with_typing_effect

def create_board():
    board = []

    for _ in range(3):
        board.append(['-' for _ in range(3)])

    return board

BOARD = create_board()

def display_board(board):
    for row in board:
        print(row)

def computer_start_character(user_pick):
    if user_pick == 'X':
        PRINT('Computer picked: O\n\n')
        return 'O'
    else:
        PRINT('Computer picked: X\n\n')
        return 'X'

def user_start_character():
    PRINT("\n\nWhen you're ready, select a character: X or O: ")
    pick = input().upper()
    PRINT(f'\nYou picked: {pick}\n')
    return pick

# def user_selection_on_board(board):

def display_rules():
    rules = "\nTic Tac Toe is a 2-player game played on a 3x3 grid called the board.\nEach player takes a turn and marks a square on the board. The first player\nto get 3 squares in a row -- horizontally, vertically, or diagonally -- wins.\nIf all 9 squares are filled and neither player has 3 in a row, the game ends in a tie."

    winning_board1 = f'{['X', 'o', 'x']}-{['o', 'o', 'X']}-{['X', 'X', 'X']}\n'
    winning_board2 = f'{['X', 'o', 'o']}-{['o', 'X', 'X']}-{['o', 'o', 'x']}\n'
    winning_board3 = f'{['X', 'x', 'o']}-{['X', 'o', 'o']}-{['x', 'o', 'o']}'

    PRINT(rules)
    PRINT(f'\n\nHere are some examples of winning boards.\n\n{winning_board1}{winning_board2}{winning_board3}')

def pick_square():
    PRINT('\nMake a selection on the board\nHere are your options:\n')
    board_options = f'{[1, 2, 3]}\n{[4, 5, 6]}\n{[7, 8, 9]}\n'
    PRINT(board_options) 
    position = int(input('Enter the number on the board that correlates to the position you want to select: '))
    return position

# def is_board_position_open(list_of_numbers):
#     x, y = list_of_numbers
#     board_position = BOARD[x][y]
#     if board_position == '-':
#         return True
#     return False


def random_computer_choice(remaining_options):
    pick = choice(remaining_options)
    return [pick, x_and_y_axis_on_board[pick]]

def update_board(list_of_numbers, key, player = 'computer'):
    x, y = list_of_numbers
    BOARD[x][y] = 'O' if player == 'computer' else 'X'
    del x_and_y_axis_on_board[key]

def game_logic():
    while x_and_y_axis_on_board != {}:

        selection = pick_square()

        if x_and_y_axis_on_board.get(selection) is not None:
            user_x_and_y = x_and_y_axis_on_board[selection]
            update_board(user_x_and_y, selection, 'user')

            positions_remaining = list(x_and_y_axis_on_board.keys())

            key_to_delete, x_and_y = random_computer_choice(positions_remaining)
            update_board(x_and_y, key_to_delete)
            display_board(BOARD)

        else:
            print('no')

# game_logic()

def start_tic_tac_toe():
    PRINT('Lets play some Tic Tac Toe!\n')
    PRINT("Here are the rules before we begin.\n")
    display_rules()

    player_pick = user_start_character()
    computer_start_character(player_pick)

    display_board(BOARD)
    game_logic()


start_tic_tac_toe()

