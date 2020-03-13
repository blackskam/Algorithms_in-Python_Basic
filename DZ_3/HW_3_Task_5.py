# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение
# и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 20
mas_one = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(mas_one)
if MIN_ITEM >= 0:
    print('Отрицательные числа в массиве отсутствуют!')
else:
    place_minus = 0
    max_minus = 0
    while place_minus < len(mas_one):   # находим первое отрицательное число в массиве
        if mas_one[place_minus] < 0:
            max_minus = mas_one[place_minus]
            break
        place_minus += 1
    for i in range(len(mas_one)):   # ищем максимальное отрицательное число
        if mas_one[i] < 0 and abs(mas_one[i]) < abs(max_minus):
            max_minus = mas_one[i]
            place_minus = i
    print('Максимальное отрицательное число', max_minus, 'находится на', place_minus, 'позиции!')