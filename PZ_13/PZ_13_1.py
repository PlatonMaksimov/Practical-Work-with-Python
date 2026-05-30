# В строках исходного текстового файла (dates1.txt) все даты представить в виде
# подстроки. Поместить в новый текстовый файл все даты февраля в формате
# ДД/ММ/ГГГГ.

import re

#Чтение файла
with open('dates1.txt', 'r', encoding='utf-8') as f:
    text = f.read()

#Извлечение всех дат в формате ДД.ММ.ГГГГ
dates = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)

#Отбор февральских дат
feb_dates = [d for d in dates if d.split('.')[1] == '02']

#Запись в новый файл в формате ДД/ММ/ГГГГ
with open('feb_dates.txt', 'w', encoding='utf-8') as f:
    for date in feb_dates:
        f.write(date.replace('.', '/') + '\n')

print("Все найденные даты:", dates)
print("\nФевральские даты в формате ДД/ММ/ГГГГ:")
for d in feb_dates:
    print(d.replace('.', '/'))