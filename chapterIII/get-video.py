# 抓取一个视频
import requests
import re

url = "https://www.91kju.com/vod-play-id-63125-sid-2-pid-1.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

# resp = requests.get(url, headers=headers)
# print(resp.text)
# obj = re.compile(r'<div class="embed-responsive embed-responsive-16by9".*?"url":(?P<url>.*?)"', re.S)
#
# m3u8_url = obj.search(resp.text).group("url")
# resp.close()
# print(m3u8_url)
#
# # 这个网站太卡了，这里一直超时，就写死了一个
# # https://m3api.awenhao.com/index.php?note=kkRn6wdk9zexy5atb1hmg&raw=1&n.m3u8
# # https://m3api.awenhao.com/index.php?note=kkRch36nxfygq41jtps8m&raw=1&n.m3u8

# 下载m3u8文件
# m3u8_url = "https://m3api.awenhao.com/index.php?note=kkRch36nxfygq41jtps8m&raw=1&n.m3u8"
# resp2 = requests.get(m3u8_url, headers=headers)
# print(resp2.text)
# with open("myvideo.m3u8", mode="wb") as f:
#     f.write(resp2.content)
#
# resp2.close()


# 解析m3u8文件 下载视频
n = 1
with open("myvideo.m3u8", mode="r", encoding="utf-9") as f:
    for line in f:
        line = line.strip()
        if line.startswith("%"):
            continue
        else:
            print(line)
            resp3 = requests.get(line)
            f = open(f"{n}.ts", mode="wb")
            f.write(resp3.content)
            n += 1
