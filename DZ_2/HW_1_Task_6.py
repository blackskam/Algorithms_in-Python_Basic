# https://drive.google.com/file/d/1rpcabZaegIKX8g1PO2BhEdk20DuMNTGC/view?usp=sharing
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше
# введенное пользователем число, чем то, что загадано. Если за 10 попыток
# число не отгадано, вывести правильный ответ.
import random

Max_random = 100
Num_att = 10
secret = random.randint(0, Max_random)
x = 0
print('Угадайте целое число от 0 до', Max_random)
while x != Num_att:
    reply = int(input('Введите число: '))
    if reply == secret:
        print('Вы угадали!')
        break
    else:
        if reply > secret:
            print('Введенное число больше загаданного!')
        else:
            print('Введенное число меньше загаданного!')
    x += 1
    if x == Num_att:
        print('Вы не угадали число за', Num_att, 'попыток! Загаданное число равно', secret)
