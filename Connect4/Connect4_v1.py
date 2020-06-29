# Terminal based Connect-4

import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():  
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_loc(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def show_board(board):
    print(np.flip(board, 0), "\n  0  1  2  3  4  5  6 \n")

def winning_move(board, piece):
    # Horizontal wins
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    # Verical wins
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    # Positve slope diagonal wins
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    # Negative slope diagonal wins
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True

board = create_board()
gameover = False
turn = 0

print("\n-------CONNECT 4!-------\n")
show_board(board)

while not gameover:

    if turn == 0:
        col = int(input(f"Player 1 turn (0-{COLUMN_COUNT-1}): "))
        piece = 1
    else:
        col = int(input(F"Player 2 turn (0-{COLUMN_COUNT-1}): "))
        piece = 2

    if is_valid_loc(board, col):
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, piece)
        show_board(board)
        if winning_move(board, piece):
            print(f"PLAYER {piece} WINS!!!")
            gameover = True

    turn += 1
    turn = turn % 2