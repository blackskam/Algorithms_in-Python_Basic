# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 10
mas_one = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(mas_one)
if mas_one[0] > mas_one[1]:
    min_num_2 = mas_one[0]
    min_num = mas_one[1]
else:
    min_num_2 = mas_one[1]
    min_num = mas_one[0]
for i in range(2, SIZE):
    if mas_one[i] < min_num_2:
        min_num_2 = mas_one[i]
    elif mas_one[i] < min_num:
        min_num = mas_one[i]

print('Наименьшими элементами массива являются число', min_num, 'и число', min_num_2)