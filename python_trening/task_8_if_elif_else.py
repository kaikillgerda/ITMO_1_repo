num = -5

if num >= 0:
    print ('Число больше либо равно 0')
else:
    print('Число отрицательное')


str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print("ДА")
else:
    print("НЕТ")


num_float = 3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

num = -5
permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


def get_rank(year):
    if 1 < year < 5:
    # if year in range(1,5):
        return ('бакалавр')
    elif 5 <= year < 7:
        return ('магистр')
    elif 7 <= year < 10:
        return ('аспирант')
    else:
        return ('Введите корректный год обучения')


print(get_rank(5))


def get_num(i):
    if i > 100 or i < -100:
        print('-')
    else:
        print('+')


get_num(5)