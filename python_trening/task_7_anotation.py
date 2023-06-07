a: int = 5
b: str = 'строка'
c: list = [1, 2]


def ident(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(ident('123', 123))


def lengths_list(s: str) -> int:
    return len(s)


print(lengths_list('12345678'))


def two_lists(l: list, m: list) -> int:
    return max(len(l), len(m))


print(two_lists([1, 2, 3, 4], [1, 2]))


def my_list_2(a = [1, 2, 3, 4]):
    a.append(4)
    return a


print(my_list_2())


def my_func(my_l: list) -> int:
    res = 0
    for elem in my_l:
        res = res + elem
    return res

print(my_func([1, 2, 3]))