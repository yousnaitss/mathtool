import math


MAX_COUNT = 20
MAX_ABS = 10000


def validate_numbers(values):
    if not values:
        raise ValueError("последовательность пуста")
def total(values):
    result = 0
    for value in values:
        result += value
    return result


def mean(values):
    return total(values) / len(values)


def sum_squares(values):
    result = 0
    for value in values:
        result += value ** 2
    return result


def root_mean_square(values):
    return math.sqrt(sum_squares(values) / len(values))


def sum_squared_deviations(values):
    average = mean(values)
    result = 0

    for value in values:
        result += (value - average) ** 2

    return result


def variance(values):
    return sum_squared_deviations(values) / len(values)


def rms_deviation(values):
    return math.sqrt(variance(values))


def standard_deviation(values):
    if len(values) < 2:
        return None

    return math.sqrt(
        sum_squared_deviations(values) / (len(values) - 1)
    )


def minimum(values):
    result = values[0]

    for value in values:
        if value < result:
            result = value

    return result


def maximum(values):
    result = values[0]

    for value in values:
        if value > result:
            result = value

    return result


def positive_count(values):
    result = 0

    for value in values:
        if value > 0:
            result += 1

    return result


def negative_count(values):
    result = 0

    for value in values:
        if value < 0:
            result += 1

    return result

    if len(values) > MAX_COUNT:
        raise ValueError("слишком много чисел")

    for value in values:
        if not math.isfinite(value):
            raise ValueError("число должно быть конечным")

        if abs(value) > MAX_ABS:
            raise ValueError("число вне допустимого диапазона")