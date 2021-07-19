# Задание 2

class ZeroDivErr(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend = float(input('Введите делимое: '))
    divisor = float(input('Введите делитель: '))
    if divisor == 0:
        raise ZeroDivErr('Делитель равен 0. На 0 делить нельзя!')
    number = dividend / divisor
except ValueError:
    print('Введён другой тип данных. Напишите число.')
except ZeroDivErr as err:
    print(err)
else:
    print(f'{dividend} / {divisor} = {number}')
finally:
    print('Расчёт окончен.')
