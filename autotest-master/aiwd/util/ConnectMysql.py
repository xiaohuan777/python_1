import pymysql

mysql_list = {"mysql":['192.168.18.118', 3306, 'ytxroot', 'ytxmysqlpass']}

def mysql_query(sql, mysql, instance):
    mysqldb = mysql_list[mysql]
    # 打开数据库连接 car mysql
    db = pymysql.connect(host = mysqldb[0], port = mysqldb[1], user = mysqldb[2], passwd=mysqldb[3], db=instance)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()[0]
    cursor.close()
    db.close()
    return result


if __name__ == '__main__':
    sql = "select * from t_question where id = '161'"
    result = mysql_query(sql, 'mysql', 'rjhy_ai')
    print(result)
    print(type(result))