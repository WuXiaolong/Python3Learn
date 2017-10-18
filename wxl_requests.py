import requests
from bs4 import BeautifulSoup

header = {"X-Bmob-Application-Id": '',
          "X-Bmob-REST-API-Key": '',
          "Content-Type": 'application/json'
          }
# Get  请求
response = requests.get('https://api.bmob.cn/1/classes/ArticleTable/', headers=header)

# obj = {"article_title": "title3",
#        "article_author": "author3",
#        "article_content": "content3",
#        "article_create_time": 20171012
#        }

# response = requests.post('https://api.bmob.cn/1/classes/article/', headers=header, json=obj)

# obj = {
#     "requests": [
#         {
#             "method": "POST",
#             "path": "/1/classes/article",
#             "body": {
#                 "article_title": "title3333",
#                 "article_author": "author3",
#                 "article_content": "content3",
#                 "article_create_time": 20171013
#             }
#         },
#         {
#             "method": "POST",
#             "path": "/1/classes/article",
#             "body": {
#                 "article_title": "title4444",
#                 "article_author": "author4",
#                 "article_content": "content4",
#                 "article_create_time": 20171014
#             }
#         }
#     ]
# }
# response = requests.post('https://api.bmob.cn/1/batch', headers=header, json=obj)
# 状态码
print(response.status_code)

# 原因短语
print(response.reason)

# 响应内容
print(response.text)
