import sys

from calc import equation
from cli import create_parser


def handle_solve(args):
    a, b, c = args.a, args.b, args.c

    if a is None and b is None and c is None:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            raise ValueError("введите целые числа")

    elif a is None or b is None or c is None:
        raise ValueError(
            "необходимо указать либо все параметры -a, -b, -c, либо ни одного"
        )

    kind, d, roots = equation.solve(a, b, c)

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


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "solve":
            return handle_solve(args)

        return 1

    except (ValueError, OSError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())