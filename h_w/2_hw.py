# --- ЗАДАЧА 1 ---
def task_1():
    a: int = 777
    b: float = 3.15
    c: str = 'пятница'
    d: list = [3, 6, 'ci', "привет", 8.5]
    e: bool = True
    return type(a), type(b), type(c), type(d), type(e)


fun = task_1()
print(fun, end=',\n')


# --- ЗАДАЧА 2 ---
def task_2():
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]


print(task_2())


# --- ЗАДАЧА 3 ---
def task_3(a):
    sq = a * a
    return sq


print(task_3(9))
