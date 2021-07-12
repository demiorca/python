# Задание 6

with open('test_file6.txt', 'r') as my_file:
    read_file = my_file.readlines()
    subjects_dict = {}
    for l in read_file:
        name, hours = l.split(':')
        total = sum(map(int, "".join([i for i in hours if i == ' ' or i in '0123456789']).split()))
        subjects_dict[name] = total
    print(subjects_dict)
