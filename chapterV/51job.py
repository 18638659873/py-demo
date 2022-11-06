from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()

web.get('https://login.51job.com/login.php')

# 输入账号
web.find_element(By.XPATH, '').send_keys("18638659873")
# 输入密码
web.find_element(By.XPATH, '').send_keys("yc793266")
# 点击登录
web.find_element(By.XPATH, '').click()

# 最大化浏览器窗口
web.maximize_window()
