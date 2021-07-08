# Задание 5

with open('test_file5.txt', 'w', encoding='utf-8') as my_file:
    line_input = input('Введите числа через пробел: ')
    line_input = line_input.split()
    line_input = [int(i) for i in line_input]
    result = sum(line_input)
    print(result)
    line_input = ' '.join(map(str, line_input))
    my_file.write(f'{line_input}\n')
