# Задание 1

with open('test_file.txt', 'w', encoding='utf-8') as my_file:
    while True:
        line_input = input('Введите данные: ')
        my_file.write(f'{line_input}\n')
        if line_input == '':
            break

with open('test_file.txt', 'r') as my_file_r:
    read_file = my_file_r.read()
    print(read_file)
