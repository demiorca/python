# Задание 1
print('Задание 1')


class Matrix:
    def __init__(self, matrices):
        self.matrices = matrices

    def __str__(self):
        matrix1 = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrices[0]])
        matrix2 = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrices[1]])
        matrix_sum = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.__add__()])
        return f'Матрица 1:\n{matrix1}\nМатрица 2:\n{matrix2}\nСумма матриц:\n{matrix_sum}'

    def __add__(self):
        matrix = []
        for i in range(len(self.matrices[0])):
            matrix.append([])
            for j in range(len(self.matrices[0][0])):
                matrix[i].append(self.matrices[0][i][j] + self.matrices[1][i][j])
        return matrix


m3_3 = Matrix([[[14, 41, 7],
                [2, 10, 81],
                [13, 8, 4]],
               [[77, 12, 5],
                [92, 64, 1],
                [9, 23, 32]]])

m2_3 = Matrix([[[14, 41, 7],
                [2, 10, 81]],
               [[77, 12, 5],
                [92, 64, 1]]])

m3_2 = Matrix([[[14, 41],
                [2, 10],
                [13, 8]],
               [[77, 12],
                [92, 64],
                [9, 23]]])

m2_2 = Matrix([[[14, 41],
                [2, 10]],
               [[77, 12],
                [92, 64]]])

print(f'Суммирование матриц 3 на 3:\n{m3_3}')
print()
print(f'Суммирование матриц 2 на 3:\n{m2_3}')
print()
print(f'Суммирование матриц 3 на 2:\n{m3_2}')
print()
print(f'Суммирование матриц 2 на 2:\n{m2_2}')

# Задание 2
print()
print('Задание 2')

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def coat_square(self):
        pass

    @property
    @abstractmethod
    def suit_square(self):
        pass

    def __add__(self, other):
        result = self.coat_square + other.suit_square
        return f'Общий подсчёт расхода ткани под {self.v} размер и рост {other.h} равен: {result}'


class Coat(Clothes):
    def __init__(self, v):
        """
        :param v: Размер для пальто
        """
        super().__init__()
        self.v = v

    @property
    def coat_square(self):
        return round(self.v / 6.5 + 0.5, 2)

    def suit_square(self):
        pass

    def __str__(self):
        return f'Расход ткани для пальто под {self.v} размер равен: {self.coat_square}'


class Suit(Clothes):
    def __init__(self, h):
        """
        :param h: Рост для костюма
        """
        super().__init__()
        self.h = h

    @property
    def suit_square(self):
        return round(2 * self.h + 0.3, 2)

    def coat_square(self):
        pass

    def __str__(self):
        return f'Расход ткани для костюма под рост {self.h} равен: {self.suit_square}'


coat = Coat(41)
print(coat)
suit = Suit(164)
print(suit)
print(coat + suit)

# Задание 3
print()
print('Задание 3')


class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __str__(self):
        return f'Количество ячеек в клетке: {self.cells} ({"*" * self.cells})'

    def __add__(self, other):
        add_result = self.cells + other.cells
        return f'Количество ячеек в общей клетке после объединения двух путём сложения: {add_result}'

    def __sub__(self, other):
        sub_result = self.cells - other.cells
        if sub_result > 0:
            return f'Количество ячеек в общей клетке после объединения двух путём вычитания: {sub_result}'
        else:
            return 'Разность меньше 0'

    def __mul__(self, other):
        mul_result = self.cells * other.cells
        return f'Количество ячеек в общей клетке после объединения двух путём умножения: {mul_result}'

    def __truediv__(self, other):
        truediv_result = self.cells // other.cells
        return f'Количество ячеек в общей клетке после объединения двух путём деления: {truediv_result}'

    def make_order(self, cells_in_row):
        row = str()
        for i in range(self.cells // cells_in_row):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.cells % cells_in_row)}'
        return f'Ячейки клетки с рядами по {cells_in_row}: {row} ({self.cells})'


cell_1 = Cell(41)
cell_2 = Cell(14)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(5))
