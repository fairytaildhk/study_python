# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 9:32
# @Author  : huangkaiding


if __name__ == '__main__':
    for value in range(1, 5):
        print(value)

    numbers = list(range(1, 6))
    print(numbers)

    even_numbers = list(range(1, 11, 2))
    print(even_numbers)

    squares = []
    for value in range(1, 11):
        squares.append(value ** 2)  # **乘方运算
    print(squares)

    # 列表解析
    squares = [value ** 2 for value in range(1, 11)]
    print(squares)

    # 数字列表的最小，最大，总和
    digits = [1, 3, 31, 311, 345, 67, 8, 9, 8, 0, 43, 567767, 445323, 5687, 86]
    print(min(digits))
    print(max(digits))
    print(sum(digits))
    print(digits[1:3])  # 切片
    # 使用切片复制列表
    digits_bck = digits[:]
    digits_bck.append('我不是数字')
    print(digits)
    print(digits_bck)

    dimensions = (200, 50)
    print(dimensions[0])

    print("练习" + '\n-----------------')
    numbers = list(range(1, 1000000))
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))
    # for number in numbers:
    #     print(number)