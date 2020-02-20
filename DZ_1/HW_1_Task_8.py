# https://drive.google.com/file/d/1buOOOidxDEl6saCyLMfcPiDXAfu5ZqSf/view?usp=sharing
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year_input = int(input('Введите год: '))
if year_input % 400 != 0 and year_input % 100 == 0 or year_input % 4 != 0:
    print('Вы ввели невисокосный год!')
else:
    print('Вы ввели високосный год')