# <Задание 2>

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint
import math


size = int(input('Введите размер списка: '))
my_list = []
for i in range(size):
    my_list.append(randint(-10, 10))

print('Список: ', my_list)
def mult_pairs(my_list):
    return [my_list[i] * my_list[-i - 1] for i in range(math.ceil(len(my_list)/2))]
print('Произведение пар списка: ', mult_pairs(my_list))