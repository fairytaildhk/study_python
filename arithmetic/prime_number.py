# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 11:54
# @Author  : huangkaiding


def prime():
    for i in range(2, 100):
        if i == 2:
            print(i)
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


def prime_1():
    prime_list = []
    for i in range(2, 100):
        if i == 2:
            prime_list.append(i)
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    print(prime_list)


if __name__ == '__main__':
    prime_1()
