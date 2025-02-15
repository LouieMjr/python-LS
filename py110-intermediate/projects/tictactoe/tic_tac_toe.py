from random import choice
from time import sleep
from os import system
import json
import math

with open('./TTT_messages.json', encoding="utf-8") as file:
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

    PRINT('Computer picked: X\n\n')
    return 'X'

def user_start_character(msg = MESSAGES['character_select']):
    PRINT(msg)
    pick = input().upper()

    if validate_user_character(pick):
        system('clear')
        PRINT(f'\nYou picked: {pick}\n')
        return pick

    return user_start_character(MESSAGES['invalid_character'])

def validate_user_character(user_input):
    if user_input not in ('X', 'O'):
        return False
    return True

def select_cell(internal_board, remaining_options, current_player):
    if current_player == 'Computer':
        return choice(list(internal_board.keys()))

    if remaining_options == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        PRINT(MESSAGES['available_board_options'])

    row1, row2, row3 = remaining_options
    display_board_options = f'\n{row1}\n{row2}\n{row3}\n\n'
    print(display_board_options)

    PRINT(MESSAGES['select_position'])
    cell = input()
    if is_valid_board_position(cell, internal_board):
        system('clear')
        return int(cell)

    system('clear')
    PRINT(MESSAGES['unavailable'])
    return select_cell(internal_board, remaining_options, current_player)

def is_valid_board_position(user_input, internal_board):
    return (user_input in '123456789'
            and int(user_input) in internal_board.keys())

def update_board(display_board, list_coordinates, display_options_remaining,
                 marker):
    x, y = list_coordinates
    display_board[x][y] = marker
    display_options_remaining[x][y] = '-'

def check_round_winner(board, marker, current_player):
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


    top_left_to_bottom_right = (top_left == marker
                                and top_left == center
                                and center == bottom_right)

    top_right_to_bottom_left = (top_right == marker
                                and top_right == center
                                and center == bottom_left)
    # diagonal winner
    if (top_right_to_bottom_left or top_left_to_bottom_right):
        return current_player

    left_column = (top_left == marker
                    and top_left == center_left
                    and center_left == bottom_left)

    right_column = (top_right == marker
                    and top_right == center_right
                    and center_right == bottom_right)
    center_column = (top_center == marker
                     and top_center == center
                     and center == bottom_center)

    # column winner
    if (left_column or right_column or center_column):
        return current_player

    return False

def update_score(score):
    score += 1
    return score

def initial_game_state():

    board_options = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    internal_board = {
        1: [0, 0], # top left
        2: [0, 1], # top center
        3: [0, 2], # top right
        4: [1, 0], # center left
        5: [1, 1], # center
        6: [1, 2], # center right
        7: [2, 0], # bottom left
        8: [2, 1], # bottom center
        9: [2, 2], # bottom right
    }

    return [board_options, internal_board]

def play_round(display_board, player_marker, computer_marker):
    board_options, internal_board = initial_game_state()

    while internal_board != {}:

        current_turn = ('Player' if len(internal_board.keys()) % 2 == 1
                                 else 'Computer')

        current_marker = (player_marker if current_turn == 'Player'
                                       else computer_marker)
        cell = select_cell(internal_board, board_options, current_turn)

        if internal_board.get(cell) is None:
            PRINT(f'Position {cell} is unavailable. Try again.\n')
            print_board(display_board)

        else:
            cell_coordinates = internal_board[cell]
            del internal_board[cell]
            update_board(display_board, cell_coordinates, board_options,
                         current_marker)

            round_winner = check_round_winner(display_board, current_marker,
            current_turn)
            if round_winner:
                return round_winner

            if current_turn == 'Computer':
                print_board(display_board)

    return PRINT('Round ended in a tie!\n')

def remove_s_from_round(string):
    list_of_words = string.split(' ')
    list_of_words[list_of_words.index('rounds')] = 'round'
    return ' '.join(list_of_words)

def display_current_score(score_tracker, rounds_to_win, rounds):
    player_total = score_tracker['Player']
    computer_total = score_tracker['Computer']
    zero = computer_total + player_total

    if zero == 0:
        return PRINT(
            f"Best of {rounds} games.\nIt's 0 to 0. First to {rounds_to_win} "
            "rounds wins!\n")

    if player_total == rounds_to_win:
        return PRINT(f'You won! {player_total} rounds to {computer_total}.\n')

    if computer_total == rounds_to_win:
        return PRINT(f'You lost! {computer_total} rounds to {player_total}.\n')

    if player_total > computer_total:
        msg = (f"You're winning: {player_total} rounds to {computer_total}.\n"
        "You're almost there!\n")
        if player_total == 1:
            return PRINT(remove_s_from_round(msg))

        return PRINT(msg)

    if player_total < computer_total:
        msg = (f"You're losing: {computer_total} rounds to {player_total}.\n"
        "Don't give up!\n")
        if computer_total == 1:
            return PRINT(remove_s_from_round(msg))

        return PRINT(msg)

    if player_total == computer_total:
        return PRINT(
            f"It's currently a tie: {player_total} to {computer_total}."
            "\nKeep Fighting!\n")

def display_rules():

    winning_board1 = f'{['X', 'o', 'x']}-{['o', 'o', 'X']}-{['X', 'X', 'X']}\n'
    winning_board2 = f'{['X', 'o', 'o']}-{['o', 'X', 'X']}-{['o', 'o', 'x']}\n'
    winning_board3 = f'{['X', 'x', 'o']}-{['X', 'o', 'o']}-{['x', 'o', 'o']}'

    rules = MESSAGES['rules']
    PRINT(rules)

    win_example_msg = MESSAGES['win_example_msg']
    PRINT(f'{win_example_msg}{winning_board1}{winning_board2}{winning_board3}')

def restart_game(msg = MESSAGES['restart']):
    PRINT(msg)
    response = input()[0].upper()

    if response in ['Yes', 'Y']:
        system('clear')
        return play_tic_tac_toe()
    if response in ['No', 'N']:
        return PRINT('\nThank you for playing!\n')

    return restart_game(MESSAGES['invalid_restart'])

def rounds_needed_to_win(total_rounds):
    round_number_up = math.ceil(total_rounds / 2)
    return round_number_up if total_rounds % 2 == 1 else round_number_up + 1

def play_tic_tac_toe():

    player_pick = user_start_character()
    computer_pick = computer_start_character(player_pick)

    score_tracker = {"Player": 0, "Computer": 0}

    rounds = 5
    # you can changes "rounds" to any number, func below will
    # adapt to give proper amount of rounds needed to win
    rounds_to_win = rounds_needed_to_win(rounds)
    display_current_score(score_tracker, rounds_to_win, rounds)

    while rounds > 0:

        display_board = create_board()
        round_winner = play_round(display_board, player_pick, computer_pick)

        if round_winner:
            rounds -= 1
            PRINT(f'{round_winner} won that round!\n')
            score_tracker[round_winner] += 1
            display_current_score(score_tracker, rounds_to_win, rounds)
            if score_tracker[round_winner] == rounds_to_win:
                PRINT(f'{round_winner} Wins The Game!\n')
                print_board(display_board)
                break

        if rounds == 0:
            PRINT('\nGame has ended in a tie!\n')

    return restart_game()

def initialize_game():
    # PRINT('Lets play some Tic Tac Toe!\n')
    # display_rules()

    play_tic_tac_toe()

initialize_game()
