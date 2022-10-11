# <Задание 3>

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.
# Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import uniform

def get_real_list (n, frst, last):
    return [round(uniform(frst,last), 2) for i in range(n)]

def find_diff(my_list):
    list = [round(x - int(x), 2) for x in (my_list)]
    return max(list) - min(list)

n = 5
frst = 1
last = 10
my_list = get_real_list(n, frst, last)

print ('Список вещественных чисел:', my_list)
print('Разница между max и min дробной части: ', find_diff(my_list))
