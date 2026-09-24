import math

MAX_VALUE = 10000


def solve(a, b, c):
    #проверка допустимости коэффициентов
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        raise ValueError("Числа слишком большие")

    if a == 0:
        if b == 0:
            raise ValueError("Это не уравнение")

        x = -c / b
        return "линейное", None, [x]
    #решение квадратного уравнения
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return "квадратное", d, [x1, x2]

    if d == 0:
        x = -b / (2 * a)
        return "квадратное", d, [x]

    return "квадратное", d, []