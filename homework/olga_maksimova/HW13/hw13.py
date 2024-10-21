import os
import re
from datetime import datetime, timedelta


base_path = os.path.dirname(__file__)  # текущая папка
homework_path = os.path.dirname(os.path.dirname(base_path))  # поднялись выше
eu_path = os.path.join(homework_path, 'eugene_okulik')
file_path = os.path.join(eu_path, 'hw_13', 'data.txt')


def process_line(line, index):
    line = line.strip()
    # ищет соответствие шаблону в любом месте строки
    date_match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)', line)
    date_str = date_match.group(1)

    # Преобразуем строку с датой в объект datetime
    date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

    if index == 1:
        new_date = date_obj + timedelta(weeks=1)
        print(f"1. Дата на неделю позже: {new_date}")
    elif index == 2:
        day_of_week = date_obj.strftime('%A')
        print(f"2. День недели: {day_of_week}")
    elif index == 3:
        today = datetime.now()
        days_ago = (today - date_obj).days
        print(f"3. Эта дата была {days_ago} дней назад")


# Основная функция для чтения файла и обработки каждой строки
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as hw_file:  # Используем кодировку UTF-8
        for index, line in enumerate(hw_file, start=1):
            process_line(line, index)


# Запуск обработки файла
process_file(file_path)
