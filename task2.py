# Задание 2

with open('test_file2.txt', 'r') as my_file:
    read_file = my_file.readlines()
    print(read_file)
    lines = 0
    for l in read_file:
        lines += l.count('\n')
        words = len(l.split())
        print(f'Количество слов в {lines} строке: {words}')
    print(f'Количество строк в файле: {lines}')
