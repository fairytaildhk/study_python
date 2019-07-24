# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 11:50
# @Author  : huangkaiding

"""
每月还款额=贷款本金×[月利率×(1+月利率) ^ 还款月数]÷{[(1+月利率) ^ 还款月数]-1}
等额本息还款公式推导 设贷款总额为A，银行月利率为β，总期数为m（个月），月还款额设为X，
则各个月末所欠银行贷款为：
第一个月末：A1 = A(1 + β) - X
第二个月末：
第三个月末：
…
由此可得第n个月末所欠银行贷款为：

由于还款总期数为m，也即第m月末刚好还完银行所有贷款，因此有：

由此求得：



"""
from decimal import Decimal, ROUND_UP, ROUND_DOWN


def data_processing(data):
    
    return Decimal(str(data)).quantize(Decimal('1.00'), rounding=ROUND_UP)


LOAN_PRINCIPAL = Decimal('520000')  # 贷款总额
ANNUAL_INTEREST_RATE = Decimal('0.05635')  # 年利率 5.635%
MONTHLY_INTEREST_RATE = ANNUAL_INTEREST_RATE / Decimal('12')  # 月利率 0.004695833333333333
months = Decimal('360')  # 总还款月数
X1 = Decimal('2996.70')

FIRST_MONTH = Decimal('4054.83')  # 2018/05/15 554.87  3499.96
"""
554.87  3499.96   519445.13
557.48  2439.22   518887.65
560.09  2436.61   518327.56
562.72  2433.98
565.36  2431.34
568.02  2428.68
570.68  2426.02
573.37  2423.33
"""

A1 = LOAN_PRINCIPAL - Decimal('554.87')
A2 = A1 * (Decimal('1') + MONTHLY_INTEREST_RATE) - X1
a_2 = data_processing(A1 - A2)

#  每月还款额
X = (LOAN_PRINCIPAL * MONTHLY_INTEREST_RATE * (1 + MONTHLY_INTEREST_RATE) ** months) / (
        (1 + MONTHLY_INTEREST_RATE) ** months - 1)
print(X, A1, A2, a_2)


def remain(m):
    A_m = LOAN_PRINCIPAL * (1 + MONTHLY_INTEREST_RATE) ** m - (
            X1 * ((1 + MONTHLY_INTEREST_RATE) ** m - 1)) / MONTHLY_INTEREST_RATE
    print(A_m)


n = 1

def detail(n, A1):

    A2 = Decimal(A1 * (1 + MONTHLY_INTEREST_RATE) - X1).quantize(Decimal('1.00'), rounding=ROUND_DOWN)
    a_2 = A1 - A2
    print(A2, a_2)
    n += 1
    if n <= 359:
        detail(n, A2)


if __name__ == '__main__':
    remain(15)
    print(Decimal('557.4722437083255').quantize(Decimal('1.00'), rounding=ROUND_UP))
    detail(n, A1)

    print(Decimal('51445.13') - Decimal('557.48'))