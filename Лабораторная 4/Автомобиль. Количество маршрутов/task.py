from typing import List
from functools import lru_cache


@lru_cache()
def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    n, m = tuple(map(int, input().split(' ')))
    final = [[0 for i in range(n)] for k in range(m)]
    for i in enumerate(final):
        for k in enumerate(i[1]):
            if (i[0] == 0) and (k[0] == 0):
                continue
            if i[0] == 0:
                final[0][k[0]] = 1
            elif k[0] == 0:
                final[i[0]][0] = 1
            else:
                final[i[0]][k[0]] = final[i[0] - 1][k[0]] + final[i[0]][k[0] - 1] + 1
    return(final)


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
