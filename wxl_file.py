def write_file():
    try:
        f = open('/Users/wuxiaolong/Desktop/Python3Learn.txt', 'w')  # 标示符'w'表示写
        f.write('Hello, Python')
    except BaseException as e:
        print(e)

    finally:
        if f:
            f.close()


def read_file():
    try:
        f = open('/Users/wuxiaolong/Desktop/Python3Learn.txt', 'r')  # 标示符'r'表示读
        # print(f.read())  # read()会一次性读取文件的全部内容
        print(f.readlines())  # 每次读取一行内容，返回list
    except BaseException as e:
        print(e)
    finally:
        if f:
            f.close()


def read_byte_file():
    try:
        f = open('/Users/wuxiaolong/Desktop/Python3Learn.png', 'rb')  # 标示符'rb'表示读
        print(f.read())  # read()会一次性读取文件的全部内容
        # print(f.readlines())  # 每次读取一行内容，返回list
    except BaseException as e:
        print(e)
    finally:
        if f:
            f.close()


# write_file()
# read_file()

read_byte_file()
# def with_file():
#     # 引入了with语句来自动帮我们调用close()方法
#     with open('/Users/wuxiaolong/Desktop/Python3Learn.txt', 'r', encoding='gbk', errors='ignore') as f:
#         print(f)
