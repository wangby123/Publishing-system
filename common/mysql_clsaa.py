import pymysql
"""
ip地址：47.104.190.48
用户名：root
密码：root
"""

def select_db(select_sql):
    '''查询数据库'''
    db = pymysql.connect(host='47.104.190.48',
                         port=3306,
                         user='root',
                         passwd='root',
                         db='xiaodai')

    # 创建一个游标对象cur
    cur = db.cursor()

    # 执行 SQL 查询
    cur.execute(select_sql)

    # 获取查询结果,返回元祖
    data = cur.fetchall()
    print(data)  # 取出对应的psw值

    # 关闭数据库连接
    db.close()
    return data

def insert_delete_update_db(insert_delete_update_sql):
    '''对数据赠、删、改操作'''
    # 打开数据库连接
    db = pymysql.connect(host='47.104.190.48',
                         port=3306,
                         user='root',
                         passwd='root',
                         db='xiaodai')

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    try:
        cur.execute(insert_delete_update_sql)  # 执行
        # 提交
        db.commit()
    except Exception as e:
        print("操作异常：%s" % str(e))
        # 错误回滚
        db.rollback()
    finally:
        db.close()

if __name__ == '__main__':
    for i in range(0, 99):
        sql = "('12', '孙膑', '男', '新疆', '26', '3班', '340322199000297655')"
    insert_delete_update_db(sql)
