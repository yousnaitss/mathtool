import math


MAX_COUNT = 20
MAX_ABS = 10000


def validate_numbers(values):
    #проверка количества и допустимых значений
    if not values:
        raise ValueError("последовательность пуста")
def total(values):
    #расчет суммы
    result = 0
    for value in values:
        result += value
    return result


def mean(values):
    #расчет среднего арифметического
    return total(values) / len(values)


def sum_squares(values):
    #расчет суммы квадратов
    result = 0
    for value in values:
        result += value ** 2
    return result


def root_mean_square(values):
    #расчет среднего квадратичного
    return math.sqrt(sum_squares(values) / len(values))


def sum_squared_deviations(values):
    #расчет суммы квадратов отклонений от среднего
    average = mean(values)
    result = 0

    for value in values:
        result += (value - average) ** 2

    return result


def variance(values):
    #расчет дисперсии
    return sum_squared_deviations(values) / len(values)


def rms_deviation(values):
    #расчет среднеквадратичного отклонения
    return math.sqrt(variance(values))


def standard_deviation(values):
    #расчет стандартного отклонения
    if len(values) < 2:
        return None

    return math.sqrt(
        sum_squared_deviations(values) / (len(values) - 1)
    )


def minimum(values):
    #расчет минимального значения
    result = values[0]

    for value in values:
        if value < result:
            result = value

    return result


def maximum(values):
    #расчет максимального значения
    result = values[0]

    for value in values:
        if value > result:
            result = value

    return result


def positive_count(values):
    #подсчет количества положительных чисел
    result = 0

    for value in values:
        if value > 0:
            result += 1

    return result


def negative_count(values):
    #подсчет количества отрицательных чисел
    result = 0

    for value in values:
        if value < 0:
            result += 1

    return result

    #проверка ограничения колва числел
    if len(values) > MAX_COUNT:
        raise ValueError("слишком много чисел")

    #проверка диапазона
    for value in values:
        if not math.isfinite(value):
            raise ValueError("число должно быть конечным")

        if abs(value) > MAX_ABS:
            raise ValueError("число вне допустимого диапазона")