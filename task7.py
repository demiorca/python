# Задание 7

from itertools import count
from math import factorial


def fact(n):
    for i in count(n):
        yield f'{i}! = {factorial(i)}'


x = 0
n = int(input('Введите крайнее число, по которому нужно посчитать факториал: '))

for i in fact(1):
    if x < n:
        print(i)
        x += 1
    else:
        break
