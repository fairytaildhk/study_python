# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 13:44
# @Author  : huangkaiding
import logging
import random


def even():
    """求100（包含100）以内的偶数"""
    ev = [i for i in range(100) if i % 2 == 0]
    logging.basicConfig(level=logging.NOTSET)
    logging.info(ev)
    # print(ev)


def convergence(a, b):
    if a - b < 2:
        return "a和b收敛于2"

if __name__ == '__main__':
    a_list = [i for i in range(10)]
    print(a_list)

    b_list = [random.randrange(1, 100) for i in range(5)]
    print(b_list)
    b_list.sort(reverse=True)
    print(b_list)
    b_list.insert(0, '999')
    b_list.insert(0, '999')
    print(b_list)
    q = b_list.pop(1)
    print(b_list)

    n = 10000  # @param {type:"number"}
    a = range(n)
    b = tuple(a)  # 把 a 转换成元组
    c = list(a)  # 把 a 转换成列表
    print(a.__sizeof__(), b.__sizeof__(), c.__sizeof__())

    a_set = {1, 2, 3, 4, 5, 6}
    b_set = {'a', 'b', 'c'}
    for i, t in enumerate(a_set):
        print(i, t)
    print(''.join(b_set))
    phonebook1 = {'ann': 6575, 'bob': 8982, 'joe': 2598, 'zoe': 1225}
    print(phonebook1.items())

    even()
