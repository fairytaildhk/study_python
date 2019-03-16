# -*- coding: utf-8 -*-
# @Author ：dhk
# @Time ：2019-03-09 15:10

from itertools import islice


def change():
    # 数据交换值
    x = 1
    y = 2
    x, y = y, x
    print("x:", x, "y:", y)


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def study_yield():
    while True:
        res = yield 4
        print("res:", res)


if __name__ == '__main__':
    change()
    print(list(islice(fib(), 5)))
    g = study_yield()
    print(next(g))
    print(next(g))
