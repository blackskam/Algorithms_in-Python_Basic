# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 3
MAX_ITEM = 6
mas_one = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(mas_one)
mas_two = [0 for x in range(MIN_ITEM, MAX_ITEM + 1)]   # создаем массив из нулей
for i in range(len(mas_two)):
    num_entry = 0
    for k in range(SIZE):
        if (i + MIN_ITEM) == mas_one[k]:
            num_entry += 1
    mas_two[i] = num_entry
max_num = 0
place_max = 0
max_num = mas_two[place_max]
for i in range(len(mas_two)):
    if mas_two[i] > max_num:
        max_num = mas_two[i]
        place_max = i
print('Число', (place_max + MIN_ITEM), 'встречается в массиве чаще,', mas_two[place_max], 'раз(a)!')
