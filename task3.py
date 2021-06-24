# Задание 3

n = int(input('Введите число: '))

if n > 0:
    result = int(str(n)) + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
    print(result)
else:
    print('Введите положительное число')
