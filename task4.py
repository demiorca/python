# Задание 4

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
