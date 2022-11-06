# 爬取网易云音乐的热门评论 案例


import requests
# 安装加密工具
# pip install pycrypto -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip3 install -i https://pypi.douban.com/simple pycryptodome

from Crypto.Cipher import AES
from base64 import b64encode
import json

# 网页上传的参数为 加密前的参数 只需要改变 rid 和threadId 就可以继续访问其他音乐评论
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "A_PL_0_1989897584",
    "threadId": "A_PL_0_1989897584"
}

# 网页上的加密方式为i7b 就是加密前的数据， 后面的都是一个固定方法进行加密的，可以才console上运行后直接写死就行
"""
function a(a) { # 生成随机数 16的
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { # 分别调用 a b c方法
        var h = {}
          , i = a(16); 
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d, # 就是d方法
    window.ecnonasr = e
"""

# var bKB8t = window.asrsea(JSON.stringify(i7b), buU5Z(["流泪", "强"]), buU5Z(Rg1x.md), buU5Z(["爱心", "女孩", "惊恐", "大笑"]));
# window.asrsea  使用浏览器console 计算后的常量数据如下
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "LPP0iyzztnuax8I9"


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def get_encSecKey():
    return "b075b7d6376da58eb5ac8ba9dab340d6d8dc234b36216f87340a6561884ef85a3b0500d3cb9d5680b29030487471c811bbcef5e43816f20af62a4933a8b0dd502378b75e7c939ec586c4c3b862f0adf544b2cb5a377d6c2086d5e2028a045cd90caeb68b07db1fd12293baa89bfa2140fbf08c72d06d4821529de4aae4608662"


def enc_params(data, key):
    iv = "0102030405060708"
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    data = to_16(data)
    bs = aes.encrypt(data.encode("utf-8"))
    return str(b64encode(bs), "utf-8")


def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second


url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})

print(resp.text)
