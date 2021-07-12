# Задание 4

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
