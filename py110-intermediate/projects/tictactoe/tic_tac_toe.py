from pprint import pprint
from random import randrange

position_on_board = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

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
        print('Computer picked: O')
        return 'O'
    else:
        print('Computer picked: X')
        return 'X'

def user_start_character():
    pick = input('\nTo begin select a character: X or O: ').upper()
    print(f'You picked: {pick}')
    return pick

# def user_selection_on_board(board):

def display_rules():
    rules = "Tic Tac Toe is a 2-player game played on a 3x3 grid called the board.\nEach player takes a turn and marks a square on the board. The first player\nto get 3 squares in a row -- horizontally, vertically, or diagonally -- wins.\nIf all 9 squares are filled and neither player has 3 in a row, the game ends in a tie."

    winning_board1 = f'{['X', 'o', 'x']}-{['o', 'o', 'X']}-{['X', 'X', 'X']}\n'
    winning_board2 = f'{['X', 'o', 'o']}-{['o', 'X', 'X']}-{['o', 'o', 'x']}\n'
    winning_board3 = f'{['X', 'x', 'o']}-{['X', 'o', 'o']}-{['x', 'o', 'o']}'

    print(rules, '\n')
    print(f'Here are some examples of winning boards\n\n{winning_board1}{winning_board2}{winning_board3}')

def pick_square():
    print('Make a selection on the board\nHere are you options:\n')
    board_options = f'{[1, 2, 3]}\n{[4, 5, 6]}\n{[7, 8, 9]}\n'
    print(board_options) 
    position = int(input('Enter the number on the board that correlates to the position you want to select: '))
    return position

# def is_board_position_open(list_of_numbers):
#     x, y = list_of_numbers
#     board_position = BOARD[x][y]
#     if board_position == '-':
#         return True
#     return False


def generate_two_random_numbers():
    random_numbers = []
    for _ in range(2):
        num = randrange(3)
        random_numbers.append(num)
    return random_numbers

# def random_computer_choice(board_position_dict):
#     x, y = generate_two_random_numbers()

def update_board(list_of_numbers, player = 'computer'):
    x, y = list_of_numbers
    BOARD[x][y] = 'O' if player == 'computer' else 'X'

    # if player == 'computer':
    #     BOARD[x][y] = 'O'
    # else:
    #     BOARD[x][y] = 'X'




def game_logic():
    positions_on_board = {
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

    while positions_on_board != {}:

        selection = pick_square()

        if positions_on_board.get(selection) is not None:
            user_numbers = positions_on_board[selection]
            update_board(user_numbers, 'user')
            del positions_on_board[selection]

            # update_board()
            print(BOARD)

            print('yes')
        else:
            print('no')




game_logic()


def start_tic_tac_toe():
    print('Lets play some Tic Tac Toe!')
    print("Here are the rules before we begin.\n")
    display_rules()

    player_pick = user_start_character()
    computer_pick = computer_start_character(player_pick)
 
    display_board(BOARD)



# start_tic_tac_toe()

