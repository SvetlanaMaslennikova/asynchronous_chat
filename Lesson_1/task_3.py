"""
Задание 3.
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

WORD_1 = 'attribute'
WORD_2 = 'класс'
WORD_3 = 'функция'
WORD_4 = 'type'

WORD_LIST = [WORD_1, WORD_2, WORD_3, WORD_4]

# Вариант 1
for el in WORD_LIST:
    try:
        print(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{el}" невозможно записать в виде байтовой строки')

