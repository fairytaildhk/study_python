# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 9:59
# @Author  : huangkaiding


if __name__ == '__main__':
    s = 'dfasewes'
    print(s.find('e'), sorted(s))

    name = 'luka'
    name_reverse = name[::-1]
    ll = list(name)
    ll.reverse()
    result = "".join(ll)
    print(name, name_reverse, name[0:3:2], result)
