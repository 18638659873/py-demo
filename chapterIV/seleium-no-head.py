# 在不打开谷歌浏览器的情况下，后台运行浏览器去获取一些页面上的数据
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
# 设置无头浏览器属性
opt.add_argument("--headless")
# 不适用GPU 显卡
opt.add_argument("--disable-gpu")

web = Chrome(options=opt)

web.get('https://ys.endata.cn/BoxOffice/Ranking')

sel_el = web.find_element(By.XPATH, '//*[@id="OptionDate"]')

sels = Select(sel_el)

for i in range(len(sels.options)):
    sels.select_by_index(i)
    time.sleep(2)
    table = web.find_element(By.XPATH, '')
    print(table.text)

# 获取页面源代码，这个是经过ajax加载后的页面
web.page_source

web.close()
