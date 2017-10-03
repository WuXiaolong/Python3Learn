dic = {'name': 'WuXiaolong', 'site': 'http://wuxiaolong.me/', 'code': 1024}
print(dic)
print(dic.keys())  # 输出所有键，打印：dict_keys(['name', 'site', 'code'])
print(dic.values())  # 输出所有值，打印：dict_values(['WuXiaolong', 'http://wuxiaolong.me/', 1024])
print(dic['site'])  # 输出键为 site 的值
dic['code'] = 520  # 修改元素
print(dic['code'])  # 打印：520
dic['id'] = 1314  # 新增元素
print(dic)  # 打印：{'name': 'WuXiaolong', 'site': 'http://wuxiaolong.me/', 'code': 520, 'id': 1314}
dic.pop('code')  # 删除 code 键
print(dic)  # 打印：{'name': 'WuXiaolong', 'site': 'http://wuxiaolong.me/', 'id': 1314}
dic.clear()  # 清空
print(dic)  # 打印：{}

# dict() 方法创建字典
d = dict(id=1024, name='wxl', site='http://wuxiaolong.me/')
print(d)
