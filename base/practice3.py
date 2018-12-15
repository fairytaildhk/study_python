# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 13:43
# @Author  : huangkaiding
import csv


def user(name, age, **kwargs):
    user_info = {'name': name, 'age': age}
    for k, v in kwargs.items():
        user_info[k] = v
    print(user_info)


def reader_csv():
    with open("test.csv", newline='') as f:
        csv_file = csv.reader(f, delimiter=' ', quotechar='|')
        for row in csv_file:
            data = {}
            case = []
            print(', '.join(row))


def reade_csv2():
    with open("test.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row1 in reader:
            print(row1['caseNo'], row1['test1'])


if __name__ == '__main__':
    user('Lilei', '18', city='shanghai')
    reader_csv()
    print('---------------')
    reade_csv2()
