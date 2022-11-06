import requests
from pyquery import PyQuery


def get_page_source(url):
    resp = requests.get(url)
    resp.encoding = "gbk"
    return resp.text


def parse_page_source(html):
    doc = PyQuery(html)
    mt_list = doc(".mt-10").items()
    for mt in mt_list:
        chexing = mt("div > dl:nth-child(1) > dd").eq(0).text()
        didiaan = mt("div >dl:nth-child(2) >dd").text()
        shijian = mt("div >dl:nth-child(4) >dd").text()
        youhao = mt("div >dl:nth-child(5)>dd").text()


if __name__ == '__main__':
    url = "https://k.autohome.com.cn/146/"
    html = get_page_source(url)
    parse_page_source(html)
