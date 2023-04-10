"""
Задание 6.
Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

with open('test_file.txt') as codedFile:
    print(f'Кодировка файла: {codedFile.encoding}')
    for line in codedFile:
        encd_line = line.encode('utf-8')
        dcd_line = encd_line.decode('utf-8')
        print(dcd_line)
