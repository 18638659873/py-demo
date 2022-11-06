from selenium.webdriver import Chrome
# 导入按键模拟
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

web = Chrome()
web.get("http://lagou.com")
time.sleep(1)
# 点击全国按钮 这个是基于导入上面的By实现的
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
el.click()
time.sleep(1)

web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("python", Keys.ENTER)
time.sleep(1)

div_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')

for div in div_list:
    job_name = div.find_element(By.XPATH, './div[1]/div[1]/div[1]/a').text
    print(job_name)

# web.close()
