MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000


def sign(n):
    if n % 2 == 0:
        return -1
    return 1


def term_sqplus(n):
    return sign(n) / (n * n + 1)


def term_third(n):
    return sign(n) / (3 * n)


FORMULAS = {
    "sqplus": (
        term_sqplus,
        "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."
    ),
    "third": (
        term_third,
        "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."
    ),
}


def sum_by_terms(term, terms):
    #проверка корректности количества слагаемых
    if terms < 1 or terms > MAX_TERMS:
        raise ValueError("количество слагаемых вне диапазона")

    result = 0
    #суммирование слагаемых
    for n in range(1, terms + 1):
        result += term(n)

    return result


def sum_by_eps(term, eps):
    #проверка точности
    if eps <= 0 or eps > MAX_EPS:
        raise ValueError("точность вне диапазона")

    result = 0
    n = 0
    #суммирование слагаемых до достижения точности
    while n < MAX_ITERATIONS:
        n += 1
        value = term(n)
        result += value

        if abs(value) < eps:
            return result, n
    #ограничение количества итераций
    raise ValueError("точность не достигнута")