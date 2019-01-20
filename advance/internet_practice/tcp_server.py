# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 15:21
# @Author  : huangkaiding
import os
from socket import *
from time import ctime


def tcp_test1():

    HOST = ''
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建服务器套接字
    tcpSerSock.bind(ADDR)                      # 套接字与地址绑定
    tcpSerSock.listen(5)                       # 监听连接

    while True:  # 服务器无限循环
        print("等待连接...")
        tcpCliSock, addr = tcpSerSock.accept()  # 接受客户端连接
        print("...connected from:", addr)

        while True:  # 通信循环
            data = tcpCliSock.recv(BUFSIZ)  # 对话接收
            if not data:
                break
            tcpCliSock.send('[%s] %s'.encode() % (bytes(ctime(), 'utf-8'), data))  # 注意：将str转为bytes
        tcpCliSock.close()  # 关闭客户端套接字
    tcpSerSock.close()  # 关闭服务器套接字，目前永远不会运行到

if __name__ == '__main__':
    tcp_test1()