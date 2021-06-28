# Задание 4

string = input('Введите строку из слов, разделённых пробелами: ')
new_string = string.split(' ')

for i, k in enumerate(new_string, 1):
    if len(k) > 10:
        k = k[0:10]
    print(f'{i}) {k}')
