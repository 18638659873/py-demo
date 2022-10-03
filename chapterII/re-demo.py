import re

# findall 匹配所有的数据类型
list = re.findall(r"\d+", "匹配所有的数字类型：10010，以及还有10086")
print(list)

it = re.finditer(r"\d+", "匹配所有的数字类型：10010，以及还有10086")

for i in it:
    print(i.group())

# z找到一个结果就返回了
s = re.search(r"\d+", "匹配所有的数字类型：10010，以及还有10086")
print(s.group())

# 从头开始进行匹配
# m = re.match(r"\d+", "匹配所有的数字类型：10010，以及还有10086")
# print(m.group())

# 提前定义一个正则
reg = re.compile(r"\d+")

ret = reg.findall("匹配所有的数字类型：10010，以及还有10086")
print(ret)

s = """
<div class='jar'><span id='1'>小明</span></div>
<div class='yu'><span id='2'>小瑜</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)

its = obj.finditer(s)
for it in its:
    print(it.group("name"))
