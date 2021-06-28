# Задание 2

data_list = []
pos = 0

while len(data_list) < 7:
    data_list.append(input())

for p in range(int(len(data_list) / 2)):
    data_list[pos], data_list[pos + 1] = data_list[pos + 1], data_list[pos]
    pos += 2

print(data_list)
