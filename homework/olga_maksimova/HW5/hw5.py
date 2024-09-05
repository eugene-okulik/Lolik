# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)


# Task 2
line1 = 'результат операции: 42'
line2 = 'результат операции: 514'
line3 = 'результат работы программы: 9'

summ1 = int(line1[line1.index(":") + 2:])
summ2 = int(line2[line2.index(":") + 2:])
summ3 = int(line3[line3.index(":") + 2:])

print(summ1 + 10)
print(summ2 + 10)
print(summ3 + 10)


# Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students = ', '.join(students)
subjects = ', '.join(subjects)
my_text = 'Students {} study these subjects: {}'
print(my_text.format(students, subjects))
