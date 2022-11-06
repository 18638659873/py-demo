# 安装xpath 这里指定清华源 进行安装会成功
# pip install lxml -i https://pypi.tuna.tsinghua.edu.cn/simple

from lxml import etree

# 加载本地文件，并且指定解析器为html解析
tree = etree.parse('./a.html', etree.HTMLParser())

# result = tree.xpath('/html')
# 获取 a 元素中的文本
# result = tree.xpath('/html/body/ul/li/a/text()')
# 获取第一个a元素中的数据
# result = tree.xpath('/html/body/ul/li[1]/a/text()')
# 获取href = dapao的元素的文本
# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")


lis = tree.xpath("/html/body/ol/li")

for li in lis:
    # 使用相对路径获取li 下的a元素的值
    a = li.xpath("./a/text()")
    print(a)

div = tree.xpath("/html/body/div[1]/text()")
print(div)
