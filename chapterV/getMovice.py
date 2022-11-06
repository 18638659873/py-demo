import requests

from bs4 import BeautifulSoup

# 获取网页信息
text = requests.get('https://www.cbooo.cn/year?year=2008').text

main_page = BeautifulSoup(text, "html.parser")

table = main_page.find("table", attrs={"id": "tbContent"})

trs = table.find_all("tr")

for tr in trs:
    lst = tr.find_all("td")
    if len(lst) != 0:
        for td in lst:
            print(td.text)

