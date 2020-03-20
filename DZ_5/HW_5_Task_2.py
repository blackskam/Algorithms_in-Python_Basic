# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections

Point = collections.namedtuple('Point', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
d = Point( 0 = '0', 1 = '1', 2='2', 3='3', 4='4', 5='5', 6='6', 7='7', 8='8', 9='9', 10='A', 11='B',12='C',13='D',14='E', 15='F')

first = input('Введите первое шестнадцатеричное число:').upper()
second = input('Введите второе шестнадцатеричное число:').upper()
# print(num_1)
# print(num_2)
sum_oper = input('Введите требуемю операцию сложения ""+"" или умнржения ""*"":')
if sum_oper == '+':
    if len(first) > len(second):
        first,second = second,first
    second = second[::-1]
    third = []
    j = -1
    k = 0
    for i in second:
        one = d.index(i)
        two = d.index(first[j])
        third.append(d[(one + two + k) % 16])
        if (one + two) >= 15:
            k = 1
        else:
            k = 0
        j -= 1
        if j == -len(first) - 1:
            break
    diff = len(second) - len(first)
    if diff:
        for i in second[-diff:]:
            third.append(d[(d.index(second[-diff]) + k) % 16])
            if d.index(second[-diff]) + 1 >= 15:
                k = 1
            else:
                k = 0
    if k == 1:
        third.append('1')
    print(third[::-1])
