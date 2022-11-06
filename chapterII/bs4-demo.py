# 安装 bs4
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/priceDetail.html"

resp = requests.get(url)

# print(resp.text)

# 使用bs4的beautifulSoup指定html解析器 解析上面的文本
page = BeautifulSoup(resp.text, "html.parser")

# 找到tbody元素，并要求class 属性上带有ul的
# table = page.find("tbody", attrs={"class": "ul"})
# table = page.find("tbody", attrs={"id": "tableBody"})

table = page.find("table")
list = table.find_all("th")

for it in list:
    print(it)
