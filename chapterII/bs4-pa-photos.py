import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"

resp = requests.get(url)
resp.encoding = "utf-8"

page = BeautifulSoup(resp.text, "html.parser")

# 获取图片的div的为止
divs = page.find_all("div", attrs={"class": "item masonry_brick"})

for div in divs:
    a = div.find("a", attrs={"class": "img_album_btn"})
    # 获取每个图片的打开连接地址
    child_url = url + a.get("href").split("/")[-1]
    child_resp = requests.get(child_url)
    child_resp.encoding = "utf-8"
    child_page = BeautifulSoup(child_resp.text, "html.parser")
    img = child_page.find("div", attrs={"class": "big-pic"}).find("img")
    src = img.get("src")
    p_name = src.split("/")[-1]
    time.sleep(1)
    img_resp = requests.get(src)
    # 创建的img文件夹，需要标注掉，让它作为扩展文件夹，这样IDEA不会创建索引
    with open("img/" + p_name, mode="wb") as f:
        f.write(img_resp.content)
        print("copy over: " + p_name)

print("over!")
