# Задание 1
print('Задание 1')


class Date:
    """
    Введите дату в формате 'день-месяц-год'
    """

    def __init__(self, date):
        self.date = str(date)

    def __str__(self):
        return self.date

    @classmethod
    def extract_date(cls, date):
        num_date = []
        for d in date.split('-'):
            num_date.append(int(d))
        return num_date

    @staticmethod
    def validation_date(date):
        date = date.split('-')
        if 1 <= int(date[0]) <= 31:
            pass
        else:
            print('Исправьте день')
        if 1 <= int(date[1]) <= 12:
            pass
        else:
            print('Исправьте месяц')
        if 1 <= int(date[2]) <= 2021:
            pass
        else:
            print('Исправьте год')
        if 1 <= int(date[0]) <= 31 and 1 <= int(date[1]) <= 12 and 1 <= int(date[2]) <= 2021:
            return 'Дата введена корректно'
        else:
            return 'Дата введена некорректно'

    """
    или:

    @staticmethod
    def validation_date(date):
        date = date.split('-')
        if 1 <= int(date[0]) <= 31 and 1 <= int(date[1]) <= 12 and 1 <= int(date[2]) <= 2021:
            return 'Дата введена корректно'
        else:
            return 'Исправьте дату. День - от 1 до 31, месяц - от 1 до 12, год - от 1 до 2021.'
    """


my_date = Date('19-07-2021')
print(my_date)
print(Date.extract_date('19-07-2021'))
print(Date.validation_date('19-07-2021'))
print()
print(Date.validation_date('99-99-9999'))

# Задание 2
print()
print('Задание 2')


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

# Задание 3
print()
print('Задание 3')


class OnlyNumberInList(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []

while True:
    data = input('Введите данные: ')
    if data.lower() == 'stop':
        break
    try:
        if not data.replace('.', '').isdigit():
            raise OnlyNumberInList('Для ввода допускаются только цифры.')
        if '.' in data:
            num_list.append(float(data))
        else:
            num_list.append(int(data))
    except OnlyNumberInList as err:
        print(err)

print(num_list)

# Задание 7
print()
print('Задание 7')


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        if self.imaginary_part < 0:
            return f'{self.real_part}+({self.imaginary_part})i'
        else:
            return f'{self.real_part}+{self.imaginary_part}i'

    def __add__(self, other):
        return ComplexNumber((self.real_part + other.real_part), (self.imaginary_part + other.imaginary_part))

    def __mul__(self, other):
        return ComplexNumber((self.real_part * other.real_part - self.imaginary_part * other.imaginary_part),
                             (self.real_part * other.imaginary_part + other.real_part * self.imaginary_part))


complex_number1 = ComplexNumber(2, 7)
complex_number2 = ComplexNumber(6, -5)
complex_number3 = ComplexNumber(5, 4)
print(f'z1 = {complex_number1}')
print(f'z2 = {complex_number2}')
print(f'z3 = {complex_number3}')
print()
z1 = complex_number1 + complex_number2
print(f'z = ({complex_number1}) + ({complex_number2}) = {z1}')
z2 = complex_number1 * complex_number2
print(f'z = ({complex_number1}) * ({complex_number2}) = {z2}')
z3 = complex_number1 + complex_number2 + complex_number3
print(f'z = ({complex_number1}) + ({complex_number2}) + ({complex_number3}) = {z3}')
z4 = complex_number1 * complex_number2 * complex_number3
print(f'z = ({complex_number1}) * ({complex_number2}) * ({complex_number3}) = {z4}')
