# Задание 3

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
            raise OnlyNumberInList('Для ввода допускаются только числа.')
        if '.' in data:
            num_list.append(float(data))
        else:
            num_list.append(int(data))
    except OnlyNumberInList as err:
        print(err)

print(num_list)
