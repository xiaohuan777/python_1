# coding:utf-8
# import pymysql
# pymysql.install_as_MySQLdb()
# import MySQLdb.cursors
import pymysql.cursors
import json

class OperationMysql():
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='sqltest',
            charset='utf8',
            cursorclass = pymysql.cursors.DictCursor
        )
        self.cur = self.connect.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result

if __name__ == '__main__':
    op_mysql = OperationMysql()
    result = op_mysql.search_one("select * from stu where name='daniu'")
    print(result)

