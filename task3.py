# Задание 3


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
