# null.øbject
import random as rd
from Cell import Cell


class TicTacToe:

    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    pole = (Cell(0, 0), Cell(0, 1), Cell(0, 2),
            Cell(1, 0), Cell(1, 1), Cell(1, 2),
            Cell(2, 0), Cell(2, 1), Cell(2, 2))

    def __init__(self):
        for i in TicTacToe.pole:
            i.value = 0

        self.pole = list(TicTacToe.pole)
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def __repr__(self):
        for row in range(3):
            buffer = []
            for column in range(3):
                if self[row, column].value == 0:
                    buffer.append('ø')
                elif self[row, column].value == 1:
                    buffer.append('X')
                else:
                    buffer.append('O')
            print(' '.join(buffer))
        return str()

    def __getitem__(self, pos):
        row, column = pos
        if 0 <= row <= 2 and 0 <= column <= 2:
            for i in self.pole:
                if i.row == row and i.column == column:
                    return i
        else:
            raise IndexError('некорректно указанные индексы')

    def __setitem__(self, pos, new_value):
        self.__getitem__(pos).value = new_value
        self.game_check()

    def show(self):
        for row in range(3):
            buffer = []
            for column in range(3):
                if self[row, column].value == 0:
                    buffer.append('ø')
                elif self[row, column].value == 1:
                    buffer.append('X')
                else:
                    buffer.append('O')
            print(' '.join(buffer))

    def human_go(self):
        if not bool(self):
            return True

        while True:
            pos = list(map(int, input('Введите координаты клетки через пробел \n').split()))
            # INDEX CHECK ----------------------------------------------------
            if not(len(pos) == 2 and 0 <= pos[0] <= 2 and 0 <= pos[1] <= 2):
                print('Введён неверный индекс')
                continue
            # ---------------------------------------------------- INDEX CHECK
            if self[pos].value == 0:
                self.__setitem__(pos, 1)
                return self.game_check()
            else:
                print('Введена занятая ячейка, введите другое значение ')

    def computer_go(self):
        if not bool(self):
            return True

        while True:
            pos = [rd.randint(0, 2), rd.randint(0, 2)]
            if self[pos].value == 0:
                self.__setitem__(pos, 2)
                break

        self.game_check()

    def __bool__(self):
        return False if (self.is_draw or self.is_computer_win or self.is_human_win) else True

    def game_check(self):

        if not bool(self):
            return True

        # DRAW
        if len([i for i in self.pole if i.value == 0]) == 0:
            self.is_draw = True
            return True

        # ROW VICTORY
        for row in range(0, 3):
            buffer = set()
            for column in range(0, 3):
                buffer.add(self[row, column].value)

            if len(buffer) == 1:
                if sum(buffer) == 1:
                    self.is_human_win = True
                    return True
                if sum(buffer) == 2:
                    self.is_computer_win = True
                    return True

        # COLUMN VICTORY
        for column in range(0, 3):
            buffer = set()
            for row in range(0, 3):
                buffer.add(self[row, column].value)

            if len(buffer) == 1:
                if sum(buffer) == 1:
                    self.is_human_win = True
                    return True
                if sum(buffer) == 2:
                    self.is_computer_win = True
                    return True

        # DIAGONAL VICTORY
        if self.pole[2].value == self.pole[4].value == self.pole[6].value:

            if self.pole[2].value == 1:
                self.is_human_win = True
                return True

            elif self.pole[2].value == 2:
                self.is_computer_win = True
                return True

        if self.pole[0].value == self.pole[4].value == self.pole[8].value:

            if self.pole[0].value == 1:
                self.is_human_win = True
                return True
            elif self.pole[0].value == 2:
                self.is_computer_win = True
                return True

    def init(self):
        for i in TicTacToe.pole:
            i.value = 0
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False


