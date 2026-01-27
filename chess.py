from board import Board

class Chess:
    def __init__(self):
        pass

    def start_game(self):
        self.board = Board()
        self.board.init_game()

    def parse_input(self):
        pass

if __name__ == "__main__":
    chess = Chess()
    chess.start_game()
    chess.board.print_board()