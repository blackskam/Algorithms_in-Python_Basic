# https://drive.google.com/file/d/1qNVghD1tfq2-D1VDYwWIqewzn_0VsRsy/view?usp=sharing
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

ID_BEGIN = 96
ID_END = 123
char_1 = input('Введите букву английского алфавита: ')
char_2 = input('Введите другую букву английского алфавита этого же регистра: ')
id_char_1 = ord(char_1)
id_char_2 = ord(char_2)
if ID_BEGIN < id_char_1 < ID_END and ID_BEGIN < id_char_2 < ID_END and id_char_1 != id_char_2:
    id_char_1 = id_char_1 - ID_BEGIN
    id_char_2 = id_char_2 - ID_BEGIN
    number_char = (abs(id_char_2 - id_char_1)) - 1
    print('Порядковый номер буквы "', char_1, '" в алфавите равен ', id_char_1)
    print('Порядковый номер буквы "', char_2, '" в алфавите равен ', id_char_2)
    print('Между буквами "', char_1, '" и "', char_2, '" находится ', number_char, 'буквы')
else:
    print('Введены символы не английского алфавита или неправильный регистр или буквы одинаковы!')
