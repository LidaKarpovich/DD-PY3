def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError
    factorial = 1
    for num in range(2, n + 1):
        factorial *= num
    return factorial
