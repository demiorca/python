# Задание 7

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
