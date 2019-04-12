# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 9:43
# @Author  : huangkaiding
from random import randrange

if __name__ == '__main__':
    print(randrange(10, 100))
    s = "Simple is better than complex."
    print(s)
    print(s.strip('Sibett selrx.pm'))  # p 全部处理完之后，p 并不在首部，所以原字符串中的 p 字母不受影响；
    print(s.strip('pSix.mle'))  # 这一次，首部的 p 被处理了…… 参数中的字符顺序对结果没有影响，换乘 Sipx.mle 也一样……

    a = 'test center string ha'
    print(a.title().center(60, '='))

    # 一、标识
    a = 'test1'
    b = "test2"
    c = """test3"""
    print(a, b, c)

    # 二、转义符
    d = '\'' '\"' '\t' 'test' '\n' 'test'
    print(d)
    """
    '"	test
    test
    """

    # 三、操作符
    e = 'test' + 'test'
    f = 'test' * 6
    g = 't' in f
    h = 't' not in f
    i = len(f)
    j = ['p', 'y', 't', 'h', 'o', 'n']
    k = ''.join(j)
    k_1 = '-'.join(j)
    j_2 = ('t', 'e', 's', 't')
    k_2 = ''.join(j_2)
    print(e, f, g, h, i, k, k_1, k_2)

    # 四、提取
    print('提取'.center(20, '-'))
    l = a[0], a[1:], a[:2], a[1:2]
    print(l)