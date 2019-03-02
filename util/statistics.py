# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 19:15
# @Author  : huangkaiding
import datetime
import os
import re


def statistics():
    # 需要过滤的目录
    filter = ['.pytest_cache', '__init__.py', '__pycache__']
    # 测试用例的路径
    path = os.path.join(os.path.abspath('..'), 'testcase')
    result = []  # 过滤后的目录存放
    pat = "test(.*?).py$"   # 正则找出test打头.py结尾的文件
    pat1 = "def test(.*?)"
    pat2 = "assert"
    # 获取指定路径下的目录名字
    list = os.listdir(path)
    caseTotal = 0  # 用例总数
    assertTotal = 0  # 断言总数
    stas = []  # 保存到文件的列表
    # 把不需要的目录名过滤
    for dir in list:
        if dir not in filter:
            result.append(dir)
    print(result)
    # 遍历过滤后的result中的目录
    for res in result:
        print('---------------------\n' + res + "应用下：")
        path1 = os.path.join(path, res)  # 拼出当前目录的路径
        caseNum = 0
        assertNum = 0
        for root, dirs, files in os.walk(path1):
            for file_1 in files:
                if re.compile(pat, re.S).findall(file_1):
                    # 当前测试类的文件路径
                    path2 = os.path.join(root, file_1)
                    with open(path2, 'r', encoding='UTF-8') as file_test:
                        str1 = file_test.readlines()
                        for str2 in str1:
                            if re.compile(pat1, re.S).findall(str2):
                                caseNum = caseNum + 1
                            if re.compile(pat2, re.S).findall(str2):
                                assertNum = assertNum + 1
        print("用例数：" + str(caseNum))
        print("检查点数：" + str(assertNum))
        stas.append(res + "应用：" + " 用例数 " + str(caseNum) + " 检查点数 " + str(assertNum))
        caseTotal = caseTotal + caseNum
        assertTotal = assertTotal + assertNum

    print('----------------------------\n' + "用例总数：" + str(caseTotal))
    print("检查点总数：" + str(assertTotal))
    stas.append('--------------------------------------\n' + "用例总数：" + str(caseTotal))
    stas.append("检查点总数：" + str(assertTotal))
    print(stas)
    with open(os.path.join(os.path.abspath('..'), 'statistics.txt'), 'a', encoding='utf-8') as f:  # 使用with open()新建对象f
        f.write('======================================\n' + '统计日期：' + str(datetime.datetime.now()) + '\n')
        for s in stas:
            f.write(s + '\n')  # 写入数据，文件保存在上面指定的目录


if __name__ == '__main__':
    statistics()
