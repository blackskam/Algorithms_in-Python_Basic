# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import timeit
import cProfile


def fun_1(n):
    k = n + 1
    s = n - 1
    while True:
        a = [0] * k  # создание массива с n количеством элементов
        for i in range(k):  # заполнение массива ...
            a[i] = i  # значениями от 0 до n-1
        # вторым элементом является единица, которую не считают простым числом
        # забиваем ее нулем.
        a[1] = 0
        m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
        while m < (k - 1):  # перебор всех элементов до заданного числа
            if a[m] != 0:  # если он не равен нулю, то
                j = m * 2  # увеличить в два раза (текущий элемент - простое число)
                while j < (k - 1):
                    a[j] = 0  # заменить на 0
                    j = j + m  # перейти в позицию на m больше
            m += 1
        b = []
        for i in a:
            if a[i] != 0:
                b.append(a[i])
        if n > len(b):
            k = k * 2
        else:
            break
    return b[s]
#
#
# print(fun_1(1000))
#
print(timeit.timeit('fun_1(50)', number=100, globals=globals()))    # 0.038461979
print(timeit.timeit('fun_1(100)', number=100, globals=globals()))   # 0.083635224
print(timeit.timeit('fun_1(200)', number=100, globals=globals()))   # 0.17423791199999997
print(timeit.timeit('fun_1(400)', number=100, globals=globals()))   # 0.40870510600000004
print(timeit.timeit('fun_1(800)', number=100, globals=globals()))   # 0.762874511
#
cProfile.run('fun_1(50)')  # 177 function calls in 0.001 seconds
cProfile.run('fun_1(100)')  # 301 function calls in 0.001 seconds
cProfile.run('fun_1(2000)')  # 7171 function calls in 0.042 seconds
cProfile.run('fun_1(4000)')  # 13282 function calls in 0.086 seconds
cProfile.run('fun_1(80000)')  # 200826 function calls in 2.111 seconds


def fun_2(n):
    s = n - 1
    i = 2
    lst = []
    size_mas = 0
    while True:
        if i % 2 == 0 and i == 2:
                lst.append(i)
                size_mas += 1
                #print(lst)
        else:
            d = 3
            while d * d <= i and i % d != 0:
                d += 2
            if d * d > i:
                lst.append(i)
                size_mas += 1
                # print(lst)
        if n <= size_mas:
            break
        i += 1
    #print(lst)
    return lst[s]


# print(fun_2(1000))

print(timeit.timeit('fun_2(50)', number=100, globals=globals()))    # 0.004628133000000201
print(timeit.timeit('fun_2(100)', number=100, globals=globals()))   # 0.01350030000000002
print(timeit.timeit('fun_2(200)', number=100, globals=globals()))   # 0.037756547999999945
print(timeit.timeit('fun_2(400)', number=100, globals=globals()))   # 0.11919455299999981
print(timeit.timeit('fun_2(800)', number=100, globals=globals()))   # 0.3150821309999996

cProfile.run('fun_2(50)')  # 54 function calls in 0.000 seconds
cProfile.run('fun_2(100)')  # 104 function calls in 0.000 seconds
cProfile.run('fun_2(2000)')  # 2004 function calls in 0.014 seconds
cProfile.run('fun_2(4000)')  # 4004 function calls in 0.036 seconds
cProfile.run('fun_2(80000)')  # 80004 function calls in 3.636 seconds


def fun_3(n):
    s = n - 1
    size_mas = 0
    my_list = [2]
    k = 3
    while True:
        i = 0
        while k > my_list[i]:
            if k % my_list[i] == 0:
                break
            if my_list[i] * 2 > k:
                my_list.append(k)
                size_mas += 1
                break
            i += 1
        if n <= size_mas:
            break
        k += 2
    return my_list[s]


# print(fun_3(1000))
print(timeit.timeit('fun_3(50)', number=100, globals=globals()))    # 0.022897889000000005
print(timeit.timeit('fun_3(100)', number=100, globals=globals()))   # 0.08093113700000001
print(timeit.timeit('fun_3(200)', number=100, globals=globals()))   # 0.310241224
print(timeit.timeit('fun_3(400)', number=100, globals=globals()))   # 1.1941692000000002
print(timeit.timeit('fun_3(800)', number=100, globals=globals()))   # 4.5872963989999995

cProfile.run('fun_3(50)')  # 54 function calls in 0.000 seconds
cProfile.run('fun_3(100)')  # 104 function calls in 0.001 seconds
cProfile.run('fun_3(2000)')  # 2004 function calls in 0.286 seconds
cProfile.run('fun_3(4000)')  # 4004 function calls in 1.178 seconds
cProfile.run('fun_3(80000)')  # не подсчитало, зависло