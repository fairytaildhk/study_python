# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 10:37
# @Author  : huangkaiding


def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')


def say_hi2(**names_greetins):
    for name, greeting in names_greetins.items():
        print(f'{greeting},{name}!')


def say_hi3(*names, greeting='Hello', capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')


if __name__ == '__main__':
    say_hi('luka')
    names = ('luka1', 'luka2', 'luka3')
    say_hi(*names)
    say_hi2(luka4='hello')
    a_dic = {'luka5': 'hello'}
    say_hi2(**a_dic)
    say_hi3(*names, greeting='Haha', capitalized=True)
