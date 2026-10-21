import random

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000


#создаёт список случайных целых чисел
def fill_array(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    #проверка параметров генерации
    if not 1 <= count <= MAX_COUNT:
        raise ValueError(
            f"количество элементов вне диапазона 1..{MAX_COUNT}"
        )

    if low < MIN_VALUE or high > MAX_VALUE or low > high:
        raise ValueError(
            f"границы должны быть в диапазоне {MIN_VALUE}..{MAX_VALUE}, min <= max"
        )

    #генерация массива
    random.seed(seed)
    values = []

    for _ in range(count):
        values.append(random.randint(low, high))

    return values
