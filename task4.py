# Задание 4

my_list = [4, 4, 4, 4, 41, 14, 99, 99, 99, 101, 101, 300, 81, 81, 1, 1, 1, 2021]
new_list = [i for i in my_list if my_list.count(i) < 2]

print(new_list)
