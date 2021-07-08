# Задание 1
print('Задание 1')

with open('test_file.txt', 'w', encoding='utf-8') as my_file:
    while True:
        line_input = input('Введите данные: ')
        my_file.write(f'{line_input}\n')
        if line_input == '':
            break

with open('test_file.txt', 'r') as my_file_r:
    read_file = my_file_r.read()
    print(read_file)

# Задание 2
print('')
print('Задание 2')

with open('test_file2.txt', 'r') as my_file:
    read_file = my_file.readlines()
    print(read_file)
    lines = 0
    for l in read_file:
        lines += l.count('\n')
        words = len(l.split())
        print(f'Количество слов в {lines} строке: {words}')
    print(f'Количество строк в файле: {lines}')

# Задание 3
print('')
print('Задание 3')

with open('test_file3.txt', 'r') as my_file:
    read_file = my_file.readlines()
    print(read_file)
    print('')
    employees = 0
    salary = 0
    print('Список сотрудников с окладом менее 20000 кредитов:')
    for l in read_file:
        l = l.split()
        employees += l.count(str) + 1
        salary += int(l[1])
        if int(l[1]) < 20000:
            print(l[0])
    print('*' * 52)
    print(f'Всего сотрудников в компании: {employees}')
    print(f'Средняя зарплата всех сотрудников: {round(salary / employees, 2)} кредитов')

# Задание 4
print('')
print('Задание 4')

with open('test_file4.txt', 'r') as my_file:
    read_file = my_file.readlines()
    print(read_file)
    russificator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    rus_keys = (k for k in russificator.keys())
    rus_values = (k for k in russificator.values())
    new_file = []
    for l in read_file:
        l = l.split()
        try:
            if l[0] == next(rus_keys):
                l[0] = next(rus_values)
                l[-1] += '\n'
                new_file.append(l)
        except StopIteration:
            break
        print(l)
    new_file = [' '.join(i) for i in new_file]

with open('test_file4_new.txt', 'w', encoding='utf-8') as my_new_file:
    my_new_file.writelines(new_file)

# Задание 5
print('')
print('Задание 5')

with open('test_file5.txt', 'w', encoding='utf-8') as my_file:
    line_input = input('Введите числа через пробел: ')
    line_input = line_input.split()
    line_input = [int(i) for i in line_input]
    result = sum(line_input)
    print(result)
    line_input = ' '.join(map(str, line_input))
    my_file.write(f'{line_input}\n')

# Задание 6
print('')
print('Задание 6')

with open('test_file6.txt', 'r') as my_file:
    read_file = my_file.readlines()
    subjects_dict = {}
    for l in read_file:
        name, hours = l.split(':')
        total = sum(map(int, "".join([i for i in hours if i == ' ' or i in '0123456789']).split()))
        subjects_dict[name] = total
    print(subjects_dict)
