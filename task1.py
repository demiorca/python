# Задание 1

def division(dividend, divisor):
    try:
        quotient = dividend / divisor
        return quotient
    except ZeroDivisionError:
        return 'Делить на 0 нельзя'


print(division(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
