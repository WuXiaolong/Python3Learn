import requests
from bs4 import BeautifulSoup
import sched
import time
from datetime import datetime

import pymysql


def create_table():
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='test4python')
    # 创建名为 developer 数据库语句
    sql = '''create table if not exists article (
    id int NOT NULL AUTO_INCREMENT, 
    article_title text,
    article_author text,
    article_content text,
    create_time text,
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


def insert_table(article_title, article_author, article_content, create_time):
    # 建立连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         db='test4python',
                         charset="utf8")
    # 插入数据
    query_sql = 'select * from article where article_title=%s'
    sql = 'insert into article (article_title,article_author,article_content,create_time) values (%s, %s, %s, %s)'
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        query_value = (article_title,)
        # 执行 sql 语句
        cursor.execute(query_sql, query_value)
        results = cursor.fetchall()
        if len(results) == 0:
            value = (article_title, article_author, article_content, create_time)
            cursor.execute(sql, value)
            # 提交事务
            db.commit()
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print('--------------《%s》 insert table success-------------' % article_title)
            return True
        else:
            print('--------------《%s》 已经存在-------------' % article_title)
            return False

    except BaseException as e:  # 如果发生错误则回滚
        db.rollback()
        print(e)

    finally:  # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()


create_time = 20170630


def get_html_data():
    # Get  请求
    response = requests.get('https://meiriyiwen.com/random')

    # 状态码
    print(response.status_code)

    # 原因短语
    print(response.reason)

    # 响应内容
    # print(response.content)

    soup = BeautifulSoup(response.content, "html5lib")
    article = soup.find("div", id='article_show')
    # print('article=%s' % article)
    article_title = article.h1.string
    # print('article_title=%s' % article_title)
    article_author = article.find('p', class_="article_author").string
    # print('article_author=%s' % article.find('p', class_="article_author").string)
    article_texts = article.find('div', class_="article_text").find_all('p')
    article_text = ''
    for a in article_texts:
        article_text = article_text + str(a)

    global create_time
    create_time = create_time - 1
    insert_table(article_title, article_author, article_text, create_time)


# 初始化sched模块的 scheduler 类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)


# 被周期性调度触发的函数
def print_time(inc):
    get_html_data()
    schedule.enter(inc, 0, print_time, (inc,))


# 默认参数60s
def main(inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    schedule.enter(0, 0, print_time, (inc,))
    schedule.run()


if __name__ == '__main__':
    # 10s 输出一次
    main(60 * 2)
    # create_table()
    # get_html_data()
