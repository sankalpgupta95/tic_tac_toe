import random

print('Welcome to Tic Tac Toe!')


def choose_first():
    print(f"Player{random.randint(1, 2)}")


def win_check(board, mark):
    win = 0
    if board[1] == mark and board[2] == mark and board[3] == mark:
        win = 1
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        win = 1
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        win = 1
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        win = 1
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        win = 1
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        win = 1
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        win = 1
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        win = 1

    return win


def full_board_check(board):
    for i in board:
        if i == ' ':
            return False
    return True


def display_board(board):
    print("\n")
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print("\n")


def player_input():
    marker = input("player1 = \"Please pick a marker 'X' or 'O'\" ")
    while marker not in ('X', 'O'):
        marker = input("Sorry! You can pick only either 'X' or 'O' ")
    return marker


def replay():
    ans = input("Do you want to play again? (Y/N) ")
    return ans.upper() == 'Y'


while True:
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Set the game up here
    # pass
    p1_marker = player_input()
    if p1_marker == 'X':
        p2_marker = 'O'
    elif p1_marker == 'O':
        p2_marker = 'X'

    print("\nLet's Get Started!!\n")
    display_board(board)

    while True:
        while True:
            while True:
                try:
                    position = int(input("Player 1 Enter the position of your marker "))
                except ValueError:
                    print("!!Enter only numbers from 1 to 9")
                    continue
                except IndexError:
                    print("!!Enter only numbers from 1 to 9")
                    continue
                else:
                    break
            if position in inputs:
                inputs.remove(position)
                break
            else:
                print('This position is already marked. Please choose the blank positions only😁')
                continue
        board[position] = p1_marker
        display_board(board)
        if win_check(board, p1_marker) == 1:
            print("Player 1 Wins!!!")
            break

        while True:
            while True:
                try:
                    position = int(input("Player 1 Enter the position of your marker "))
                except ValueError:
                    print("!!Enter only numbers from 1 to 9")
                    continue
                except IndexError:
                    print("!!Enter only numbers from 1 to 9")
                    continue
                else:
                    break
            if position in inputs:
                inputs.remove(position)
                break
            else:
                print('This position is already marked. Please choose the blank positions only😁')
                continue
        '''
        This below commented code to be uncommented if user wants to play with computer
        '''
        # while True:
        #    position = random.randint(1,9)
        #    if(board[position] == ' '):
        #        break
        board[position] = p2_marker
        display_board(board)
        if win_check(board, p2_marker) == 1:
            print("Player 2 Wins!!!")
            break

        if full_board_check(board):
            print("Sorry!! Nobody won")

    if not replay():
        break
    else:
        inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
