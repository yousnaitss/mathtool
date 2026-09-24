import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="Программа для вычислений",
        allow_abbrev=False
    )

    subparsers = parser.add_subparsers(dest="command")

    solve_parser = subparsers.add_parser(
        "solve",
        help="решение уравнения",
        allow_abbrev=False
    )
    solve_parser.add_argument("-a", type=int, help="коэффициент A")
    solve_parser.add_argument("-b", type=int, help="коэффициент B")
    solve_parser.add_argument("-c", type=int, help="коэффициент C")

    #параметры для команды stats
    stats_parser = subparsers.add_parser(
        "stats",
        help="показатели числовой последовательности",
        allow_abbrev=False
    )
    stats_parser.add_argument(
        "--input",
        help="файл с числами"
    )

    #параметры для команды series
    series_parser = subparsers.add_parser(
        "series",
        help="сумма ряда",
        allow_abbrev=False
    )
    series_parser.add_argument(
        "--func",
        choices=["sqplus", "third"],
        required=True,
        help="рассчитываемый ряд"
    )

    #выбор способа суммирования ряда
    series_group = series_parser.add_mutually_exclusive_group(required=True)
    series_group.add_argument(
        "--terms",
        type=int,
        help="колво слагаемых"
    )
    series_group.add_argument(
        "--eps",
        type=float,
        help="требуемая точность"
    )

    #параметры для команды integrate
    integrate_parser = subparsers.add_parser(
        "integrate",
        help="интегрирование",
        allow_abbrev=False
    )
    integrate_parser.add_argument(
        "--func",
        choices=["ratio", "root"],
        required=True,
        help="подынтегральная функция"
    )
    integrate_parser.add_argument(
        "--from",
        dest="start",
        type=float,
        required=True,
        help="нижний предел"
    )
    integrate_parser.add_argument(
        "--to",
        dest="end",
        type=float,
        required=True,
        help="верхний предел"
    )
    integrate_parser.add_argument(
        "--steps",
        type=int,
        required=True,
        help="количество шагов"
    )

    return parser