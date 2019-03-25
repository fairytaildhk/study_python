# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 19:24
# @Author  : huangkaiding
import json

import schedule as schedule

from util import DBRequest, mail, DateTimeUtil
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.font_manager import _rebuild
import time as t
import datetime as dt


def record_order(date):
    """根据日期查询订单数，记录数据到本地数据库"""
    query_sql = "SELECT COUNT(*) c FROM hotel_order_detail WHERE create_day = '{date}' AND pay_status = 'Paid'".format(
        date=date)
    data = DBRequest.db_query('btc_hos', query_sql)[0]['c']
    sql = "SELECT COUNT(*) c FROM hotel_order_detail WHERE create_day = '{date}'".format(date=date)
    order_num = DBRequest.db_query('btc_hos', sql)[0]['c']
    print(data)
    insert_sql = "INSERT INTO order_statistics(`date`, `order_paid_count`, `order_num`) VALUES('{date}', {order_paid_count}, {order_num})".format(
        date=date, order_paid_count=data, order_num=order_num)
    DBRequest.db_update('test', insert_sql)


def query_order_num():
    """查询本地数据库的订单数据"""
    query_sql = "SELECT * FROM order_statistics ORDER BY date desc LIMIT 30"
    datas_db = DBRequest.db_query('test', query_sql)
    datas = list(reversed(datas_db))
    date_list = []
    order_paid_count_list = []
    order_num_list = []
    for data in datas:
        date_list.append(data['date'])
        order_paid_count_list.append(data['order_paid_count'])
        order_num_list.append(data['order_num'])

    print(date_list)
    print(order_paid_count_list)
    print(order_num_list)
    return date_list, order_paid_count_list, order_num_list


def paint():
    """画折线图"""
    date_list, order_paid_count_list, order_num_list = query_order_num()
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['font.family'] = 'sans-serif'
    fig, ax = plt.subplots(figsize=(18, 10))
    fig.autofmt_xdate()
    ax.plot(date_list, order_paid_count_list, 'o-', linewidth=3, label='已支付订单')
    ax.plot(date_list, order_num_list, 'o-', linewidth=3, label='所有订单')
    ax.legend(fontsize=20, loc="upper right")
    plt.title("订单量统计", fontsize=24)
    plt.xlabel("日期", fontsize=16)
    plt.ylabel("订单量", fontsize=16)
    ax.tick_params(axis='both', labelsize=18)
    # for a, b in zip(date_list, order_paid_count_list):
    #     ax.text(a, b, b, ha='center', va='bottom', fontsize=20)
    for i in range(len(date_list)):
        ax.text(date_list[i], order_paid_count_list[i], order_paid_count_list[i], ha='center', va='bottom', fontsize=20)
        ax.text(date_list[i], order_num_list[i], order_num_list[i], ha='center', va='bottom', fontsize=20)
    plt.savefig('order.png')
    plt.show()


def timing_task():
    """定时任务"""
    print("定时任务开启")

    # schedule.every(3).minutes.do(main)
    # schedule.every(10).minutes.do(job)
    # schedule.every().hour.do(job)
    schedule.every().day.at("08:00").do(main)
    # schedule.every(5).to(10).days.do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        t.sleep(1)


def send_mail():
    """发邮件"""
    mail.sendMail()


def main():
    """程序执行入口"""
    date = DateTimeUtil.getFutureDateTime(-1)
    record_order(date)
    paint()
    send_mail()


if __name__ == '__main__':
    # _rebuild()
    # date_list, order_paid_count_list, order_num_list = query_order_num()
    # paint()
    # a = {"s": "s",
    #          "q": "q", }
    # a_json = json.dumps(a, sort_keys=True, indent=4, separators=(',', ':'), skipkeys=False)
    # print(a_json)
    timing_task()
    # main()