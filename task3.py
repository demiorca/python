# Задание 3

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
