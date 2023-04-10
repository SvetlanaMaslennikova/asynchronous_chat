"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess
import chardet

ARGS_1 = ['ping', 'yandex.ru']
YA_PING_1 = subprocess.Popen(ARGS_1, stdout=subprocess.PIPE)
for line in YA_PING_1.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

ARGS_2 = ['ping', 'youtube.com']
YA_PING_2 = subprocess.Popen(ARGS_2, stdout=subprocess.PIPE)
for line in YA_PING_2.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
