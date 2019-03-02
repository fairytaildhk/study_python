# -*- coding: utf-8 -*-
# @Time    : 2018/11/18 10:26
# @Author  : huangkaiding
from util import DBRequest


def querySupplierId(cityId):
    sql = "SELECT * FROM province_city_supplier WHERE city_code = %s" % cityId
    db_supplierId = DBRequest.db_query("has", sql)[0]['supplier_id']
    return db_supplierId


def queryCityIdByHotelId(hotel_id):
    sql = "select city_id from base_hotel_info where hotel_id = %s" % hotel_id
    cityId = DBRequest.db_query("his", sql)[0]['city_id']
    return cityId


def querySupplierIdByCityId(hotel_id):
    return querySupplierId(queryCityIdByHotelId(hotel_id))


# 根据订单号查询hotel_order_detail
def queryOrderDetailByOrderNo(orderNo):
    sql = 'SELECT * FROM hotel_order_detail WHERE order_no = "%s"' % orderNo
    print(sql)
    return DBRequest.db_query('hos', sql)[0]


if __name__ == '__main__':
    print(queryOrderDetailByOrderNo("1019201811261628146262016190809"))