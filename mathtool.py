import sys
from calc import integration
from calc import series
from calc import stats
from calc import equation
from cli import create_parser


def handle_solve(args):
    #получение коэффициентов
    a, b, c = args.a, args.b, args.c

    #ввод коэф при отсутствии параметров
    if a is None and b is None and c is None:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            raise ValueError("введите целые числа")
    #проверка ввода всех коэффициентов
    elif a is None or b is None or c is None:
        raise ValueError(
            "необходимо указать либо все параметры -a, -b, -c, либо ни одного"
        )

    #решение уравнения
    kind, d, roots = equation.solve(a, b, c)
    
    #вывод результата
    if kind == "линейное":
        print("Линейное уравнение")
        print(f"x = {roots[0]:.3f}")

    else:
        print("Квадратное уравнение")
        print(f"D = {d}")

        if len(roots) == 2:
            print(f"x1 = {roots[0]:.3f}")
            print(f"x2 = {roots[1]:.3f}")
        elif len(roots) == 1:
            print(f"x = {roots[0]:.3f}")
        else:
            print("Действительных корней нет")

    return 0

def handle_stats(args):
    #чтение числ последовательности
    if args.input:
        with open(args.input, encoding="utf-8-sig") as handle:
            values = []

            #чтение данных из файла
            for line in handle:
                for word in line.split():
                    try:
                        value = float(word)
                    except ValueError:
                        raise ValueError(f"{word} не является числом")

                    values.append(value)
    else:
        values = []
        #чтение данных из обычного ввода
        for line in sys.stdin:
            for word in line.split():
                try:
                    value = float(word)
                except ValueError:
                    raise ValueError(f"{word} не является числом")

                values.append(value)

    stats.validate_numbers(values)
    #вывод статистических данных
    print(f"Количество: {len(values)}")
    print(f"Сумма: {stats.total(values):.3f}")
    print(f"Ср. арифм.: {stats.mean(values):.3f}")
    print(f"Сумма кв.: {stats.sum_squares(values):.3f}")
    print(f"Ср. кв.: {stats.root_mean_square(values):.3f}")
    print(f"Дисперсия: {stats.variance(values):.3f}")
    print(f"СКО: {stats.rms_deviation(values):.3f}")

    standard = stats.standard_deviation(values)

    if standard is None:
        print("Станд. откл.: НЕ СУЩЕСТВУЕТ")
    else:
        print(f"Станд. откл.: {standard:.3f}")

    print(f"Наименьшее: {stats.minimum(values):.3f}")
    print(f"Наибольшее: {stats.maximum(values):.3f}")
    print(f"Положительных: {stats.positive_count(values)}")
    print(f"Отрицательных: {stats.negative_count(values)}")

    return 0

def handle_series(args):
    term, formula = series.FORMULAS[args.func]

    #выбор способа суммирования
    if args.terms is not None:
        result = series.sum_by_terms(term, args.terms)
        terms = args.terms
    else:
        result, terms = series.sum_by_eps(term, args.eps)

    #вывод результата суммирования
    print(formula)
    print(f"Слагаемых: {terms}")
    print(f"Сумма ряда: {result:.4f}")

    return 0

def handle_integrate(args):
    function, formula, low, high, closed = integration.FUNCTIONS[args.func]

    #проверка пределов интегрирования
    integration.validate_limits(
        args.start,
        args.end,
        low,
        high,
        closed
    )

    #вычисление интеграла
    result = integration.integrate(
        function,
        args.start,
        args.end,
        args.steps
    )

    #вывод результата
    print(formula)
    print(f"Значение интеграла: {result:.4f}")

    return 0

def main():
    parser = create_parser()
    args = parser.parse_args()

    #если команда не указана то вывод справки
    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "solve":
            return handle_solve(args)

        if args.command == "stats":
            return handle_stats(args)

        if args.command == "series":
            return handle_series(args)

        if args.command == "integrate":
            return handle_integrate(args)


        return 1
    #обработка ошибок входных данныъ
    except (ValueError, OSError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())