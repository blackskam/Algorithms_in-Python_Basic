# https://drive.google.com/file/d/1MRNWmca8eEUtKOpFKtFsPBeCRZSVDXml/view?usp=sharing
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите натуральное число:')
n = len(number)
k = 0
num_even = 0
num_odd = 0
while k < n:
    num = int(number) // 10 ** k % 10
    k += 1
    if num % 2 == 0:
        num_even += 1
    else:
        num_odd += 1
print('В введенном числе', num_even, 'четных цифр и', num_odd, 'нечетных цифр')