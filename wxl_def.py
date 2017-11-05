# 函数
def hello():
    print('Hello，Python3')


hello()  # 函数调用


# 必传参数
def hello1(x, y):
    print(x, y)


hello1('必传', '参数')


# 默认参数
def hello2(x, y, z=8, name='wxl'):
    print(x, y, z, name)


hello2(666, 999)  # 相当于hello2(666, 999，8,'wxl')
hello2(666, 999, 888)  # 打印：666 999 888 wxl
hello2(666, 999, 888, 'WuXiaolong')  # 打印：666 999 888 WuXiaolong
hello2(666, 999, name='WuXiaodlong')  # 不按顺序提供默认参数，打印：666 999 8 WuXiaodlong


# 可变参数
def hello3(*y):
    print(y)


hello3(1, '2', 3.0, True)  # 打印：(1, '2', 3.0, True)
hello3('wxl')  # 打印：('wxl',)
hello3()  # 打印：()


def hello4(x, *y):
    print(x, y)


hello4(1, '2', 3.0, True)  # 打印：1 ('2', 3.0, True)
hello4('wxl')  # 打印：wxl ()


# 关键字参数
def hello5(x, **y):
    print(x, y)


hello5(1024)  # 打印：1024 {}
hello5(1024, name='WuXiaolong', code=520)  # 打印：1024 {'name': 'WuXiaolong', 'code': 520}


# 返回值
def hello6(x):
    return x


print(hello6(666))  # 打印：666


def hello7(x, y):
    return x, y


m = hello7(666, 999)
type(m)
print(type(m), m)  # 打印：<class 'tuple'> (666, 999)

# 全局变量
z = 1024


def hello8():
    global z
    z = 520
    print('z=' + str(z))  # z=520


hello8()
