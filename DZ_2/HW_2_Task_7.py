# https://drive.google.com/file/d/1s4e7io6upGCXh8m0zISPr8eZCwWbJilr/view?usp=sharing
# Напишите программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n1 = 99
n2 = n1
x = 0
while n1 != 0:
    x = x + n1
    n1 -= 1
y = n2*(n2 + 1) / 2
print(x, '=', int(y))
