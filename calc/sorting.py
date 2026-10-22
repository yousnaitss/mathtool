
from calc.arrays import MIN_VALUE, MAX_VALUE

METHODS = {}


def not_in_order(a, b, descending=False):
    #проверяет, нужно ли поменять соседние элементы местами
    if descending:
        return a < b
    return a > b


def bubble_sort(values, descending=False):
    #сортирует массив пузырьковым методом
    n = len(values)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if not_in_order(values[j], values[j + 1], descending):
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

        if not swapped:
            break


METHODS["bubble"] = bubble_sort


def selection_sort(values, descending=False):
    #сортирует массив выбором элемента
    n = len(values)

    for i in range(n - 1):
        best_index = i

        for j in range(i + 1, n):
            if not_in_order(
                values[best_index],
                values[j],
                descending
            ):
                best_index = j

        if best_index != i:
            values[i], values[best_index] = values[best_index], values[i]


METHODS["selection"] = selection_sort


def insertion_sort(values, descending=False):
    #сортирует массив вставками
    for i in range(1, len(values)):
        current = values[i]
        j = i - 1

        while j >= 0 and not_in_order(
            values[j],
            current,
            descending
        ):
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = current


METHODS["insertion"] = insertion_sort

def counting_sort(values, descending=False):
    #сортирует массив подсчётом количества значений
    counts = [0] * (MAX_VALUE - MIN_VALUE + 1)

    #подсчитываем количество каждого значения
    for value in values:
        counts[value - MIN_VALUE] += 1

    #записываем значения в исходный список
    index = 0

    if descending:
        value_range = range(MAX_VALUE, MIN_VALUE - 1, -1)
    else:
        value_range = range(MIN_VALUE, MAX_VALUE + 1)

    for value in value_range:
        count = counts[value - MIN_VALUE]

        for _ in range(count):
            values[index] = value
            index += 1


METHODS["counting"] = counting_sort
