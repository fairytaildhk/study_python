#coding=utf-8
import pymysql

from util.db_config import db_dic


def db_query(db, sql):
    # 连接数据库
    global db_info
    db_info = db_dic[db]
    conn = pymysql.connect(host=db_info[0], user=db_info[1],
                           password=db_info[2], db=db_info[3], port=db_info[4], charset='utf8')  # db：库名
    try:
        # 设置游标类型，默认游标类型为元祖形式
        # 将游标类型设置为字典形式
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        # 将表中所有数据以字典形式输出
        ret = cur.fetchall()
        # print(ret)
        # 提交
        conn.commit()
        # 关闭指针对象
        cur.close()
        return ret
    finally:
        # 关闭连接对象
        conn.close()


def db_update(db, sql):
    # 连接数据库
    global db_info
    db_info = db_dic[db]
    conn = pymysql.connect(host=db_info[0], user=db_info[1],
                           password=db_info[2], db=db_info[3], port=db_info[4], charset='utf8')  # db：库名
    try:
        # 设置游标类型，默认游标类型为元祖形式
        # 将游标类型设置为字典形式
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        conn.commit()
        # 关闭指针对象
        cur.close()
    finally:
        # 关闭连接对象
        conn.close()


if __name__ == '__main__':
    sql = "SELECT * from douban_movie where movie_name = 'test1'"
    sql1 = "INSERT INTO douban_movie(movie_name, detail) VALUES('测试一下中文', '哈哈')"

    # print(db_update('test', sql1))
    print(db_query('test', sql))

