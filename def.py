# 函数

def hello():
    print('Hellp，Python3')


hello()  # 函数调用


# 必选参数
def hello(x, y):
    print(x, y)


hello('必须', '参数')


# 默认参数
def hello(x, y, z=8, name='wxl'):
    print(x, y, z, name)


# hello(666, 999)  # 相当于hello(666, 999，8,'wxl')
# hello(666, 999, 888, 'WuXiaolong')  # 打印：666 999 888 WuXiaolong
hello(666, 999, name='WuXiaodlong')  # 不按顺序提供默认参数，打印：666 999 8 WuXiaodlong


# 可变参数
def hello(*x):
    print(x)


hello(1, '2', 3.0, True)  # 打印：(1, '2', 3.0, True)
hello('wxl')  # 打印：('wxl',)
hello()  # 打印：()


# 关键字参数
def hello(x, **y):
    print(x, y)


hello(1024)  # 打印：1024 {}
hello(1024, name='WuXiaolong', code=520)  # 打印：1024 {'name': 'WuXiaolong', 'code': 520}


# 返回值
def hello(x):
    return x


print(hello(666))  # 打印：666


def hello(x, y):
    return x, y


m = hello(666, 999)
type(m)
print(type(m), m)  # 打印：<class 'tuple'> (666, 999)
