import requests

url = "https://fanyi.baidu.com/sug"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

dataFrom = {
    "kw": "dog"
}

resp = requests.post(url, data=dataFrom)
print(resp.json())
