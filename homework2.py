# Задание 1
print('Задание 1')

data_list = [41, 'python', True, 36.6, (1, 2), [3, 4], {5, 6}, {'a': 'b', 'c': 'd'}, 1+2j]

for l in data_list:
    print(type(l))


# Задание 2
print('Задание 2')

data_list = []
pos = 0

while len(data_list) < 7:
    data_list.append(input())

for p in range(int(len(data_list) / 2)):
    data_list[pos], data_list[pos + 1] = data_list[pos + 1], data_list[pos]
    pos += 2

print(data_list)


# Задание 3
print('Задание 3')

season = int(input('Введите цифру месяца в виде целого числа от 1 до 12: '))

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = dict(winter='зима', spring='весна', summer='лето', autumn='осень')

if season == 1 or season == 2 or season == 12:
    print(f'Выбранный вами месяц - это {seasons_list[0]}')
    print(f'Выбранный вами месяц - это {seasons_dict.get("winter")}')
elif season == 3 or season == 4 or season == 5:
    print(f'Выбранный вами месяц - это {seasons_list[1]}')
    print(f'Выбранный вами месяц - это {seasons_dict.get("spring")}')
elif season == 6 or season == 7 or season == 8:
    print(f'Выбранный вами месяц - это {seasons_list[2]}')
    print(f'Выбранный вами месяц - это {seasons_dict.get("summer")}')
elif season == 9 or season == 10 or season == 11:
    print(f'Выбранный вами месяц - это {seasons_list[3]}')
    print(f'Выбранный вами месяц - это {seasons_dict.get("autumn")}')
else:
    print('Введите цифру месяца в виде целого числа от 1 до 12')


# Задание 4
print('Задание 4')

string = input('Введите строку из слов, разделённых пробелами: ')
new_string = string.split(' ')

for i, k in enumerate(new_string, 1):
    if len(k) > 10:
        k = k[0:10]
    print(f'{i}) {k}')


# Задание 5
print('Задание 5')

num = int(input('Введите цифру: '))
my_list = [7, 5, 3, 3, 2]
cnt = my_list.count(num)

for i in my_list:
    if cnt > 0:
        idx = my_list.index(num)
        my_list.insert(idx + cnt, num)
        break
    else:
        if num > i:
            j = my_list.index(i)
            my_list.insert(j, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)

print(my_list)
