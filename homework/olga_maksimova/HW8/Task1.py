# Задание 1
# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
#
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
#
# Примеры результатов:
#
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'
import random


def gen_salary(salary):
    salary = int(salary)
    bonus = random.choice([True, False])
    if bonus:
        bonus_amount = round(random.uniform(0, 0.05) * salary)
        total_salary = salary + bonus_amount
        return f'${total_salary}'
    else:
        return f'${salary}'


user_salary = input('Введите вашу зарплату: ')
result = gen_salary(user_salary)
print(result)
