"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

WORD_1 = 'разработка'
WORD_2 = 'администрирование'
WORD_3 = 'protocol'
WORD_4 = 'standard'

WORD_LIST = [WORD_1, WORD_2, WORD_3, WORD_4]

ELEMS_ENCODE = []
for el in WORD_LIST:
    el_encode = el.encode('utf-8')
    ELEMS_ENCODE.append(el_encode)
print(ELEMS_ENCODE)

ELEMS_DECODE = []
for el in ELEMS_ENCODE:
    el_decode = el.decode('utf-8')
    ELEMS_DECODE.append(el_decode)
print(ELEMS_DECODE)
