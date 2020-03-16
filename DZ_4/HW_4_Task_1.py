# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
# Для примера взял 3 задачу с 2 урока: в массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import timeit
import cProfile
import random

def swap_max_min(n):
    MIN_ITEM = 1
    MAX_ITEM = 99
    mas_one = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    place_min = 0
    place_max = 0
    min_num = mas_one[place_min]
    max_num = mas_one[place_max]
    for i in range(n):
        if mas_one[i] < min_num:
            min_num = mas_one[i]
            place_min = i
        if mas_one[i] > max_num:
            max_num = mas_one[i]
            place_max = i
    mas_one[place_max] = min_num
    mas_one[place_min] = max_num
    return mas_one

print(timeit.timeit('swap_max_min(5000)', number=100, globals=globals()))    # 0.055597992
print(timeit.timeit('swap_max_min(10000)', number=100, globals=globals()))   # 0.110891626
print(timeit.timeit('swap_max_min(20000)', number=100, globals=globals()))   # 0.238630698
print(timeit.timeit('swap_max_min(40000)', number=100, globals=globals()))   # 0.44605031600000006
print(timeit.timeit('swap_max_min(80000)', number=100, globals=globals()))   # 0.900483301

cProfile.run('swap_max_min(5000)') # 2671 function calls in 0.001 seconds
cProfile.run('swap_max_min(10000)') # 5266 function calls in 0.003 seconds
cProfile.run('swap_max_min(20000)') # 10543 function calls in 0.005 seconds
cProfile.run('swap_max_min(40000)') # 21110 function calls in 0.010 seconds
cProfile.run('swap_max_min(80000)') # 42308 function calls in 0.023 seconds

def swap_max_min_2(n):
    MIN_ITEM = 1
    MAX_ITEM = 99
    mas_one = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    mas_one[(mas_one.index(min(mas_one)))] = max(mas_one)
    mas_one[(mas_one.index(max(mas_one)))] = min(mas_one)
    return mas_one

print(timeit.timeit('swap_max_min_2(5000)', number=100, globals=globals()))    # 0.05480453
print(timeit.timeit('swap_max_min_2(10000)', number=100, globals=globals()))   # 0.10912864100000001
print(timeit.timeit('swap_max_min_2(20000)', number=100, globals=globals()))   # 0.288488921
print(timeit.timeit('swap_max_min_2(40000)', number=100, globals=globals()))   # 0.492466652
print(timeit.timeit('swap_max_min_2(80000)', number=100, globals=globals()))   # 0.9048568160000001

cProfile.run('swap_max_min_2(5000)') # 2646 function calls in 0.001 seconds
cProfile.run('swap_max_min_2(10000)') # 5298 function calls in 0.002 seconds
cProfile.run('swap_max_min_2(20000)') # 10614 function calls in 0.004 seconds
cProfile.run('swap_max_min_2(40000)') # 21133 function calls in 0.009 seconds
cProfile.run('swap_max_min_2(80000)') # 42433 function calls in 0.017 seconds

def swap_max_min_3(n):
    MIN_ITEM = 1
    MAX_ITEM = 99
    mas_one = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    i = mas_one.index(max(mas_one))
    j = mas_one.index(min(mas_one))
    mas_one[i], mas_one[j] = mas_one[j], mas_one[i]
    return mas_one

print(timeit.timeit('swap_max_min_3(5000)', number=100, globals=globals()))    # 0.057200706000000004
print(timeit.timeit('swap_max_min_3(10000)', number=100, globals=globals()))   # 0.113484391
print(timeit.timeit('swap_max_min_3(20000)', number=100, globals=globals()))   # 0.219523268
print(timeit.timeit('swap_max_min_3(40000)', number=100, globals=globals()))   # 0.429706186
print(timeit.timeit('swap_max_min_3(80000)', number=100, globals=globals()))   # 0.930687355

cProfile.run('swap_max_min_3(5000)') # 2653 function calls in 0.001 seconds
cProfile.run('swap_max_min_3(10000)') # 5324 function calls in 0.002 seconds
cProfile.run('swap_max_min_3(20000)') # 10574 function calls in 0.004 seconds
cProfile.run('swap_max_min_3(40000)') # 21176 function calls in 0.009 seconds
cProfile.run('swap_max_min_3(80000)') # 42388 function calls in 0.017 seconds


# Вывод, алгоритмы одинаковы, пример взял неудачный.



