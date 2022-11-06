from lxml import etree
import requests

url = "https://www.zbj.com/search/service/?kw=saas&r=1&nt=3553&fcn=图像识别&l=0"

resp = requests.get(url)

html = etree.HTML(resp.text)

divs = html.xpath("/html/body/div[6]")

print(divs)

for div in divs:
    pri = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")
    print(pri)
