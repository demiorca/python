from sys import argv  # для задания 1
from functools import reduce  # для задания 5
from itertools import cycle  # для задания 6
from itertools import count  # для заданий 6 и 7
from math import factorial  # для задания 7

# Задание 1
print('Задание 1')

try:
    script_name, working_hours, working_rate, working_bonus = argv

    print(f'Имя скрипта: {script_name}')
    print(f'Расчёт заработной платы сотрудника: {int(working_hours) * int(working_rate) + int(working_bonus)}')
except ValueError:
    print('Not enough values to unpack')

'''
или:

from sys import argv

try:
    script_name, working_hours, working_rate, working_bonus = argv
    
    salary = int(working_hours) * int(working_rate) + int(working_bonus)
    
    print(f'Имя скрипта: {script_name}')
    print(f'Расчёт заработной платы сотрудника: {salary}')
except ValueError:
    print('Not enough values to unpack')  
'''

# Задание 2
print('Задание 2')

my_list = [4, 41, 14, 99, 101, 300, 81, 1, 2021]
result = [i for i in my_list if i > my_list[my_list.index(i) - 1]]

print(f'Исходный список: {my_list}')
print(f'Результат: {result}')

# Задание 3
print('Задание 3')

print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

# Задание 4
print('Задание 4')

my_list = [4, 4, 4, 4, 41, 14, 99, 99, 99, 101, 101, 300, 81, 81, 1, 1, 1, 2021]
new_list = [i for i in my_list if my_list.count(i) < 2]

print(new_list)

# Задание 5
print('Задание 5')


def my_func(prev_el, el):
    return prev_el * el


my_list = [i for i in range(100, 1001, 2)] # или [i for i in range(100, 1001) if i % 2 == 0]

print(my_list)
print(reduce(my_func, my_list))

# Задание 6
print('Задание 6')


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

# Задание 7
print('Задание 7')


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
