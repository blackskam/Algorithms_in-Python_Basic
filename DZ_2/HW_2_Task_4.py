# https://drive.google.com/file/d/1DjmT1gDb_Pk37g-WKPrgasSMzDwDtxGi/view?usp=sharing
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


def row_sum(x):
    if x == 1:
        return 1
    else:
        return row_sum(x - 1) / -2 + 1


num_count = int(input('Введите целое положительное число: '))
row_rezult = row_sum(num_count)
print('Cумма ряда: ', row_rezult)
