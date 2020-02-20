# https://drive.google.com/file/d/1qNVghD1tfq2-D1VDYwWIqewzn_0VsRsy/view?usp=sharing
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.


char_1 = input('Введите букву английского алфавита: ')
char_2 = input('Введите другую букву английского алфавита этого же регистра: ')
id_char_1 = ord(char_1)
id_char_2 = ord(char_2)
if 64 < id_char_1 < 91 and 64 < id_char_2 < 91 and id_char_1 != id_char_2:
    id_char_1 = id_char_1 - 64
    id_char_2 = id_char_2 - 64
    number_char = (abs(id_char_2 - id_char_1)) -1
    print('Порядковый номер буквы "', char_1, '" в алфавите равен ', id_char_1)
    print('Порядковый номер буквы "', char_2, '" в алфавите равен ', id_char_2)
    print('Между буквами "', char_1,'" и "', char_2,'" находится ', number_char, 'буквы')
elif 96 < id_char_1 < 123 and 96 < id_char_2 < 123 and id_char_1 != id_char_2:
    id_char_1 = id_char_1 - 96
    id_char_2 = id_char_2 - 96
    number_char = (abs(id_char_2 - id_char_1)) - 1
    print('Порядковый номер буквы "', char_1, '" в алфавите равен ', id_char_1)
    print('Порядковый номер буквы "', char_2, '" в алфавите равен ', id_char_2)
    print('Между буквами "', char_1, '" и "', char_2, '" находится ', number_char, 'буквы')
else:
    print('Введены символы не английского алфавита или различаются регистры или символы одинаковы!')
