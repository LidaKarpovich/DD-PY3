"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if len(arr) == 0:
        raise ValueError

    minimum = arr[0]
    index_of_min = 0
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
            index_of_min = i
    return index_of_min
