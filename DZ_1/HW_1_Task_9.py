# https://drive.google.com/file/d/15Dh4G_FxluH0VaQMYwg7CBTHlA17ZL6S/view?usp=sharing
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_1 = int(input('Введите первое целое число: '))
num_2 = int(input('Введите второе уникальное целое число: '))
num_3 = int(input('Введите третье уникальное целое число: '))
if num_1 > num_2 > num_3 or num_3 > num_2 > num_1:
    print('Среднее из трех чисел: ', num_2)
elif num_2 > num_1 > num_3 or num_3 > num_1 > num_2:
    print('Среднее из трех чисел: ', num_1)
else:
    print('Среднее из трех чисел: ', num_3)