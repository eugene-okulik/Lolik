import os
import argparse


def find_text_in_file(file_path, search_text):
    results = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file, start=1):
            if search_text in line:
                results.append((i, line.strip()))
    return results


def extract_context(line, search_text, context_size=5):
    words = line.split()
    try:
        index = words.index(search_text)
        start_index = max(index - context_size, 0)
        end_index = min(index + context_size + 1, len(words))
        context_words = words[start_index:end_index]
        return ' '.join(context_words)
    except ValueError:
        return ''


def main(directory, text_to_find):
    print(f'Поиск текста "{text_to_find}" в папке {directory}')

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file_name in files:
        file_path = os.path.join(directory, file_name)

        found_lines = find_text_in_file(file_path, text_to_find)

        if found_lines:
            print(f'\nФайл: {file_name}')

            for line_number, line in found_lines:
                context = extract_context(line, text_to_find)
                print(f'Строка {line_number}: {context}')


parser = argparse.ArgumentParser(description="Анализатор лог файлов")
parser.add_argument("path", help="Путь к папке с логами")
parser.add_argument("--text", required=True, help="Текст для поиска")
args = parser.parse_args()
main(args.path, args.text)
