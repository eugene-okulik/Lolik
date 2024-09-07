# Task 1

text = "Etiam tincidunt neque erat, " \
        "quis molestie enim imperdiet vel. Integer urna nisl, " \
        "facilisis vitae semper at, dignissim vitae libero"

words = text.split()
# Здесь что я сделала
# new_str = ' '.join(f'{word}ing' for word in words)
# print(new_str)

# Здесь помог чат гпт
new_words = []
for word in words:
    if word[-1] in ",.":  # Проверяем, заканчивается ли слово на знак препинания
        new_words.append(word[:-1] + 'ing' + word[-1])  # Добавляем 'ing' перед знаком препинания
    else:
        new_words.append(word + 'ing')

print(' '.join(new_words))