# 安装requests
# pip install requests
import requests

url = "https://www.sogou.com/web?query=周杰伦"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

resp = requests.get(url, headers=headers)

print(resp.text)



