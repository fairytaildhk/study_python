# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 19:15
# @Author  : huangkaiding
import matplotlib.pyplot as plt

def test1():
    input_value = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_value, squares, linewidth=3)
    plt.title("test", fontsize=24)
    plt.xlabel("x_value", fontsize=14)
    plt.ylabel("y_value", fontsize=14)

    plt.tick_params(axis='both', labelsize=14)

    plt.show()
