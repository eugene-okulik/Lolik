# Возьмем задание из пятого занятия.
#
# Допустим, какая-то программа возвращает результат своей работы в таком виде:
#
# результат операции: 42
#
# результат операции: 54
#
# результат работы программы: 209
#
# результат: 2
#
# Нужно сделать всё то же самое, но уже способ - на ваше усмотрение (можно с помощью срезов и метода index,
# а можно с помощью split ). Получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте. Главное отличие - выполните всё с использованием функций. Нужно сделать так,
# чтобы строк кода стало как можно меньше, и не было повторений одного и того же.

line1 = 'результат операции: 42'
line2 = 'результат операции: 54'
line3 = 'результат работы программы: 209'


def hhh(line):
    result = int(line.split()[-1])
    print(result + 10)


hhh(line1)
hhh(line2)
hhh(line3)
