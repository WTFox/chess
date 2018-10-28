class Coordinates:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __repr__(self):
        return "({},{})".format(self.row, self.column)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.row == other.row and self.column == other.column
