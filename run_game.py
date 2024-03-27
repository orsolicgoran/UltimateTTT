import game as gm

def run_game():
    game = gm.Game()
    game.start_game()

    while game.is_game_running():
        if not game.get_first_move_played():
            game.set_starting_player()
            
        if game.current_player == 1:
            game.current_move.get_move()
        else:
            while game.current_move.get_ai_move().is_move_legal(game.get_board(), game.get_first_move_played(), game.get_last_move_played(), game.get_board().get_big_board()) == False:
                pass

        if game.current_move.is_move_legal(game.get_board(), game.get_first_move_played(), game.get_last_move_played(), game.get_board().get_big_board()):
            game.get_board().modify_board(game.current_move.row, game.current_move.column, game.current_player)
            game.set_last_move_played(game.current_move)
            game.get_board().print_board()
            print(f"Last move played: {game.get_last_move_played().to_string()}")
            game.switch_turn()
        else:
            print("Illegal move, game over.")
            game.end_game()


        if game.get_board().check_game_over() == 1:
            print("Player 1 wins!")
            game.end_game()
        elif game.get_board().check_game_over() == 2:
            print("Player 2 wins!")
            game.end_game()
        elif game.get_board().check_game_over() == -1:
            print("It's a draw!")
            game.end_game()
        if not game.get_first_move_played():
            game.set_first_move_played()