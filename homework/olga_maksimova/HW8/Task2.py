# Задание 2
# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
#
# На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.

def gen_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 1
for number in gen_fib():
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
        break
    count += 1
