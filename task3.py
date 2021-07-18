# Задание 3

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
