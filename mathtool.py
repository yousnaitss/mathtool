import sys
import math  

MAX_VALUE = 10000


def main():
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        show_help() 
        return
    
    if sys.argv[1] != "solve":
        print("Ошибка: неизвестная команда", file=sys.stderr)
        return

    if len(sys.argv) == 2:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            print("Ошибка: введите числа", file=sys.stderr)
            return

    elif len(sys.argv) == 7:
        if sys.argv[2] != "-a" or sys.argv[4] != "-b" or sys.argv[6] != "-c":
            print("Ошибка в параметрах", file=sys.stderr)
            return

        try:
            a = int(sys.argv[3])
            b = int(sys.argv[5])
            c = int(sys.argv[7])
        except ValueError:
            print("Ошибка: введите числа!", file=sys.stderr)
            return

    else:
        print("Неверный формат ввода", file=sys.stderr)
        return

    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        print("Числа слишком большие", file=sys.stderr)
        return

    if a == 0:
        if b == 0:
            print("Это не уравнение", file=sys.stderr)
            return

        print("Линейное уравнение")
        x = -c / b
        print(f"x = {x:.3f}")

    else:
        print("Квадратное уравнение")
        D = b ** 2 - 4 * a * c 
        print(f"D = {D}")

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            print(f"x1 = {x1:.3f}")
            print(f"x2 = {x2:.3f}")

        elif D == 0:
            x = -b / (2 * a)
            print(f"x = {x:.3f}")

        else:
            print("Корней нет")


def show_help():
    print("Программа решает уравнения вида A*x^2 + B*x + C = 0")
    print("Как использовать:")
    print("python mathtool.py        # показать справку")
    print("python mathtool.py --help # показать справку")
    print("python mathtool.py solve  # ввести коэффициенты с клавиатуры")
    print("python mathtool.py solve -a 1 -b -3 -c 2  # решить с заданными числами")
    print("Числа должны быть целыми и не больше 10000 по модулю")


if __name__ == "__main__":
    main()
