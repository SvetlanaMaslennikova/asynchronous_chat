"""
4. Продолжаем работать над проектом «Мессенджер»:
a) Реализовать скрипт, запускающий два клиентских приложения: на чтение чата и на запись в него.
Уместно использовать модуль subprocess).
b) Реализовать скрипт, запускающий указанное количество клиентских приложений.
"""

import subprocess


def start_clients(receiver_number=1, sender_number=0):
    port = 7777

    for cr in range(receiver_number):
        process = subprocess.Popen([f'python client.py -port {port} -login user{cr}_from_script -mode r'],
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   shell=True,
                                   )
        string = process.communicate()
        print(f'{string}')

    for cs in range(sender_number):
        process = subprocess.Popen([f'python client.py -port {port} -login user{cs}_from_script -mode s'],
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   shell=True,
                                   )
        string = process.communicate(input='hi from script'.encode())[0].decode()
        print(f'{string}')


start_clients(receiver_number=2, sender_number=2)
