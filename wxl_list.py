s = [100, 100.0, 'wxl', True, 'I\'am WuXiaolong']

# 访问元素
print(s)  # 输出 list，打印：[100, 100.0, 'wxl', True, "I'am WuXiaolong"]
print(len(s))  # 输出 list 长度
print(s[0])  # 输出 list 第 1 个元素
print(s[2:5])  # 输出 lsit 下标从第 2 个到第 4个元素，打印：['wxl', True, "I'am WuXiaolong"]
print(s[2:])  # 输出 lsit 下标从第 2 个起后面所有元素，打印：['wxl', True, "I'am WuXiaolong"]

# 添加元素
s1 = [False]
print(s + s1)  # list 拼接，打印：[100, 100.0, 'wxl', True, "I'am WuXiaolong", False]

# 在列表末尾一次性追加另一个列表
s.extend(s1)
print('extend 添加 = ' + str(s))  # extend 添加 = [100, 100.0, 'wxl', True, "I'am WuXiaolong", False]

# append 方法拼接，列表末尾添加新的对象
s.append('测试拼接')
print('append 方法拼接 = ' + str(s))  # append 方法拼接 = [100, 100.0, 'wxl', True, "I'am WuXiaolong", False, '测试拼接']

s.insert(0, '测试拼接')  # 指定位置插入元素
print('insert 插入 = ' + str(s))  # insert 插入 = ['测试拼接', 100, 100.0, 'wxl', True, "I'am WuXiaolong", False, '测试拼接']

# 更新元素
s[0] = '1024'
print('更新元素 = ' + str(s))  # 更新元素 = ['1024', 100, 100.0, 'wxl', True, "I'am WuXiaolong", False, '测试拼接']

# 删除元素
s.pop()  # pop 方法删除，可指定位置，默认最后一个
print(s)  # 打印：['1024', 100, 100.0, 'wxl', True, "I'am WuXiaolong", False]

s.pop(0)  # pop 指定位置删除
print(s)  # 打印：[[100, 100.0, 'wxl', True, "I'am WuXiaolong", False]

del s[0]
print(s)  # 打印：[100.0, 'wxl', True, "I'am WuXiaolong", False]

# 移除列表中某个值的第一个匹配项，没有会抛异常
s.remove('wxl')
print(s)

# 其他
print(s * 2)  # 打印两次

s.reverse()  # 反向列表中元素
print(s)

s2 = s.copy()  # 复制
print(s2)

s.clear()  # 清空
print(s)
