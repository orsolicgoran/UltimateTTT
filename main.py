import numpy as np

board = np.zeros((9, 9), dtype=int)

player_1_table = np.array([
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0]
])

player_2_table = np.array([
    [2, 2, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 2, 2],
    [2, 0, 0, 2, 0, 0, 2, 0, 0],
    [0, 2, 0, 0, 2, 0, 0, 2, 0],
    [0, 0, 2, 0, 0, 2, 0, 0, 2],
    [2, 0, 0, 0, 2, 0, 0, 0, 2],
    [0, 0, 2, 0, 2, 0, 2, 0, 0]
])

def init_board(board):
    board = np.zeros((9, 9), dtype=int)

def get_start():
    start = input()
    if start == "P":
        return 1
    elif start == "D":
        return 0

def get_move():
    move = input()
    row = int(move[0])
    column = int(move[-1])
    return (row, column)

def play_move(row, column):
    print(f"{row} {column}")

def modify_board(row, column, player):
    sub_board_idx = (row - 1) // 3 * 3 + (column - 1) // 3
    pos_within_sub_board = ((row - 1) % 3) * 3 + (column - 1) % 3
    board[sub_board_idx][pos_within_sub_board] = player

def check_3x3(board):
    for i in range(8):
        if np.array_equal(board, player_1_table[i]):
            return 1
        elif np.array_equal(board, player_2_table[i]):
            return 2

    if np.all(board != 0):
        return -1
    
    return 0

def check_game_over(board):
    sub_boards = [board[i] for i in range(9)]
    big_board = np.zeros(9, dtype=int)
    for idx, sub_board in enumerate(sub_boards):
        result = check_3x3(sub_board)
        big_board[idx] = result
    return check_3x3(big_board)

def print_board(board):
    reshaped_board = np.array(board).reshape(3, 3, 3, 3).swapaxes(1, 2).reshape(9, 9)
    for i in range(9):
        for j in range(9):
            print(reshaped_board[i, j], end=' ')
            if (j + 1) % 3 == 0 and j < 8:
                print("|", end=' ')
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print("-" * 29)

game_running = True
game_setup = False

while game_running:
    if not game_setup:
        init_board(board)
        print("Enter starting player (P/D)")
        start = get_start()
        game_setup = True
        print("GAME STARTING")
    
    if start:
        print("Player 1's turn")
        print("CURRENT BOARD:")
        print_board(board)
        row, column = get_move()
        modify_board(row, column, 1)
        start = not start
    else:
        print("Player 2's turn")
        print("CURRENT BOARD:")
        print_board(board)
        row, column = get_move()
        modify_board(row, column, 2)
        start = not start
    
    game_over = check_game_over(board)
    if game_over == 1:
        print("Player 1 wins")
        game_running = False
        game_setup = False
    elif game_over == 2:
        print("Player 2 wins")
        game_running = False
        game_setup = False
    elif game_over == -1:
        print("Draw")
        game_running = False
        game_setup = False
    elif game_over == 0:
        continue
