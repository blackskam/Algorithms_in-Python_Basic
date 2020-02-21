# https://drive.google.com/file/d/1Qf0sLh5QGH7-TDvkKyOB_yANWRyLyzqD/view?usp=sharing
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
# и заканчивая 127-м включительно. Вывод выполнить в табличной форме:
# по десять пар "код-символ" в каждой строке.

First_char = 32
Last_char = 128
T = 100
x_char = First_char
while x_char != Last_char:
    n = 10
    while n != 0 and x_char != Last_char:
        if n == 1:
            if x_char < T:
                print('"', x_char, ' -', chr(x_char), '"')
            else:
                print('"', x_char, '-', chr(x_char), '"')
        else:
            if x_char < T:
                print('"', x_char, ' -', chr(x_char), '"', end="   ")
            else:
                print('"', x_char, '-', chr(x_char), '"', end="   ")
        n -= 1
        x_char += 1
