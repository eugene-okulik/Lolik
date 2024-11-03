import mysql.connector as mysql


# функция на отправку запроса и получения айдишников
def insert_and_get_ids(cursor, query, values):
    ids = []
    for value in values:
        # Выполняем запрос для каждого значения отдельно
        cursor.execute(query, value)
        # Сохраняем полученный id
        ids.append(cursor.lastrowid)
    return ids


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Добавляем пользователя
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
               ('Olga', 'Nukanukova', 333))
db.commit()
student_id = cursor.lastrowid
print(student_id)

# Получение данных студента по ID
student_id_query = "SELECT * FROM students WHERE id = %s"
cursor.execute(student_id_query, (student_id,))
print(cursor.fetchone())

# Cписок книг
book_values = [
    ("Distributed motivating installation644", student_id),
    ("Open-source disintermediate strategy 8", student_id),
    ("Visionary object-oriented moratorium", student_id)
]

insert_books_query = """
INSERT INTO books (title, taken_by_student_id)
VALUES (%s, %s)
"""
book_ids = insert_and_get_ids(cursor, insert_books_query, book_values)
db.commit()

for book_id in book_ids:
    print(f'ID книги: {book_id}')

# Добавляем группу и сохраняем её идентификатор
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ('OM', '1993-02-18', '2024-05-24'))
db.commit()
group_id = cursor.lastrowid  # Получаем идентификатор новой группы
print(group_id)

# Используем существующий group_id для обновления студента
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))
db.commit()

# Вставка предметов
subjects_data = [("Maths in English",), ("Birth or Die",), ("Hello World",)]
insert_subjects_query = "INSERT INTO subjets (title) VALUES (%s)"
subject_ids = insert_and_get_ids(cursor, insert_subjects_query, subjects_data)
db.commit()

for subject_id in subject_ids:
    print(f'ID предмета: {subject_id}')

# Используем первый subject_id для lessons_data
math_subject_id = subject_ids[
    0]  # if subject_ids else None # проверяет, не пуст ли список c subject_id, если пуст - None
lit_subject_id = subject_ids[1]  # if subject_ids else None
russ_subject_id = subject_ids[2]  # if subject_ids else None

lessons_data = [
    {"title": "Maths", "subject_id": math_subject_id},
    {"title": "Literature", "subject_id": lit_subject_id},
    {"title": "Russian lang", "subject_id": russ_subject_id}
]
insert_lessons_query = "INSERT INTO lessons (title, subject_id) VALUES (%(title)s, %(subject_id)s)"
lesson_ids = insert_and_get_ids(cursor, insert_lessons_query, lessons_data)
db.commit()

for lesson_id in lesson_ids:
    print(f'ID урока: {lesson_id}')

# Вставка оценок
marks_data = [
    {"value": "A", "lesson_id": lesson_ids[0], "student_id": student_id},
    {"value": "B", "lesson_id": lesson_ids[1], "student_id": student_id},
    {"value": "C", "lesson_id": lesson_ids[2], "student_id": student_id},
    {"value": "A-", "lesson_id": lesson_ids[0], "student_id": student_id},
    {"value": "B+", "lesson_id": lesson_ids[1], "student_id": student_id},
    {"value": "C+", "lesson_id": lesson_ids[2], "student_id": student_id}
]

insert_marks_query = """
INSERT INTO marks (value, lesson_id, student_id) VALUES (%(value)s, %(lesson_id)s, %(student_id)s)" """
mark_ids = insert_and_get_ids(cursor, insert_marks_query, marks_data)
db.commit()

for mark_id in mark_ids:
    print(f'ID оценки: {mark_id}')

# Выборка оценок студента
select_marks_query = "SELECT * FROM marks WHERE student_id = %s"
cursor.execute(select_marks_query, (student_id,))
marks_result = cursor.fetchall()
print("Оценки студента:")
for row in marks_result:
    print(row)

complex_select_query = """
SELECT s.id, s.name, s.second_name, g.id AS group_id, g.title AS title_group,
       b.title AS taken_books, m.value AS mark,
       GROUP_CONCAT(sub.title SEPARATOR ', ') AS subject_titles
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets sub ON l.subject_id = sub.id
WHERE s.id = %s
GROUP BY s.id, s.name, s.second_name, g.id, g.title, b.title, m.value;
"""

cursor.execute(complex_select_query, (student_id,))
full_info_result = cursor.fetchall()
print("\nПолная информация о студенте:")
for row in full_info_result:
    print(row)

# Закрытие соединения с базой данных
db.close()
