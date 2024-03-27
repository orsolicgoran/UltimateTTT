import numpy as np
import board as brd
import move as mv


class Game:
    def __init__(self):
        self._game_running = False
        self._first_move_played = False
        self._starting_player = None
        self.current_player = None
        self.board = brd.Board()
        self.last_move_played = mv.Move()
        self.current_move = mv.Move()

    def start_game(self):
        self._game_running = True

    def end_game(self):
        self._game_running = False

    def is_game_running(self):
        return self._game_running

    def get_starting_player(self):
        return self._starting_player

    def set_starting_player(self):
        starting_player = None
        while starting_player not in ["P", "D"]:
            starting_player = input("Enter starting player (P/D): ").upper()
        if starting_player == "P":
            self._starting_player = 1
            self.current_player = 1
        elif starting_player == "D":
            self._starting_player = 2
            self.current_player = 2
    
    def get_first_move_played(self):
        return self._first_move_played

    def set_first_move_played(self):
        self._first_move_played = True

    def is_game_running(self):
        return self._game_running

    def switch_turn(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def set_last_move_played(self, move):
        self.last_move_played.row = move.row
        self.last_move_played.column = move.column

    def get_last_move_played(self):
        return self.last_move_played

    def get_board(self):
        return self.board
