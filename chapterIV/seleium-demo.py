# 程序连接浏览器
# seleium : 自动化测试工具
# 可以打开浏览器，模仿人去操作浏览器
# 搭建环境
# pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
# 下载浏览器驱动 https://npm.taobao.org/mirrors/chromedriver  http://chromedriver.storage.googleapis.com/index.html
# 再把解压后的exe 文件在python的安装目录下复制一份
# 下面路也放一份，或者配置环境变量
# C:\Program Files (x86)\Google\Chrome\Application

from selenium.webdriver import Chrome

web = Chrome()
web.get("http://www.baidu.com")
# web.close()
print(web.title)