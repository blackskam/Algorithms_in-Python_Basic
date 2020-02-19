# https://drive.google.com/file/d/1Qg5S0lj-vx25SQR6mEott0H7NtuDbNU2/view?usp=sharing
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
x = 5
y = 6
z_bit_and = x & y
z_bit_xor = x ^ y
z_bit_or = x | y
z_bit_right = x >> 2
z_bit_left = x << 2
print('Побитовая операция «И» над числами 5 и 6: ', z_bit_and)
print('Побитовая операция «НЕ ИЛИ» над числами 5 и 6: ', z_bit_xor)
print('Побитовая операция «ИЛИ» над числами 5 и 6: ', z_bit_or)
print('Побитовый сдвиг вправо над числом 5: ', z_bit_right)
print('Побитовый сдвиг влево над числом 5: ', z_bit_left)



