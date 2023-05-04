"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

import ipaddress

from lesson_9.task_1 import host_ping


def host_range_ping(ip_range: str, printable=True):
    try:
        ip_network = ipaddress.ip_network(ip_range)
    except Exception as ex:
        print(f'bad ip range {ex}')
    else:
        ip_list = [ip_address for ip_address in ip_network]
        return host_ping(host_list=ip_list, printable=printable)


host_range_ping('127.0.0.0/27')
