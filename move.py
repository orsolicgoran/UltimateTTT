import numpy as np

class Move:
    def __init__(self):
        self.row = 0
        self.column = 0

    def get_move(self):
        move = input("Please input your move: ")
        self.row = int(move[0])
        self.column = int(move[-1])
        
    def play_move(self):
        print(f"{self.row} {self.column}")

    def is_move_legal(self, board, first_move_played, last_move_played):
        if not first_move_played:
            if self.row in range(1, 9) and self.column in range(1, 9):
                return True
        else:
            last_move_pos = ((last_move_played.row - 1) % 3) * 3 + (last_move_played.column - 1) % 3
            sub_board_idx = (self.row - 1) // 3 * 3 + (self.column - 1) // 3
            if last_move_pos == sub_board_idx:
                if board.get_board()[sub_board_idx][(self.row - 1) % 3 * 3 + (self.column - 1) % 3] == 0:
                    return True
        return False

    def set_row(self, row):
        self.row = row

    def set_column(self, column):
        self.column = column