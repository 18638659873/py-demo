# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQuery

from pyquery import PyQuery

html = """
    <ul>
        <li class ="aaa"><a href="www.baidu.com">百度</a> </li>
        <li class ="aaa"><a href="www.google.com">谷歌</a> </li>
    </ul>
"""

p = PyQuery(html)

# . 是类选择器 # 是id选择器，就是jquery的使用
a = p(".aaa")
print(a)
