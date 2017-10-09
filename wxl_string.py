name = 'I\'am WuXiaolong'
print(name)  # 输出字符串，打印：I'am WuXiaolong
print(len(name))  # 输出字符串长度
print(name[0])  # 输出第 1 个字符
print(name[0: - 1])  # 输出下标第 1 个位置到倒数第 2 位置的所有字符，打印：I'am WuXiaolon
print(name[5: 15])  # 输出下标从第 5 个到第 14 个位置的字符，打印：WuXiaolong
print(name[5:])  # 输出下标从第 5 个起后面所有的字符，打印：WuXiaolong
print(name * 2)  # 输出 2 次字符串
print('Hello,' + name)  # 字符串拼接，打印：Hello,I'am WuXiaolong
print('Hello,%s' % 'Python')  # 占位符：%d 表示那个位置是整数，%s 表示字符串
print('Hello,%d%s%.2f' % (666, 'Python', 9.9))  # 两个占位符，要写在一个圆括号内，中间用逗号（半角）隔开，打印：Hello,666Python10.00

w = '012345678'
s = '123456789'
print(s[2:5])
# 整型变量
a = 100
# 浮点型变量
b = 100.0
# 字符串
c = 'wxl'
print(a, b, c)

a = b = c = 100
print(a, b, c)

a, b, c = 100, 100.0, 'wxl'
print(a, b, c)

a = 1000
# print(type(a))

print(isinstance(a, int))

print(9 / 4)  # 返回 2.25
print(9 // 4)  # 返回 2
print(2 ** 3)  # 返回 8
