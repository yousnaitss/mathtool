import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="программа для вычислений"
    )

    subparsers = parser.add_subparsers(dest="command")

    solve_parser = subparsers.add_parser(
        "solve",
        help="решение квадратного или линейного уравнения"
    )

    solve_parser.add_argument("-a", type=int)
    solve_parser.add_argument("-b", type=int)
    solve_parser.add_argument("-c", type=int)

    return parser