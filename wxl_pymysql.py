import pymysql


def create_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='test4python')
    # 创建名为 developer 数据库语句
    sql = '''create table if not exists developer (
    id int NOT NULL AUTO_INCREMENT, 
    name text,
    job text,
    site text,
    PRIMARY KEY (`id`)
    )'''
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 执行 sql 语句
        cursor.execute(sql)
        # 提交事务
        db.commit()
        print('create table success')
    except BaseException as e:  # 如果发生错误则回滚
        db.rollback()
        print(e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()


def insert_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='test4python')
    # 插入数据
    sql = 'insert into developer (name,job,site) values (%s, %s, %s)'
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        value = ('wxl', 'Android', 'http://wuxiaolong.me/')
        # 执行 sql 语句
        cursor.execute(sql, value)
        # 提交事务
        db.commit()
        print('insert table success')

    except BaseException as e:
        # 如果发生错误则回滚
        db.rollback()
        print(e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()


def query_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='test4python')
    # 查询语句
    sql = 'select * from developer'
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 执行 sql 语句
        cursor.execute(sql)
        # 查询一条记录
        result = cursor.fetchone()
        print('查询一条记录：id=%s,name=%s,job=%s,site=%s' % (result[0], result[1], result[2], result[3]))
        # 如果先用 fetchone()，游标是从 1 开始
        # 重置游标位置，偏移量:大于0向后移动;小于0向前移动，mode默认是relative
        # relative:表示从当前所在的行开始移动; absolute:表示从第一行开始移动
        cursor.scroll(0, mode='absolute')
        # 查询多条记录
        results = cursor.fetchall()
        for row in results:
            print('查询多条记录：id=%s,name=%s,job=%s,site=%s' % (row[0], row[1], row[2], row[3]))

    except BaseException as e:
        # 如果发生错误则回滚
        db.rollback()
        print(e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()


def update_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='test4python')
    # 更新数据
    sql = 'update developer set name=%s where id=%s'
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        value = ('WuXia33olong', 3)
        # 执行 sql 语句
        cursor.execute(sql, value)
        # 提交事务
        db.commit()
        print('update table success')

    except BaseException as e:
        # 如果发生错误则回滚
        db.rollback()
        print(e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()


def delete_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='test4python')
    # 更新数据
    sql = 'delete from developer where id=%s'
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql, 4)
        # 提交事务
        db.commit()
        print('delete table success')

    except BaseException as e:
        # 如果发生错误则回滚
        db.rollback()
        print(e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()


if __name__ == '__main__':
    # create_table()
    # insert_table()
    # query_table()
    update_table()
    delete_table()
