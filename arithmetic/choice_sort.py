# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 20:10
# @Author  : huangkaiding


def select_sort(a_list):
    for i in range(len(a_list) - 1):
        min_index = i

        for j in range(i + 1, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
        print(a_list)


def insert_sort(a_list):
    for i in range(len(a_list) - 1):
        current_num = a_list[i + 1]
        index = i
        while index >= 0 and current_num < a_list[index]:
            a_list[index + 1] = a_list[index]
            index -= 1
        a_list[index + 1] = current_num
        print(a_list)


if __name__ == '__main__':
    a_list = [5, 9, 1, 2, 3]
    select_sort(a_list.copy())
    print("=" * 20)
    insert_sort(a_list.copy())
