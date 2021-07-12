# Задание 5

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
