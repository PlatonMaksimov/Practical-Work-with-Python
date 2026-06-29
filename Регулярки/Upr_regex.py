# Упражнение по регулярным выражениям (12 заданий).

import os
import re

BASE_DIR = os.path.dirname(__file__)
TEXT_PATH = os.path.join(BASE_DIR, 'test_text.txt')

with open(TEXT_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

TASKS = [
    {
        'title': '1. Натуральные числа (возможно, внутри букв)',
        'pattern': r'(?<=[a-zA-Zа-яА-ЯёЁ])\d+(?=[a-zA-Zа-яА-ЯёЁ])|\b[1-9]\d*\b',
    },
    {
        'title': '2. Последовательности ЗАГЛАВНЫХ букв',
        'pattern': r'[A-ZА-ЯЁ]{2,}',
    },
    {
        'title': '3. Русская буква, за которой цифра',
        'pattern': r'[а-яёА-ЯЁ]\d',
    },
    {
        'title': '4. Слова с большой русской или латинской буквы',
        'pattern': r'\b[A-ZА-ЯЁ][a-zA-Zа-яА-ЯЁё]*\b',
    },
    {
        'title': '5. Слова, начинающиеся на гласную',
        'pattern': r'\b[aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ][a-zA-Zа-яА-ЯЁё]*\b',
    },
    {
        'title': '6. Натуральные числа не на границе слова',
        'pattern': r'(?<=\w)\d+(?=\w)',
    },
    {
        'title': '7. Строки, содержащие символ *',
        'pattern': r'^.*\*.*$',
        'flags': re.MULTILINE,
    },
    {
        'title': '8. Строки с открывающей и позже закрывающей скобкой',
        'pattern': r'^[^\n]*\([^\n)]*\)[^\n]*$',
        'flags': re.MULTILINE,
    },
    {
        'title': '9. Блок оглавления с тегами',
        'pattern': r'<h1>Оглавление</h1>.*?</ol>',
        'flags': re.DOTALL,
    },
    {
        'title': '10. Текст оглавления без тегов (содержимое li)',
        'pattern': r'<li>\s*([^<]+?)\s*</li>',
    },
    {
        'title': '11. Пустые строки',
        'pattern': r'^\s*$',
        'flags': re.MULTILINE,
    },
    {
        'title': '12. Теги без содержимого',
        'pattern': r'<[^>]+>',
    },
]

print('Файл:', TEXT_PATH)
print('=' * 60)

for task in TASKS:
    flags = task.get('flags', 0)
    matches = re.findall(task['pattern'], text, flags)
    print(f"\n{task['title']}")
    print(f"Шаблон: {task['pattern']}")
    print(f"Найдено ({len(matches)}): {matches[:10]}")
    if len(matches) > 10:
        print('...')
