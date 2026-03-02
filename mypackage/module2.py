from collections import Counter


def create_text_file(filename='text.txt', text=None):
    """Создает файл с русским текстом"""
    if text is None:
        text = "Привет! Как дела? Сегодня хорошая погода. Солнце светит."

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return text


def find_unique_chars(filename='text.txt'):
    """Находит символы, встречающиеся только один раз"""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Считаем частоту каждого символа
    freq = Counter(text)

    # Берем только те, которые встречаются 1 раз, сохраняя порядок
    unique = [char for char in text if freq[char] == 1]

    return ''.join(unique)