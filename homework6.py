# Задание 1
print('Задание 1')

from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0

        if self.__color[0] == 'Red' and self.__color[1] == 'Yellow' and self.__color[2] == 'Green' in self.__color:
            while i < 6: # или while True для бесконечного цикла, тогда счётчик i не нужен
                for c in self.__color[0::len(self.__color) - 1]:
                    print(c)
                    i += 1
                    if c[0]:
                        sleep(7)
                    elif c[2]:
                        sleep(5)
                    print(self.__color[1])
                    sleep(2)
        else:
            print('Нарушен порядок режимов переключения')


traffic_light = TrafficLight()
traffic_light.running()

# Задание 2
print()
print('Задание 2')


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

# Задание 3
print()
print('Задание 3')


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        print(f'Имя: {name}, фамилия: {surname}, должность: {position.lower()}, '
              f'оклад: {wage} кредитов, премия: {bonus} кредитов')


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Имя и фамилия сотрудника на должности "{self.position}": {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход сотрудника на должности "{self.position}" с учётом премии: {sum(self._income.values())} кредитов'


worker_1 = Position("Джеймс", "Кирк", "Командующий", 100000, 50000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())

print()

worker_2 = Position("С'чн-Т'гай", "Спок", "Офицер по науке", 80000, 30000)
print(worker_2.get_full_name())
print(worker_2.get_total_income())

# Задание 4
print()
print('Задание 4')


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if is_police is True:
            is_police = 'полицейский'
        else:
            is_police = 'гражданский'
        print(f'Автомобиль {name}, {color} цвет, скорость {speed} км/ч, {is_police}')

    def go(self):
        return f'Автомобиль {self.name} едет'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        """
        Напишите "right", если автомобиль должен повернуть направо, либо "left", если налево
        """
        if direction == "right":
            return f'Автомобиль {self.name} повернул направо'
        elif direction == "left":
            return f'Автомобиль {self.name} повернул налево'

    def show_speed(self):
        return f'{self.speed} км/ч'


class TownCar(Car):
    """
    Городской автомобиль
    """
    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} км/ч, что превышает допустимое значение в 60 км/ч'
        else:
            return f'{self.speed} км/ч'


class SportCar(Car):
    """
    Спортивный автомобиль
    """
    pass


class WorkCar(Car):
    """
    Рабочий автомобиль
    """
    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} км/ч, что превышает допустимое значение в 40 км/ч'
        else:
            return f'{self.speed} км/ч'


class PoliceCar(Car):
    """
    Полицейский автомобиль
    """
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


mazda = TownCar(75, 'синий', 'Mazda MX-5')
nissan = SportCar(120, 'красный', 'Nissan GT-R')
zil = WorkCar(64, 'зелёный', 'ЗИЛ-131')
ford = PoliceCar(80, 'белый', 'Ford Crown Victoria')

print()
print(f'{nissan.go()} со скоростью {nissan.show_speed()}.')
print(f'{nissan.turn("right")}.')
print(f'{nissan.stop()}.')
print()
print(f'{mazda.go()} со скоростью {mazda.show_speed()}.')
print(f'{mazda.turn("left")}.')
print(f'{mazda.stop()}.')
print()
print(f'{zil.go()} со скоростью {zil.show_speed()}.')
print(f'{zil.turn("right")}.')
print(f'{zil.stop()}.')
print()
print(f'{ford.go()} со скоростью {ford.show_speed()}.')
print(f'{ford.turn("left")}.')
print(f'{ford.stop()}, когда догнал превышающего скорость водителя {mazda.name}.')
print(f'Полицейский на {ford.name} по рации сообщил коллеге, что автомобиль {zil.name} превышает скорость на '
      f'перпендикулярной улице.')

# Задание 5
print()
print('Задание 5')


class Stationery:
    def __init__(self, title='Рисование'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title='ручка'):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки. Используется {self.title}.')


class Pencil(Stationery):
    def __init__(self, title='карандаш'):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки. Используется {self.title}.')


class Handle(Stationery):
    def __init__(self, title='маркер'):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки. Используется {self.title}.')


stationery = Stationery()
stationery.draw()
print()

pen = Pen()
pen.draw()
print()

pencil = Pencil()
pencil.draw()
print()

handle = Handle()
handle.draw()
