# 使用代理去访问某些网站

import requests

# http://www.66ip.cn/areaindex_1/1.html

url = "https://www.baidu.com"
proxy = {
    "https": "https://183.172.217.109:7890"
}

resp = requests.get(url, proxies=proxy)
resp.encoding = "utf-8"

print(resp.text)
