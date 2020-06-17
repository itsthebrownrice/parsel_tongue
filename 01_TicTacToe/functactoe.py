# Print board representation
def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Ask for player input marker
def player_input():

    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input('Player 1 choose a marker (X or O): ')
        player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

# Places the marker in the board accdg. to position
def place_marker(board, marker, index):

    board[int(index)] = marker

# Checks each column, row, and diagonal for winners
def win_check(board, marker):

    return (board[7] == marker and board[8] == marker and board[9] == marker or
           board[4] == marker and board[5] == marker and board[6] == marker or
           board[1] == marker and board[2] == marker and board[3] == marker or
           board[7] == marker and board[4] == marker and board[1] == marker or
           board[8] == marker and board[5] == marker and board[2] == marker or
           board[9] == marker and board[6] == marker and board[3] == marker or
           board[7] == marker and board[5] == marker and board[3] == marker or
           board[9] == marker and board[5] == marker and board[1] == marker)

# Chooses which player will go first
import random
def first_turn():

    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Checks a player's input position if the position is still empty
def space_check(board, move):

    return board[int(move)] == ' '

# Checks the whole board if it's full
def board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Asks for player's input position
def player_move(board):

    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(move)):
        move = input('Choose your next move (1-9): ')

    return int(move)

# Asks players if they want to play agan
def replay():

    return input('Do you want to play again? (Y/N): ').lower().startswith('y')
