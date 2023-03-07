def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    if len(brackets_row) % 2 != 0:
        return False
    para = {'(': ')'}
    stack = []
    for bracket in brackets_row:
        if bracket in para.keys():
            stack.append(bracket)
        else:
            if stack == []:
                return False
            open_bracket = stack.pop()
            if bracket != para[open_bracket]:
                return False

    return stack == []


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
