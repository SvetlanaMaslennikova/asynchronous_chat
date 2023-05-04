"""
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable
10.0.0.1
10.0.0.2

Unreachable
10.0.0.3
10.0.0.4
"""

import tabulate

from lesson_9.task_2 import host_range_ping


def host_range_ping_tab(ip_range: str):
    result_dict = host_range_ping(ip_range, printable=False)
    print(tabulate.tabulate(result_dict, headers="keys"))


host_range_ping_tab('127.0.0.0/27')
