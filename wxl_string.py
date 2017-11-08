name = 'I\'am WuXiaolong'
print(name)  # 输出字符串，打印：I'am WuXiaolong
print(len(name))  # 输出字符串长度
print(name[0])  # 输出第 1 个字符
print(name[0: - 1])  # 输出下标第 1 个位置到倒数第 2 位置的所有字符，打印：I'am WuXiaolon
print(name[5: 15])  # 输出下标从第 5 个到第 14 个位置的字符，打印：WuXiaolong
print(name[5:])  # 输出下标从第 5 个起后面所有的字符，打印：WuXiaolong
print(name * 2)  # 输出 2 次字符串
print('Hello,' + name)  # 字符串拼接，打印：Hello,I'am WuXiaolong
print('Wu' in name)  # True
print(name.find('Wu'))  # 查找，打印 5，即返回开始的索引值，否则返回-1
print(name.index('Wu'))  # 查找，打印 5，即返回开始的索引值，没有则抛异常
print('Wu' not in name)  # False
print(name.upper())  # 全部转大写
print(name.lower())  # 全部转小写
print(name.capitalize())  # 把字符串的第一个字符大写
print(name.isspace())  # 是否包含空格
print(name.replace('Wu', ''))  # 替换操作
print(name.split('m'))  # 分割操作，打印： ["I'a", ' WuXiaolong']
print(name.strip())  # 去掉字符串的左右空格
print(name.lstrip())  # 去掉字符串的左空格
print(name.rstrip())  # 去掉字符串的右空格

# 占位符
print('Hello,%s' % 'Python')  # 占位符：%d 表示那个位置是整数，%s 表示字符串
print('Hello,%d%s%.2f' % (666, 'Python', 9.999))  # 两个占位符，要写在一个圆括号内，中间用逗号（半角）隔开，打印：Hello,666Python10.00

w = '012345678'
s = '123456789'
print(s[2:5])

a = b = c = 100
print(a, b, c)

a, b, c = 100, 100.0, 'wxl'
print(a, b, c)

a = 1000
print(type(a))

print(isinstance(a, int))


