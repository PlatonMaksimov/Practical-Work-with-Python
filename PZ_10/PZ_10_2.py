# 2. Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы третей
# строки их числовыми кодами.

import string

with open('text18-3.txt', 'r', encoding='utf-16') as f:
    lines = f.readlines()

lines = [line.rstrip('\n') for line in lines]


print("Содержимое text18-3.txt:")
for line in lines:
    print(line)

punct_marks = string.punctuation + '—…'
count = 0
for line in lines[:4]:
    for ch in line:
        if ch in punct_marks:
            count += 1
print(f"\nЗнаков пунктуации в первых 4 строках: {count}")

if len(lines) >= 3:
    lines[2] = ' '.join(str(ord(c)) for c in lines[2])

with open('text18-3_new.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Готово! Создан файл: text18-3_new.txt")