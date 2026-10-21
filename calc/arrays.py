import random

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000

#создаёт список случайных целых чисел
def fill_array(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    if not 1 <= count <= MAX_COUNT:
        raise ValueError(
            f"количество элементов вне диапазона 1..{MAX_COUNT}"
        )

    if (
        low < MIN_VALUE
        or low > MAX_VALUE
        or high < MIN_VALUE
        or high > MAX_VALUE
        or low > high
    ):
        raise ValueError(
            f"границы должны быть в диапазоне "
            f"{MIN_VALUE}..{MAX_VALUE}, min <= max"
        )

    rng = random.Random(seed)
    return [rng.randint(low, high) for _ in range(count)]


def binary_search(values, target):
    #возвращает индекс найденного элемента или None
    if abs(target) > MAX_SEARCH:
        raise ValueError(
            f"искомое значение должно быть в диапазоне "
            f"-{MAX_SEARCH}..{MAX_SEARCH}"
        )

    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            raise ValueError(
                "массив не упорядочен по возрастанию"
            )

    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2

        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None