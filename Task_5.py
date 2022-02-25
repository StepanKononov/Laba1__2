import matplotlib.pyplot as plt
import math
import gspread
import random

sa = gspread.service_account(filename="TokenKey.json")
sh = sa.open("FirstLab")
wh = sh.worksheet("Data")

n = math.ceil(math.sqrt(17) * 10)
n = 10
print("Ввод диапазон  значений через \"-\"")
first, second = map(int, input().split("-"))

max_count = max(first, second)
min_count = min(first, second)

xy = 0
xx = 0
x = 0
y = 0

if max_count - min_count >= n:

    x_data = []
    y_data = []

    while len(x_data) != n:
        temp = random.randint(min_count, max_count)
        if temp not in x_data:
            x_data.append(temp)

    while len(y_data) != n:
        temp = random.randint(min_count, max_count)
        if temp not in y_data:
            y_data.append(temp)

    for i in range(len(x_data)):
        wh.update_cell(i + 1, 1, x_data[i])
        wh.update_cell(i + 1, 2, y_data[i])

        xy += x_data[i] * y_data[i]
        xx += x_data[i] ** 2
        x += x_data[i]
        y += y_data[i]

    first_parameter = (10 * xy - x * y) / (10 * xx - x ** 2)
    second_parameter = (y - first_parameter * x) / 10
    MNK = [[max_count, min_count], [first_parameter * max_count + second_parameter,
                                    first_parameter * min_count + second_parameter]]
    table = plt.gca()

    table.set_facecolor('white')
    plt.plot(MNK[0], MNK[1], c='black')
    plt.scatter(x_data, y_data, c="black")

    plt.show()

else:
    print("Введённый диапазон слишком мал... увы")
