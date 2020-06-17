from functactoe import display_board, player_input, place_marker, win_check, first_turn, space_check, board_check, player_move, replay
import random

##################################################################################
################################ACTUAL GAME#######################################
##################################################################################
print('Welcome to Tic Tac Toe')

while True:
    #setup game
    board = [' ']*10

    player1, player2 = player_input()
    player_turn = first_turn()
    print(f'{player_turn} goes first!')

    play = input('Ready to play? (Y/N): ')

    if play.lower() == 'y':
        game_on = True
    else:
        game_on = False
        break

    while game_on:
        #player1's turn
        if player_turn == 'Player 1':
            display_board(board)
            position = player_move(board)
            place_marker(board, player1, position)

            if win_check(board, player1):
                display_board(board)
                print('CONGRATULATIONS! YOU WON THE GAME!!')
                game_on = False
            else:
                if board_check(board) == True:
                    game_on = False
                    display_board(board)
                    print("IT'S A DRAW")
                else:
                    player_turn = 'Player 2'
        else:
            #player2's turn
            if player_turn == 'Player 2':
                display_board(board)
                position = player_move(board)
                place_marker(board, player2, position)

                if win_check(board, player2):
                    display_board(board)
                    print('CONGRATULATIONS! YOU WON THE GAME!!')
                    game_on = False
                else:
                    if board_check(board) ==  True:
                        game_on = False
                        display_board(board)
                        print("IT'S A DRAW")
                    else:
                        player_turn = 'Player 1'
    if not replay():
        break
