def matrix_input(x, y):
    matrix = []
    for i in range(y):
        line = list(map(int, input().split()))
        while len(line) < x:
            print("Данная строка меньше указанного значения. Повторите попытку ввода")
            line = list(map(int, input().split()))
        matrix.append(line)
    return matrix


def matrix_show(matrix):
    print('-' * len(matrix[0]))
    for i in matrix:
        print(*i)
    print('-' * len(matrix[0]))


def matrix_transpose(matrix):
    x_size = len(matrix[0])
    y_size = len(matrix)

    temp = [[0] * y_size for i in range(x_size)]

    for y in range(x_size):
        for x in range(y_size):
            temp[y][x] = matrix[x][y]

    return temp


def matrix_multiplication(matrix):
    y_size = len(matrix)
    x_size = len(matrix[0])
    if x_size != y_size:
        print("Невозможная операция с данной матрицей")
        return

    temp = [[None] * y_size for __ in range(y_size)]

    for i in range(y_size):
        for j in range(x_size):
            temp[i][j] = sum(matrix[i][kk] * matrix[kk][j] for kk in range(y_size))
    return temp


def matrix_determinant(matrix):
    y_size = len(matrix)
    x_size = len(matrix[0])
    if x_size != y_size:
        print("Невозможная операция с данной матрицей")
        return

    def get_matrix_cofactor(m, i, j):
        return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]

    if (len(matrix) == 2):
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value
    det = 0
    for current_column in range(len(matrix)):
        sign = (-1) ** (current_column)
        sub_det = matrix_determinant(get_matrix_cofactor(matrix, 0, current_column))
        det += (sign * matrix[0][current_column] * sub_det)

    return det


print("Введите ширину и высоту матрицы")
x, y = map(int, input().split())

print("Введите матрицу")
matrix = matrix_input(x, y)

print("Выберете опредацию которую хотите произести")
print("1 - транспонирование")
print("2 - возведение в квадрат")
print("3 - найти определитель")

while True:

    option = input()

    match option:
        case "1":
            matrix_show(matrix_transpose(matrix))
        case "2":
            matrix_show(matrix_multiplication(matrix))
        case "3":
            print("D = " + str(matrix_determinant(matrix)))
        case _:
            print("Код опперации не найден.")
