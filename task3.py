# Задание 3

season = int(input('Введите цифру месяца в виде целого числа от 1 до 12: '))

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = dict(winter='зима', spring='весна', summer='лето', autumn='осень')

if season == 1 or season == 2 or season == 12:
    print(f'Выбранный вами месяц - это {seasons_list[0]}')
    print(f'Выбранный вами месяц - это {seasons_dict.get("winter")}')
elif season == 3 or season == 4 or season == 5:
    print(f'Выбранный вами месяц - это {seasons_list[1]}')
    print(f'Выбранный вами месяц - это {seasons_dict.get("spring")}')
elif season == 6 or season == 7 or season == 8:
    print(f'Выбранный вами месяц - это {seasons_list[2]}')
    print(f'Выбранный вами месяц - это {seasons_dict.get("summer")}')
elif season == 9 or season == 10 or season == 11:
    print(f'Выбранный вами месяц - это {seasons_list[3]}')
    print(f'Выбранный вами месяц - это {seasons_dict.get("autumn")}')
else:
    print('Введите цифру месяца в виде целого числа от 1 до 12')
