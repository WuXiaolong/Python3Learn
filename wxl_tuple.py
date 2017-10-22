s = (100, 100.0, 'wxl', True, 'I\'am WuXiaolong', [1, 2, 3])

print(s)  # 输出 list，打印：(100, 100.0, 'wxl', True, "I'am WuXiaolong", [1, 2, 3])
print(s[0])  # 输出 list 第 1 个元素
print(s[2:5])  # 输出 lsit 下标从第 2 个到第 4个元素，打印：('wxl', True, "I'am WuXiaolong")
print(s[2:])  # 输出 lsit 下标从第 2 个起后面所有元素，打印：('wxl', True, "I'am WuXiaolong", [1, 2, 3])

s1 = (1, False)  # 单独一个元素 bool 类型不能加入 Tuple
print(s + s1)  # list 拼接，打印：(100, 100.0, 'wxl', True, "I'am WuXiaolong", [1, 2, 3], 1, False)
print(s * 2)  # 打印两次
print(len(s))  # 输出 list 长度
