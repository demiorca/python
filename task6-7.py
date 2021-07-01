# Задания 6 и 7

def int_func(text):
    return text.title()


print(int_func('text'))


def new_int_func():
    _string = input('Введите строку из слов, разделённых пробелами: ').lower()
    return int_func(_string)


print(new_int_func())
