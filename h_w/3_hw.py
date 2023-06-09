import numpy


# --- ЗАДАЧА 1---
def max_digit(num_1, num_2):
    print(max(num_1, num_2))


max_digit(5, 125)


# --- ЗАДАЧА 2---
def nums_difference(num_1, num_2):
    if ((num_1 - num_2) == 135) or ((num_2 - num_1) == 135):
        print('yes')
    else:
        print('no')


nums_difference(1, 136)


# --- ЗАДАЧА 3---
def seasons(month):
    if month in [12, 1, 2]:
        print('winter')
    elif month in range(3, 7):
        print('spring')
    elif month in range(6, 9):
        print('summer')
    elif month in range(9, 12):
        print('autumn')
    else:
        print("Try again, it's only 12 months in year")


seasons(6)


# --- ЗАДАЧА 4---
def more_than_ten(num_1, num_2, num_3):
    if num_1 > 10 and num_2 > 10 and num_3 > 10:
        print('yes')
    else:
        print('no')


more_than_ten(51, 100, 15)


# *ЗАДАЧА 5*
def positive_nums(samp_nums=numpy.random.randint(-100, 100, 5)):
    print(samp_nums)
    count = 0
    for i in samp_nums:
        if i > 0:
            count += 1
    return (count)


print(positive_nums())


# *ЗАДАЧА 6*
def days_counter(years, months):
    days = years * 365 + months * 29
    print(days)


days_counter(10, 1)
