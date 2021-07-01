# Задание 4

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
