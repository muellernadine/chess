from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King

class Board:
    def __init__(self):
        self.rows = []
        for i in range(8):
            row = []
            for j in range(8):
                col = " "
                row.append(col)
            self.rows.append(row)

    def print_board(self):
        print("   ---------------------------------")
        for i in range(7,-1,-1):
            print(f""" {i+1} | {self.rows[i][0]} | {self.rows[i][1]} | {self.rows[i][2]} | {self.rows[i][3]} | {self.rows[i][4]} | {self.rows[i][5]} | {self.rows[i][6]} | {self.rows[i][7]} |""")
            print("   ---------------------------------")
        print('     A   B   C   D   E   F   G   H  ')

    def init_game(self):

        for i in range(8):
            self.rows[6][i] = Pawn("white")
            self.rows[1][i] = Pawn("black")

        colour = "black"
        for i in [0,7]:
            self.rows[i][0] = Rook(colour)
            self.rows[i][1] = Knight(colour)
            self.rows[i][2] = Bishop(colour)
            self.rows[i][3] = Queen(colour)
            self.rows[i][4] = King(colour)
            self.rows[i][5] = Bishop(colour)
            self.rows[i][6] = Knight(colour)
            self.rows[i][7] = Rook(colour)
            colour = "white"

if __name__=="__main__":
    board1 = Board()
    board1.init_game()
    board1.print_board()