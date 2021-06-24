# Задание 1
print('Задание 1')

_str = 'string'
_int = 41
_float = 3.14
_bool = True

print(f'{_str}, {_int}, {_float}, {_bool}')

get_str = input('Введите строку: ')
get_inum = int(input('Введите целое число: '))
get_fnum = float(input('Введите вещественное число (через точку): '))

print(f'{get_str}, {get_inum}, {get_fnum}')


# Задание 2
print('Задание 2')

seconds = int(input('Введите время в секундах: '))
minutes = seconds // 60
hours = minutes // 60

print('%02d:%02d:%02d' % (hours, minutes % 60, seconds % 60))


# Задание 3
print('Задание 3')

n = int(input('Введите число: '))

if n > 0:
    result = int(str(n)) + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
    print(result)
else:
    print('Введите положительное число')


# Задание 4
print('Задание 4')

n = int(input('Введите целое положительное число: '))
max_num = 0

if n > 0:
    while n > 0:
        last_num = n % 10
        if last_num >= max_num:
            max_num = last_num
        n = n // 10
    print(max_num)
else:
    print('Введите целое положительное число')


# Задание 5
print('Задание 5')

proceeds = int(input('Введите выручку компании: '))
costs = int(input('Введите издержки компании: '))

if proceeds > costs:
    profit = proceeds - costs
    profitability = profit / proceeds * 100
    print(f'Прибыль — выручка больше издержек на {profit} кредитов')
    print(f'Рентабельность выручки составляет {profitability:.2f}%')
    employees = int(input('Введите количество сотрудников компании: '))
    print(f'Прибыль компании в расчёте на одного сотрудника составляет {(profit / employees):.2f} кредитов')
elif proceeds == costs:
    print('Выручка равна издержкам')
else:
    print('Убыток — издержки больше выручки')


# Задание 6
print('Задание 6')

a = int(input('Введите начальный результат: '))
b = int(input('Введите желаемый результат: '))
day = 1

while a < b:
    print(f'{day}-й день: {a:.2f}')
    a = a + 0.1 * a
    day += 1

print(f'Желаемый результат будет достигнут на {day}-й день!')
