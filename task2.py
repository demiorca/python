# Задание 2

my_list = [4, 41, 14, 99, 101, 300, 81, 1, 2021]
result = [i for i in my_list if i > my_list[my_list.index(i) - 1]]

print(f'Исходный список: {my_list}')
print(f'Результат: {result}')
