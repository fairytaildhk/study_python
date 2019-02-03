# -*- coding: utf-8 -*-
# @Time    : 2019/2/2 17:36
# @Author  : huangkaiding
import fake as fake
import faker
from faker import Factory


def get_cre():
    fake1 = Factory.create()
    fake2 = faker.Faker()
    fake = faker.Faker("zh_CN")
    # cre = fake1.ssn(min_age=18, max_age=90)
    # cre1 = fake2.ssn(min_age=18, max_age=90)
    print(fake.ssn(min_age=18, max_age=90))
    print(fake.city())
    print(fake.name())
    print(fake.country())

if __name__ == '__main__':
    get_cre()
