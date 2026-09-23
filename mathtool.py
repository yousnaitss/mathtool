import sys

from calc import equation
from cli import create_parser

def show_help():
    print("Программа решает уравнения вида A*x^2 + B*x + C = 0")
    print("Как использовать:")
    print("python mathtool.py        # показать справку")
    print("python mathtool.py --help # показать справку")
    print("python mathtool.py solve  # ввести коэффициенты с клавиатуры")
    print("python mathtool.py solve -a 1 -b -3 -c 2  # решить с заданными числами")
    print("Числа должны быть целыми и не больше 10000 по модулю")

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "solve":
        a, b, c = args.a, args.b, args.c

        if a is None and b is None and c is None:
            try:
                a = int(input("Введите A: "))
                b = int(input("Введите B: "))
                c = int(input("Введите C: "))
            except ValueError:
                print("Ошибка: введите целые числа", file=sys.stderr)
                return 1

        elif a is None or b is None or c is None:
            print(
                "Ошибка: необходимо указать либо все параметры -a, -b, -c, либо ни одного",
                file=sys.stderr
            )
            return 1

        try:
            kind, d, roots = equation.solve(a, b, c)
        except ValueError as error:
            print(f"Ошибка: {error}", file=sys.stderr)
            return 1

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

    return 1

if __name__ == "__main__":
    sys.exit(main())
