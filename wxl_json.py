import json

# Python 字典类型转换为 JSON 对象
python_data = {'id': 1024, 'name': 'wxl', 'site': 'http://wuxiaolong.me/'}
print(json.dumps(python_data))  # 打印：{"id": 1024, "name": "wxl", "site": "http://wuxiaolong.me/"}

# 将 JSON 对象转换为 Python 字典
json_data = '{"id": 1024, "name": "wxl", "site": "http://wuxiaolong.me/"}'
print(json.loads(json_data))  # 打印：{'id': 1024, 'name': 'wxl', 'site': 'http://wuxiaolong.me/'}
