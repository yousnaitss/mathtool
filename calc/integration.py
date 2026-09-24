import math


MAX_STEPS = 100000


def f_ratio(x):
    #первая подынтегральная функция
    return x / (x + 1)


def f_root(x):
    #вторая подынтегральная функция
    return math.sqrt(x * x + 1)

#таблица доступных функций и их ограничений
FUNCTIONS = {
    "ratio": (
        f_ratio,
        "F(x) = x / (x + 1)",
        0,
        20,
        True
    ),
    "root": (
        f_root,
        "F(x) = sqrt(x^2 + 1)",
        -5,
        5,
        False
    ),
}


def integrate(function, a, b, steps):
    #проверка корректности пределов интегрирования и количества шагов
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("пределы должны быть конечными")

    if a >= b:
        raise ValueError("нижний предел должен быть меньше верхнего")

    if steps < 1 or steps > MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")

    dx = (b - a) / steps
    result = 0

    for i in range(steps):
        x = a + i * dx
        result += function(x) * dx

    return result


def validate_limits(a, b, low, high, closed):
    #проверка корректности пределов интегрирования
    if closed:
        if a < low or a > high or b < low or b > high:
            raise ValueError("предел вне допустимого диапазона")
    else:
        if a <= low or a >= high or b <= low or b >= high:
            raise ValueError("предел вне допустимого диапазона")