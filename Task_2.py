def is_prime(num):
    if num % 2 == 0:
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def iscomplex(s):
    try:
        complex(s)
        return True
    except ValueError:
        return False


print("Введите набор чисел")

data = list(input().split(","))

naturals = []
integers = []
rationals = []
complexs = []
evens = []
odds = []
primes = []

for num in data:
    if isint(num):

        if int(num) > 0:
            naturals.append(num)

        integers.append(num)
        rationals.append(num)
        complexs.append(num)

        if int(num) % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
        if is_prime(abs(int(num))):
            primes.append(num)

    elif isfloat(num):
        rationals.append(num)
        complexs.append(num)
    elif iscomplex(num):
        complexs.append(num)
    else:
        print(f"Запись числа: {num} - не соответсвует форме")

print("Натуральные числа: ", *naturals)
print("Целые числа: ", *integers)
print("Рацианальные числа: ", *rationals)
print("Коплексные числа: ", *complexs)
print("Чётные числа: ", *evens)
print("Нечётные числа: ", *odds)
print("Простые числа: ", *primes)
