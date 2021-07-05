# Задание 1

from sys import argv

try:
    script_name, working_hours, working_rate, working_bonus = argv
    print(f'Имя скрипта: {script_name}')
    print(f'Расчёт заработной платы сотрудника: {int(working_hours) * int(working_rate) + int(working_bonus)}')
except ValueError:
    print('Not enough values to unpack')

'''
или:

from sys import argv

script_name, working_hours, working_rate, working_bonus = argv

salary = int(working_hours) * int(working_rate) + int(working_bonus)

print(f'Имя скрипта: {script_name}')
print(f'Расчёт заработной платы сотрудника: {salary}')
'''

