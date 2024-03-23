class Board:
    def __init__(self):
        self.row1 = [" ", " ", " "]
        self.row2 = [" ", " ", " "]
        self.row3 = [" ", " ", " "]

    def draw(self):
        print(
            f"""
     |     |
  {self.row1[0]}  |  {self.row1[1]}  |  {self.row1[2]}
-----|-----|-----
  {self.row2[0]}  |  {self.row2[1]}  |  {self.row2[2]}
-----|-----|----- 
  {self.row3[0]}  |  {self.row3[1]}  |  {self.row3[2]}
     |     |
"""
        )

    def make_move(self, piece, row, col):
        if (row in ["0", "1", "2"]) and (col in ["0", "1", "2"]):
            row = int(row)
            col = int(col)

            if (row == 0) and self.row1[col] == " ":
                self.row1[col] = piece
                return True
            elif (row == 1) and self.row2[col] == " ":
                self.row2[col] = piece
                return True
            elif (row == 2) and self.row3[col] == " ":
                self.row3[col] = piece
                return True
            else:
                return False
        else:
            return False

    def check_winner(self):
        if self.row1[0] == self.row1[1] == self.row1[2] != " ":
            return self.row1[0]
        elif self.row2[0] == self.row2[1] == self.row2[2] != " ":
            return self.row2[0]
        elif self.row3[0] == self.row3[1] == self.row3[2] != " ":
            return self.row3[0]
        elif self.row1[0] == self.row2[0] == self.row3[0] != " ":
            return self.row1[0]
        elif self.row1[1] == self.row2[1] == self.row3[1] != " ":
            return self.row1[1]
        elif self.row1[2] == self.row2[2] == self.row3[2] != " ":
            return self.row1[2]
        elif self.row1[0] == self.row2[1] == self.row3[2] != " ":
            return self.row1[0]
        elif self.row3[0] == self.row2[1] == self.row1[2] != " ":
            return self.row3[0]

    def is_full(self):
        if " " in self.row1:
            return False
        elif " " in self.row2:
            return False
        elif " " in self.row3:
            return False
        else:
            return True
