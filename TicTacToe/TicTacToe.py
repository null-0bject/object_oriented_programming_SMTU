import random as rd
from Cell import Cell


class TicTacToe:

    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    pole = ([Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()])

    def __init__(self):

        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def __getitem__(self, pos: tuple):
        if len(pos) != 2 or type(pos[0]) != int or type(pos[1]) != int \
                or not (-1 < (pos[0]) < 3) or not (-1 < (pos[1]) < 3):
            raise IndexError('некорректно указанные индексы')

        row, column = pos
        return self.pole[row][column]

    def __setitem__(self, pos: tuple, new_value: int):
        self.__getitem__(pos).value = new_value
        self.game_check()

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

    def __bool__(self):
        return not(self.is_draw or self.is_human_win or self.is_computer_win)

    def show(self):
        for row in range(3):
            buffer = []
            for column in range(3):
                if self[row, column].value == TicTacToe.FREE_CELL:
                    buffer.append('ø')
                elif self[row, column].value == TicTacToe.HUMAN_X:
                    buffer.append('X')
                else:
                    buffer.append('0')
            print(' '.join(buffer))

    def game_check(self):
        if not(bool(self)):
            return 'Игра уже окончена'
        # DRAW ---------------------------
        draw_flag = True
        for row in self.pole:
            for column in row:
                if column.value == TicTacToe.FREE_CELL:
                    draw_flag = False

        if draw_flag:
            self.is_draw = True
            return 'Ничья'
        # --------------------------- DRAW

        # ROW VICTORY
        for row in self.pole:
            if len(set(map(int, row))) == 1:
                match sum(set(map(int, row))):
                    case 1:
                        self.is_human_win = True
                        return 'Победил Человек'
                    case 2:
                        self.is_computer_win = True
                        return 'Победил Компьютер'
                    case _:
                        continue

        # COLUMN VICTORY
        for column in range(0, 3):
            buffer = set()
            for row in range(0, 3):
                buffer.add(self[row, column].value)

            if len(buffer) == 1:
                if sum(buffer) == 1:
                    self.is_human_win = True
                    return 'Победил Человек'
                if sum(buffer) == 2:
                    self.is_computer_win = True
                    return 'Победил Компьютер'

        # DIAGONAL VICTORY
        if (self[0, 0].value == self[1, 1].value == self[2, 2].value) or \
                (self[0, 2].value == self[1, 1].value == self[2, 0].value):

            if self[1, 1].value == TicTacToe.HUMAN_X:
                self.is_human_win = True
                return 'Победил Человек'

            elif self[1, 1].value == TicTacToe.COMPUTER_O:
                self.is_computer_win = True
                return 'Победил Компьютер'

    def human_go(self):
        if not(bool(self)):
            return None
        while True:
            pos = tuple(map(int, input('Введите координаты клетки через пробел \n').split()))
            # INDEX CHECK ----------------------------------------------------
            if not (len(pos) == 2 and 0 <= pos[0] <= 2 and 0 <= pos[1] <= 2):
                print('Введён неверный индекс')
                continue
            # ---------------------------------------------------- INDEX CHECK
            if self[pos].value == 0:
                self.__setitem__(pos, 1)
                self.game_check()
                break
            else:
                print('Введена занятая ячейка, введите другое значение ')

    def computer_go(self):
        if not(bool(self)):
            return None
        while True:
            pos = tuple([rd.randint(0, 2), rd.randint(0, 2)])
            if self[pos].value == 0:
                self.__setitem__(pos, TicTacToe.COMPUTER_O)
                self.game_check()
                break

    def init(self):
        self.pole = tuple(TicTacToe.pole)
        for row in self.pole:
            for column in row:
                column.value = 0
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

