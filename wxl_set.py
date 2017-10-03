s = {'name', 'site', 'code', 1, 1}
print(s)  # 输出集合，重复的元素被自动去掉

# set可以进行集合运算
a = set('123456')
b = set('567890')
print(a - b)  # a和b的差集
print(a | b)  # a和b的并集
print(a & b)  # a和b的交集
print(a ^ b)  # a和b中不同时存在的元素
