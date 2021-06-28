# Задание 5

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
