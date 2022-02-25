nina_likeliness = ["Нина", None]
ira_likeliness = ["Ира", None]
h_likeliness = ["Хуэйминь", None]

c = 17
d = 101


def set_likeliness(num):
    try:
        num = float(num)
        if num < 0:
            return 0
        if num > 1:
            return 1
        return num
    except ValueError:
        print("Некорректный ввод")


nina_likeliness[1] = set_likeliness(input(f"Вероятность происхождения события с {nina_likeliness[0]} за {c} дней: "))
ira_likeliness[1] = set_likeliness(input(f"Вероятность происхождения события с {ira_likeliness[0]} за {c} дней: "))
h_likeliness[1] = set_likeliness(input(f"Вероятность происхождения события с {h_likeliness[0]} за {c} дней: "))


def likeliness_calculation():
    nina = 1 - ((1 - nina_likeliness[1]) ** (1 / c)) ** d
    ira = ((1 - ira_likeliness[1]) ** (1 / c)) ** d
    hy = ((1 - h_likeliness[1]) ** (1 / c)) ** d
    return nina * ira * hy


print(f"Только Нини за {d} дней создаст нейронную сеть с вероятностью = {likeliness_calculation()}")
