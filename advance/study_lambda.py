# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 16:48
# @Author  : huangkaiding

add = lambda x, y: x + y


def make_incrementor(n):
    return lambda x: x + n


if __name__ == '__main__':
    print(add(1, 2))

    f = make_incrementor(42)
    print(f)
    print(f(0), '\n', f(1))

    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair: pair[1], reverse=True)
    print(pairs)
