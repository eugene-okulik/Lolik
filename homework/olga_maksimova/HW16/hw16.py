import dotenv
import os
import mysql.connector as mysql

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)  # текущая папка
homework_path = os.path.dirname(os.path.dirname(base_path))  # поднялись выше
eu_path = os.path.join(homework_path, 'eugene_okulik')
lesson_path = os.path.join(eu_path, 'Lesson_16')
file_path = os.path.join(lesson_path, 'hw_data', 'data.csv')

import csv

with open(file_path) as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

missing_rows = []  # Список строк, которых нет в базе данных

for row in data:
    name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

    # Формируем запрос для проверки наличия данных в базе
    query = f"""
        SELECT s.id, s.name, s.second_name, g.id AS group_id, g.title AS title_group,
        b.title AS taken_books, m.value AS mark,
        sub.title AS subject_title
        FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON s.id = b.taken_by_student_id
        LEFT JOIN marks m ON s.id = m.student_id
        LEFT JOIN lessons l ON m.lesson_id = l.id
        LEFT JOIN subjets sub ON l.subject_id = sub.id
        WHERE s.name = %s AND s.second_name = %s AND g.title = %s AND b.title = %s
          AND sub.title = %s AND l.title = %s AND m.value = %s
    """

    cursor.execute(query, (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))
    results = cursor.fetchall()

    if not results:
        missing_rows.append(row)

# Выводим строки, которых нет в базе данных
if missing_rows:
    print("Строки, которые отсутствуют в базе:")
    for row in missing_rows:
        print(", ".join(row))
else:
    print("Все данные из файла присутствуют в базе.")
