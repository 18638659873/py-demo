from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

web = Chrome()

web.get("http://lagou.com")

el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
el.click()
time.sleep(1)

web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys('python', Keys.ENTER)
time.sleep(1)

# 这个命令会重新打开一个新的页面
web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
time.sleep(1)

# 切换到浏览器窗口的最后一个页面
web.switch_to.window(web.window_handles[-1])

time.sleep(1)
job_detail = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

# 关掉子窗口
web.close()

web.switch_to.window(web.window_handles[0])

# seleium 操作 iframe
# web.get('https://www.91kanju.com/vod-play/541-2-1.html')
# iframe = web.find_element(By.XPATH, '//*[@id="player_ifram"]')
# 切换到frame页面
# web.switch_to.frame(iframe)
# web.find_element()
# 切换会源页面
# web.switch_to.default_content()
