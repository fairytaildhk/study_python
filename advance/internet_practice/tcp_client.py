# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 15:37
# @Author  : huangkaiding
from socket import *


def tcp_client_test():
    HOST = '10.10.2.188'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    while True:
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(data.encode())  # 注意：将输入的str编码转为bytes
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
    tcpCliSock.close()

if __name__ == '__main__':
    tcp_client_test()