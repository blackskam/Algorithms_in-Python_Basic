# https://drive.google.com/file/d/1Y85UpafH6k-aaIFvoFCq-6999hLVBalv/view
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Ввведите трехзначное число: '))
dgt1 = a // 100
dgt2 = a % 100 // 10
dgt3 = a % 10
sum_dgt = dgt1 + dgt2 + dgt3
multi_dgt = dgt1 * dgt2 * dgt3
print('Сумма введенных цифр:', sum_dgt)
print('Произведение введенных цифр:', multi_dgt)
