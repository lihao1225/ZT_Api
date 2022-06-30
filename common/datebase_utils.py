"""
Author: lihao
Time: 2022/6/1

"""
import sys

import pymysql


class DateBaseUtil:

    def __init__(self):
        self.conn = self.get_conn()
        #创建游标
        self.cur = self.conn.cursor()

    def get_conn(self):
        conn = pymysql.connect(host="",
                               port="",
                               user="",
                               passwd="",
                               db="",
                               cursorclass=pymysql.cursors.DictCursor)
        return conn

    def find_one(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return self.cur.fetchone()
        except Exception as e:
            print(sys.exc_info())
        finally:
            print("执行成功")

    def close(self):
        self.cur.close()
        self.conn.close()
