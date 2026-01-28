from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King

class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                col = " "
                row.append(col)
            self.board.append(row)
        # Index to algebraically label chess board
        self.row = {
            8: 0,
            7: 1,
            6: 2,
            5: 3,
            4: 4,
            3: 5,
            2: 6,
            1: 7 
        }
        self.col = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7
        }


    def print_board(self, active_colour):
        if active_colour == "white":
            print("   ---------------------------------")
            for row_index, row in self.row.items():
                print(f""" {row_index} | {self.board[row][self.col["A"]]} | {self.board[row][self.col["B"]]} | {self.board[row][self.col["C"]]} | {self.board[row][self.col["D"]]} | {self.board[row][self.col["E"]]} | {self.board[row][self.col["F"]]} | {self.board[row][self.col["G"]]} | {self.board[row][self.col["H"]]} |""")
                print("   ---------------------------------")
            print('     A   B   C   D   E   F   G   H  ')

    def init_game(self):

        for i in range(8):
            self.board[6][i] = Pawn("white")
            self.board[1][i] = Pawn("black")

        colour = "black"
        for i in [0,7]:
            self.board[i][0] = Rook(colour)
            self.board[i][1] = Knight(colour)
            self.board[i][2] = Bishop(colour)
            self.board[i][3] = Queen(colour)
            self.board[i][4] = King(colour)
            self.board[i][5] = Bishop(colour)
            self.board[i][6] = Knight(colour)
            self.board[i][7] = Rook(colour)
            colour = "white"

if __name__=="__main__":
    board1 = Board()
    board1.init_game()
    board1.print_board("white")