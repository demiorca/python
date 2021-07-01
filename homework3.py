# Задание 1
print('Задание 1')


def division(dividend, divisor):
    try:
        quotient = dividend / divisor
        return quotient
    except ZeroDivisionError:
        return 'Делить на 0 нельзя'


print(division(int(input('Введите делимое: ')), int(input('Введите делитель: '))))


# Задание 2
print('Задание 2')


def user_info(name=None, surname=None, birthday=None, city=None, email=None, phone=None):
    return print(f'{name}, {surname}, {birthday}, {city}, {email}, {phone}')


user_info(name='name', surname='surname', birthday='birthday', city='city', email='email', phone='phone')


# Задание 3
print('Задание 3')


def my_func():
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите число: '))
    num3 = int(input('Введите число: '))
    my_list = [num1, num2, num3]
    new_list = []
    for i in my_list:
        max_num = max(my_list)
        new_list.append(max_num)
        my_list.remove(max_num)
    return sum(new_list)


print(my_func())


# Задание 4
print('Задание 4')


# 1-й способ

def my_func(x, y):
    _pow = 1 / x ** abs(y)
    return _pow


print(my_func(float(input('Введите число: ')), int(input('Введите отрицательное число: '))))


# 2-й способ

def my_func(x, y):
    result = 1
    if y < 0:
        while y < 0:
            result *= 1 / x
            y += 1
    else:
        while y > 0:
            result *= 1 / x
            y -= 1
    return result


print(my_func(float(input('Введите число: ')), int(input('Введите отрицательное число: '))))


# Задание 5
print('Задание 5')


def num_sum():
    total = 0
    exit_symbol = False
    while not exit_symbol:
        number = input('Введите число или числа через пробел, либо символ Q (в любом регистре) для выхода: ').split()
        result = 0
        for i in range(len(number)):
            if number[i] == 'Q' or number[i] == 'q':
                exit_symbol = True
                break
            else:
                result += int(number[i])
        total += result
        print(f'Текущий результат равен {total}')
    return f'Итоговый результат равен {total}'


print(num_sum())


# Задания 6 и 7
print('Задания 6 и 7')


def int_func(text):
    return text.title()


print(int_func('text'))


def new_int_func():
    _string = input('Введите строку из слов, разделённых пробелами: ').lower()
    return int_func(_string)


print(new_int_func())
