# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 2
MAX_ITEM = 99
mas_one = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(mas_one)
place_min = 0
place_max = 0
min_num = mas_one[place_min]
max_num = mas_one[place_max]
for i in range(SIZE):
    if mas_one[i] < min_num:
        min_num = mas_one[i]
        place_min = i
    if mas_one[i] > max_num:
        max_num = mas_one[i]
        place_max = i
mas_one[place_max] = min_num
mas_one[place_min] = max_num
print(mas_one)