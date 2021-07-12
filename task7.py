# Задание 7

import json

with open('test_file7.txt', 'r') as my_file:
    read_file = my_file.readlines()

    profit = {}
    positive_profit = 0
    firm_count = 0
    average_profit = {'average_profit': 0}

    for l in read_file:
        name, type_of_ownership, proceeds, costs = l.split()
        profit[name] = int(proceeds) - int(costs)
        if profit[name] >= 0:
            positive_profit += profit[name]
            firm_count += 1

    positive_profit /= firm_count
    average_profit.update(average_profit=round(positive_profit))

    profit_list = [profit, average_profit]
    print(profit_list)

with open('test_file7.json', 'w', encoding='utf-8') as my_json:
    json.dump(profit_list, my_json)
