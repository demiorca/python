# Задание 6

from itertools import count, cycle


def count_func(start_num, end_num):
    for i in count(start_num):
        if i > end_num:
            break
        else:
            print(i)


count_func(int(input('Введите стартовое число: ')), int(input('Введите конечное число: ')))

"""
или:

for i in count(3):
    if i > 10:
        break
    else:
        print(i)
"""

print('*' * 57)


def cycle_func(_list, end_s):
    i = 0

    for s in cycle(_list):
        if i > end_s:
            break
        i += 1
        print(s)


song = ["In the black space", "I'll find you"]

cycle_func(song, int(input('Введите число счётчика, завершающее цикл (например, 8): ')))

"""
или:

song = ["In the black space", "I'll find you"]
i = 0

for s in cycle(song):
    if i > 8:
        break
    print(s)
    i += 1
"""
