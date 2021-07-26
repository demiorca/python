# Задание 3

class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __str__(self):
        return f'Количество ячеек в клетке: {self.cells} ({"*" * self.cells})'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            return 'Разность меньше 0.'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        try:
            return Cell(self.cells // other.cells)
        except ZeroDivisionError:
            return 'Делить на 0 нельзя. У одной из клеток 0 ячеек.'

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
