"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""

import subprocess
import ipaddress
import socket
import re


def host_ping(host_list: list, printable=True):
    result_dict = {"reachable": [],
                   "unreachable": []}

    for host in host_list:
        ip_address = ''
        try:
            ip_address = ipaddress.ip_address(host)
        except Exception as ex:
            pass

        try:
            ip_address = ipaddress.ip_address(socket.gethostbyname(host))
        except Exception as ex:
            pass

        process = subprocess.Popen(['ping', '-c', '1', str(ip_address)], stdout=subprocess.PIPE)
        string = process.stdout.read().decode('utf-8')
        try:
            result = re.findall(r'time=.*', string)[0]
        except Exception:
            result_dict["unreachable"].append(host)
            if printable:
                print(f'Узел "{host}" недоступен')
        else:
            result_dict["reachable"].append(host)
            if printable:
                print(f'Узел "{host}" доступен')

    return result_dict


host_list = ['127.0.0.1', '127.0.0.2', 'google.com', '192.168.142.200']
host_ping(host_list)
