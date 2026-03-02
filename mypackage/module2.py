from collections import Counter


def create_text_file(filename='text.txt', text=None):
    if text is None:
        text = "Привет! Как дела? Сегодня хорошая погода. Солнце светит."

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return text


def find_unique_chars(filename='text.txt'):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    freq = Counter(text)
    unique = [char for char in text if freq[char] == 1]

    return ''.join(unique)