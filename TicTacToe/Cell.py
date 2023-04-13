# null_0bject

class Cell:

    def __init__(self):
        self.value = 0

    def __bool__(self):
        return True if self.value == 0 else False

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other

    def __int__(self):
        return self.value
