# Задание 2

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
