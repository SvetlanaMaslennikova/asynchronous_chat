"""
Задание 2.
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

WORD_1 = b'class'
print(type(WORD_1))
print(WORD_1)
print(len(WORD_1))

WORD_2 = b'function'
print(type(WORD_2))
print(WORD_2)
print(len(WORD_2))

WORD_3 = b'method'
print(type(WORD_3))
print(WORD_3)
print(len(WORD_3))
