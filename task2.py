# Задание 2

class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def mass_calculation(self, mass_per_cm, thickness):
        return f'Расчёт массы асфальта, необходимого для покрытия всей дороги: ' \
               f'{self._width} м * {self._length} м * {mass_per_cm} кг * {thickness} см = ' \
               f'{(self._width * self._length * mass_per_cm * thickness) / 1000} т.'


mass_calculation = Road(20, 5000)
print(mass_calculation.mass_calculation(25, 5))
