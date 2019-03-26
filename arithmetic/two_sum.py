# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 18:57
# @Author  : huangkaiding

def two_sum(nums, target):
    nums = [2, 7, 11, 15]
    target = 9
    nums_length = len(nums)
    for i in range(nums_length):
        for j in range(i + 1, nums_length):
            sum = nums[i] + nums[j]
            if sum == target:
                print([i, j])


if __name__ == '__main__':
    two_sum('', '')
