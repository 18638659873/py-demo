import re
import requests

domain = "https://www.dytt89.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

resp = requests.get(domain, verify=False)
resp.encoding = "gb2312"

obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(
    r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)"',
    re.S)

result1 = obj1.finditer(resp.text)

child_href_list = []

for it in result1:
    ul = it.group("ul")
    # print(ul)
    # child_href_list.append(domain + ul.strip("/"))

    result2 = obj2.finditer(ul)

    for it2 in result2:
        ul2 = domain + it2.group("href").strip("/")
        # print(ul2)
        child_result = requests.get(ul2, verify=False)
        child_result.encoding = "gb2312"
        its3 = obj3.finditer(child_result.text)
        for it3 in its3:
            print(it3.group("movie"))
            # print(it3.group("download"))
