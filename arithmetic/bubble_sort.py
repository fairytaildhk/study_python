# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 15:35
# @Author  : huangkaiding
import datetime
import random
import time


def bubble_sort_1(a_list):
    a_len, count_exchange, count = len(a_list), 0, 0
    start_time = time.time()
    for i in range(a_len - 1):
        count += 1
        for j in range(a_len - i - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                count_exchange += 1
    end_time = time.time()
    print('轮数:' + str(count), '交换次数:' + str(count_exchange), '排序需要时间:' + str(end_time - start_time), sep=' | ')


def bubble_sort_2(a_list):
    """分析看来这种方案，进行排序的轮数是少了，但是时间复杂度没有降低，反而耗时更长了，从代码分析来看，
    给flag变量赋值的次数远远大于优化前的循环次数，也许这就是耗时更多的原因"""
    a_len, count_exchange, count = len(a_list), 0, 0
    start_time = time.time()
    for i in range(a_len - 1):
        flag = False
        count += 1
        for j in range(a_len - i - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                flag = True
                count_exchange += 1
        if not flag:
            break
    end_time = time.time()
    print('轮数:' + str(count), '交换次数:' + str(count_exchange), '排序需要时间:' + str(end_time - start_time),
          sep=' | ')


def bubble_sort_3(a_list):
    a_len, count_exchange, count = len(a_list), 0, 0
    index_min, index_max = 0, a_len - 1
    start_time = time.time()
    while index_min < index_max:
        index_last_swap = index_min
        count += 1
        for j in range(index_min, index_max):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                count_exchange += 1
                index_last_swap = j
        index_max = index_last_swap
        for j in range(index_max, index_min, -1):
            if a_list[j] < a_list[j - 1]:
                a_list[j], a_list[j - 1] = a_list[j - 1], a_list[j]
                count_exchange += 1
                index_last_swap = j
        index_min = index_last_swap
    end_time = time.time()
    print('轮数:' + str(count * 2), '交换次数:' + str(count_exchange), '排序需要时间:' + str(end_time - start_time), sep=' | ')


if __name__ == '__main__':
    # a = [3, 6, 415, 1, 78, 9, 65]
    c = list(range(50000))
    a = random.sample(c, 1000)
    # print(a)
    for i in range(5):
        print('='*20)
        bubble_sort_1(a.copy())
        bubble_sort_2(a.copy())
        bubble_sort_3(a.copy())
