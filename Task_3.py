import random
from random import randint
from time import perf_counter
from prettytable import PrettyTable


def buble_sort(array):
    size = len(array)
    od = True
    while od and size > 0:
        od = False
        size -= 1
        for i in range(size):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i], array[i + 1]
                od = True


def gnome_sort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1
    return arr


# Блочная.
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSort(x):
    arr = []
    slot_num = 10

    for i in range(slot_num):
        arr.append([])

    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


# Пирамидальная.
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


size = 10 ** 4

original_array = [randint(-10 ** 4, 10 ** 4) for x in range(size)]
array_version_1 = original_array[:]
array_version_2 = original_array[:]
array_version_3 = original_array[:]
array_version_4 = original_array[:]

t_start = perf_counter()
print("Progress: 0%")
buble_sort(array_version_1)
time_1 = perf_counter() - t_start

t_start = perf_counter()
print("Progress: 25%")
gnome_sort(array_version_2, len(array_version_2))
time_2 = perf_counter() - t_start

t_start = perf_counter()
print("Progress: 50%")
bucketSort([random.random() for x in range(size)])
time_3 = perf_counter() - t_start

t_start = perf_counter()
print("Progress: 75%")
heapSort(array_version_4)
time_4 = perf_counter() - t_start

print("Progress: 100%")
columns = ["Тип сортировки", "Время работы"]
sort_name = ["Пузырьковая сортировка", "Гномья сортировка", "Блочная  сортировка", "Пирамидальная сортировка"]
sort_time = [time_1, time_2, time_3, time_4]

ans_table = PrettyTable()
ans_table.add_column(columns[0], sort_name)
ans_table.add_column(columns[1], sort_time)
print(ans_table)
