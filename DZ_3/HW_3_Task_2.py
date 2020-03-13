# 2. Во втором массиве сохранить индексы четных элементов первого массива.
#    Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
#    второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
#    т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 2
MAX_ITEM = 99
mas_one = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(mas_one)
mas_two = []
for i in range(SIZE):
    if mas_one[i] % 2 == 0:
        mas_two.append(i)
print(mas_two)
