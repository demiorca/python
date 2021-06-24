# Задание 5

proceeds = int(input('Введите выручку компании: '))
costs = int(input('Введите издержки компании: '))

if proceeds > costs:
    profit = proceeds - costs
    profitability = profit / proceeds * 100
    print(f'Прибыль — выручка больше издержек на {profit} кредитов')
    print(f'Рентабельность выручки составляет {profitability:.2f}%')
    employees = int(input('Введите количество сотрудников компании: '))
    print(f'Прибыль компании в расчёте на одного сотрудника составляет {(profit / employees):.2f} кредитов')
elif proceeds == costs:
    print('Выручка равна издержкам')
else:
    print('Убыток — издержки больше выручки')
