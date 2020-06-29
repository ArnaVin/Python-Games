# GUI based Connect-4 with an AI

import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 10)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
COLOUR_R = (17, 108, 135)
COLOUR_C = (5, 26, 48)
COLOUR_P1 = (114, 223, 191)
COLOUR_P2 = (255, 40, 105)
COLOUR_DB = (19, 67, 95)

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

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, COLOUR_R, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, COLOUR_C, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, COLOUR_P1, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, COLOUR_P2, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

board = create_board()
gameover = False
turn = 0

pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("calibri", 75)

while not gameover:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, COLOUR_DB, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, COLOUR_P1, (posx, int(SQUARESIZE/2)), RADIUS-5)
            else:
                pygame.draw.circle(screen, COLOUR_P2, (posx, int(SQUARESIZE/2)), RADIUS-5)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                piece = 1

            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                piece = 2

            if is_valid_loc(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col , piece)

                    if winning_move(board, piece):
                        label = myfont.render(f"PLAYER {piece} WINS!!", 1, COLOUR_C)
                        screen.blit(label, (40, 10))
                        gameover = True

            draw_board(board)
            turn = (turn+1) % 2

            if gameover:
                pygame.time.wait(3000)
