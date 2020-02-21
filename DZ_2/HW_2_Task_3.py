# https://drive.google.com/file/d/1kAJDBerXTgr71QGpqn6DrAWqenJ7hJSF/view?usp=sharing
# Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

number = int(input('Введите целое число: '))
revers = 0
while number > 0:
    digit = number % 10
    number = number // 10
    revers = revers * 10
    revers = revers + digit
print('Введенно целое число в обратной последовательности:', revers)