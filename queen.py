from figure import Figure

class Queen(Figure):
    def __init__(self, colour):
        super().__init__(colour)

    def __str__(self):
        return "Q"