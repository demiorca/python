# Задание 5

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
