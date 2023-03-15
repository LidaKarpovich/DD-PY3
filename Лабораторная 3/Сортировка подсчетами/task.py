from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    counted_container = []
    for i in range(len(container) + 1):
        counted_container += [0]
    for i in container:
        counted_container[i] += 1
    j = 0
    for i in range(len(container) + 1):
        if counted_container[i] > 0:
            for k in range(counted_container[i]):
                container[j] = i
                j += 1
    return container
