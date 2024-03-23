class Player:
    def __init__(self, name, piece, board):
        self.name = name
        self.piece = piece
        self.board = board

    def get_input(self):
        print(f"Current turn: {self.name} ({self.piece})")
        row = input("Enter a row number (0~2): ")
        col = input("Enter a column number (0~2): ")
        result = self.board.make_move(self.piece, row, col)
        return result
