# <Задание 5>

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

n = int(input('Введите предел последовательности Фибоначчи: '))

def get_fibonacci(n):
    fibo_nums = []
    for i in range(n*2+1):
        fibo_nums.append(0)
    fibo_nums[n -1] = fibo_nums[n + 1] = 1
    for i in range (n-1):
        fibo_nums[n + 2 + i] = fibo_nums[n + 1 + i] + fibo_nums[n + i]
        fibo_nums[n - 2 - i] = fibo_nums[n - i] - fibo_nums[n - 1 - i]
    return fibo_nums

fibo_nums = get_fibonacci(n)
print('Последовательность Фибоначчи ', get_fibonacci(n))
