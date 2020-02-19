# https://drive.google.com/file/d/1Qu7S3Qs0tBTjyivE71zeshUKLsiYCKHf/view?usp=sharing
# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

num_left_int = int(input('Введите левую границу для генерации случайного целого числа: '))
num_right_int = int(input('Введите правую границу для генерации случайного целого числа: '))
num_left_float = float(input('Введите левую границу для генерации случайногог вещественнго числа: '))
num_right_float = float(input('Введите правую границу для генерации случайного вещественного числа: '))
char_left = ord(input('Введите левую границу для генерации случайного символа английского алфавита: '))
char_right = ord(input('Введите правую границу для генерации случайного символа английского алфавита: '))
num_random_int = int(random.random() * (num_right_int - num_left_int + 1) + num_left_int)
num_random_float = random.random() * (num_right_float - num_left_float ) + num_left_float
char_random = chr(int(random.random() * (char_right - char_left + 1) + char_left))
print('Случайное целое число: ', num_random_int)
print('Случайное вещественное число: %.4f' % num_random_float)
print('Случайный символ: ', char_random)




