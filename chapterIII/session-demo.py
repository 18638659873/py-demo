# 登录--- 带有cookie 状态 进行访问服务器

import requests

url = "https://passport.17k.com/ck/user/login"

session = requests.session()

data = {
    "loginName": "18638659873",
    "password": "yc793266"
}

# 先进行登录，并保存cookie的记录
session.post(url, data=data)

# 再次访问我的书架，会带上上面登录的时候获取的cookie的值，当然也可以直接带上登录的cookie的值
url2 = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"


resp = session.get(url2)
print(resp.json())
