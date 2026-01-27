from figure import Figure

class Rook(Figure):
    def __init__(self, colour):
        super().__init__(colour)

    def __str__(self):
        return "R"