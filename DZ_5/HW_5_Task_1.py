# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

import collections

comp_rev = collections.defaultdict(int)
n = int(input("Введите количество предприятий: "))
sum_rev = 0
for i in range(n):
    comp_name = input("Наименование" + str(i + 1) + " -го предприятия: ")
    rev = 0
    for k in range(4):
        print('Введите прибыль в' + str(k + 1) + ' квартале: ', end='')
        rev = rev + int(input())
    sum_rev += rev
    comp_rev[comp_name] = rev
aver_sum = sum_rev / n
# print(comp_rev)
print('Средняя прибыль предприятий за год: ', "%.2f" % aver_sum)
print('Наименование предприятий с прибылью выше', "%.2f" % aver_sum, " : ")
for i in comp_rev:
    if int(comp_rev[i]) > aver_sum:
        print(i, 'с прибылью', comp_rev[i])
print('Наименование предприятий с прибылью ниже', "%.2f" % aver_sum, " : ")
for i in comp_rev:
    if int(comp_rev[i]) < aver_sum:
        print(i, 'с прибылью', comp_rev[i])