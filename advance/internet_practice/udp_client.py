# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 19:15
# @Author  : huangkaiding


from socket import *

HOST = '10.10.2.178'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode(), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data)
udpCliSock.close()
