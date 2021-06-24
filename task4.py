# Задание 4

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
