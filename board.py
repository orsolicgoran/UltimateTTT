import numpy as np

class Board:
    def __init__(self):
        self.board = np.zeros((9,9), dtype=int)
        self.big_board = np.zeros(9, dtype=int)
        self._player_1_table = np.array([
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0]
        ])
        self._player_2_table = np.array([
            [2, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 2, 2],
            [2, 0, 0, 2, 0, 0, 2, 0, 0],
            [0, 2, 0, 0, 2, 0, 0, 2, 0],
            [0, 0, 2, 0, 0, 2, 0, 0, 2],
            [2, 0, 0, 0, 2, 0, 0, 0, 2],
            [0, 0, 2, 0, 2, 0, 2, 0, 0]
        ])

    def init_board(self):
        self.board = np.zeros((9, 9), dtype=int)

    def clear_board(self):
        self.board = np.zeros((9, 9), dtype=int)

    def get_board(self):
        return self.board

    def print_board(self):
        reshaped_board = np.array(self.board).reshape(3, 3, 3, 3).swapaxes(1, 2).reshape(9, 9)
        for i in range(9):
            for j in range(9):
                print(reshaped_board[i, j], end=' ')
                if (j + 1) % 3 == 0 and j < 8:
                    print("|", end=' ')
            print()
            if (i + 1) % 3 == 0 and i < 8:
                print("-" * 29)

    def modify_board(self, row, column, player):
        sub_board_idx = (row - 1) // 3 * 3 + (column - 1) // 3
        pos_within_sub_board = ((row - 1) % 3) * 3 + (column - 1) % 3
        self.board[sub_board_idx][pos_within_sub_board] = player

    def check_3x3(self, board):
        for i in range(8):
            if np.array_equal(board, self._player_1_table[i]):
                return 1
            elif np.array_equal(board, self._player_2_table[i]):
                return 2

        if np.all(board != 0):
            return -1
    
        return 0

    def check_game_over(self):
        sub_boards = [self.board[i] for i in range(9)]
        for idx, sub_board in enumerate(sub_boards):
            result = self.check_3x3(sub_board)
            self.big_board[idx] = result
        return self.check_3x3(self.big_board)