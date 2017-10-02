s = [100, 100.0, 'wxl', True, 'I\'am WuXiaolong']
s1 = [False]
print(s)  # 输出 list，打印：[100, 100.0, 'wxl', True, "I'am WuXiaolong"]
print(len(s))  # 输出 list 长度
print(s[0])  # 输出 list 第 1 个元素
print(s[2:5])  # 输出 lsit 下标从第 2 个到第 4个元素，打印：['wxl', True, "I'am WuXiaolong"]
print(s[2:])  # 输出 lsit 下标从第 2 个起后面所有元素，打印：['wxl', True, "I'am WuXiaolong"]
print(s + s1)  # list 拼接，打印：[100, 100.0, 'wxl', True, "I'am WuXiaolong", False]
s.append('测试拼接')
print(s)  # append 方法拼接，打印：[100, 100.0, 'wxl', True, "I'am WuXiaolong", '测试拼接']
s.insert(0, '测试拼接')  # 指定位置插入元素
print(s)  # 打印：['测试拼接', 100, 100.0, 'wxl', True, "I'am WuXiaolong", '测试拼接']
s.pop()  # pop 方法删除，可指定位置，默认最后一个
s.pop(0)  # pop 指定位置删除
print(s)  # 打印：[100, 100.0, 'wxl', True, "I'am WuXiaolong"]
print(s * 2)  # 打印两次
