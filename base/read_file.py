# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 16:43
# @Author  : huangkaiding
import math
import time

if __name__ == '__main__':
    with open('file1.txt') as file:
        contents = file.read()
        print(contents)
        print('-------------------------')
    with open('file1.txt') as file:
        for line in file:
            print(line.rstrip())

    print('-------------------------')
    print(math.pi)

    with open('alice.txt',encoding='UTF-8') as file:
        contents = file.read()
        words = contents.split()

        print(len(words))