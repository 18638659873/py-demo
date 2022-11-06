# 处理下载文件时，处理防盗链的问题
# 这里例子没有成功，因为加入了一个mrd随机生成的参数，这里无法获取，因此调用请求失败
import requests
import random

mrd = random.random()

url = "https://www.pearvideo.com/video_1527879"

contId = url.split("_")[1]

# 响应头地址： https://video.pearvideo.com/mp4/adshort/20180808/1664974178632-12624968_adpkg-ad_hd.mp4
# 真实地址是： https://video.pearvideo.com/mp4/adshort/20180808/cont-1407242-12624968_adpkg-ad_hd.mp4

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd={mrd}"
print(videoStatusUrl)
hearder = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    # 防盗链处理
    "Referer": url,
    "X-Requested-With": "XMLHttpRequest"
}

resp = requests.get(videoStatusUrl, hearder)
dic = resp.json()
print(dic)

srcUrl = dic["videoInfo"]["videos"]["srcUrl"]

systemTime = dic["systemTime"]

srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

# 下载视频
with open("a.mp4", mode="wb") as f:
    video_resp = requests.get(srcUrl)
    f.write(video_resp.content)
