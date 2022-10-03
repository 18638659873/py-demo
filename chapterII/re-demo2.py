import re
import requests
import csv

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

result = requests.get(url, headers=headers)

page_content = result.text

# 打印网页信息
# with open("mycontent.html", mode="w", encoding="utf-8") as f:
#     f.write(page_content)

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', re.S)

its = obj.finditer(page_content)

f = open("data.csv", mode="w", encoding="utf-8")
csvfile = csv.writer(f)

for it in its:
    print(it.group("name"))
    print(it.group("year").strip())
    print(it.group("score"))
    print(it.group("num"))

    dic = it.groupdict()
    dic["year"] = dic["year"].strip()
    csvfile.writerow(dic.values())

f.close()

print("over!")
