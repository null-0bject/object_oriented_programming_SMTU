# null_0bject

class Cell:

    def __init__(self, row=None, column=None):
        self.row = row
        self.column = column
        self.value = 0

    def __bool__(self):
        return True if self.value == 0 else False

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other




