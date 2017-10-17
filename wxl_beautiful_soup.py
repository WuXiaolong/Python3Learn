import requests
from bs4 import BeautifulSoup

# Get  请求
response = requests.get('https://meiriyiwen.com/')

# 状态码
print(response.status_code)

# 原因短语
print(response.reason)

# 响应内容
# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")
article = soup.find("div", id='article_show')
# print('article=%s' % article)
print('article title=%s' % article.h1.string)
print('article_author=%s' % article.find('p', class_="article_author").string)
print('article_text=%s' % article.find('div', class_="article_text"))
# for article in article_list:
#     # article_soup = BeautifulSoup(article, "html.parser")
#     post_title = article.a
#     print('post_title=%s' % post_title.string)

# print(article_list[0])

# article_list0 = article_list[0]
# print('post_title=%s' % article_list0.a.string)
# print('href=%s' % article_list0.a['href'])
# print('发表于=%s' % article_list0.time.string)
# print('分类于=%s' % article_list0.find('span', itemprop='name').string)
# # 如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点
# print('内容摘要=%s' % article_list0.find('div', class_='post-body'))
