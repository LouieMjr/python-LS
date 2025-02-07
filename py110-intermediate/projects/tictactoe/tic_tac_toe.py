from pprint import pprint

position_on_board = ('r1', 'r2', 'r3', 'c1', 'c2', 'c3', 'l1', 'l2', 'l3')
circle_or_square = ('X', 'O')

def create_board():
    board = []
    row = ['-', '-', '-']

    for _ in range(3):
        board.append(row)

    return board


BOARD = create_board()

def display_board(board):
    for row in board:
        print(row)


def user_starting_charcter():
    pick = input('\nTo begin select a character: X or O: ').upper()
    return f'You picked {pick}'

# def user_selection_on_board(board):

def display_rules():
    rules = "Tic Tac Toe is a 2-player game played on a 3x3 grid called the board.\nEach player takes a turn and marks a square on the board. The first player\nto get 3 squares in a row -- horizontally, vertically, or diagonally -- wins.\nIf all 9 squares are filled and neither player has 3 in a row, the game ends in a tie."

    winning_board1 = f'{['X', 'o', 'x']}-{['o', 'o', 'X']}-{['X', 'X', 'X']}\n'
    winning_board2 = f'{['X', 'o', 'o']}-{['o', 'X', 'X']}-{['o', 'o', 'x']}\n'
    winning_board3 = f'{['X', 'x', 'o']}-{['X', 'o', 'o']}-{['x', 'o', 'o']}'

    print(rules, '\n')
    print(f'Here are some examples of winning boards\n\n{winning_board1}{winning_board2}{winning_board3}')

def start_tic_tac_toe():
    print('Lets play some Tic Tac Toe!')
    print("Here's the starting board.\n")
    display_board(BOARD)

    start_character = user_starting_charcter()
    print(start_character)
    display_rules()

start_tic_tac_toe()

