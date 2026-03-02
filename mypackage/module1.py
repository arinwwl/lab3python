import random


def generate_numbers_file(filename='numbers.txt', count=50):
    """Генерирует файл с натуральными числами"""
    with open(filename, 'w', encoding='utf-8') as f:
        numbers = [str(random.randint(1, 100)) for _ in range(count)]
        f.write(' '.join(numbers))
    return numbers


def find_odd_squares(filename='numbers.txt'):
    """Находит квадраты нечетных чисел"""
    with open(filename, 'r', encoding='utf-8') as f:
        numbers = list(map(int, f.read().split()))

    result = []
    for n in numbers:
        if n % 2 == 1:  # нечетное
            root = int(n ** 0.5)
            if root * root == n:  # проверка на квадрат
                result.append(n)

    return result