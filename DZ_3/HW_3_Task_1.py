# 1. В диапазоне натуральных чисел от 2 до 99 определить,
#    сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_NUM = 2
MAX_NUM = 100   # максимальный диапазон + 1
MIN_RANGE = 2
MAX_RANGE = 10  # максимальный диапазон + 1
mas_range = [0 for x in range(MAX_RANGE)]   # создаем массив из нулей
for num1 in range(MIN_NUM, MAX_NUM):
    for num2 in range(MIN_RANGE, MAX_RANGE):
        if num1 % num2 == 0:
            mas_range[num2] = mas_range[num2] + 1
for i in range(MIN_RANGE, MAX_RANGE):
    print(i, "=", mas_range[i])

