# <Задание 1>

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def get_list(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def sum_odd_position(my_list):
    return sum(my_list[1::2])

n = 5
frst = 1
last = 10

my_list = get_list(n, frst, last)
print('Заданный список: ', my_list)
print('Элементы стоящие на нечетных позициях: ', my_list[1::2])
print('Сумма элементов стоящих на нечетной позиции = ',sum_odd_position(my_list))


