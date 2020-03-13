# В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

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
sum_num = 0
if place_min > place_max:   
    place_min, place_max = place_max, place_min
for i in range(place_min + 1, place_max):
    sum_num = sum_num + mas_one[i]
print('Минимальное значение: ', min_num)
print('Максимальное значение: ', max_num)
print('Сумма чисел между минимальными и максимальными значениями: ', sum_num)