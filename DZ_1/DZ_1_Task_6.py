# https://drive.google.com/file/d/1neKoHCH3e6r5qT4R3fEcjL3RNTTgKBW6/view?usp=sharing
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

id_char = int(input('Введите номер буквы: '))
char = chr(id_char + 96)
print('Вы ввели код буквы "', char, '"')