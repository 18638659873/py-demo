from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.alert import Alert
from time import sleep
import pandas as pd
import configparser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

config = configparser.ConfigParser()
config.read('config.ini')

# 现在可以像这样访问配置值
db_user = config['userinfo']['bd_username']
db_password = config['userinfo']['bd_password']

# 设置驱动浏览器配置参数
option = ChromeOptions()
option.add_argument('--start-maximized')  # 最大化窗口
# option.add_argument("--headless")  # 启用无头模式
# option.add_argument("--disable-gpu")  # 禁用GPU加速，某些情况下可能需要
option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 禁用自动化栏
option.add_experimental_option('useAutomationExtension', False)  # 禁用自动化栏的原理：将window.navigator.webdriver改为undefined。

# 屏蔽密码提示框
prefs = {'credentials_enable_service': False, 'profile.password_manager_enabled': False}

# 设置chrome操作参数
option.add_experimental_option('prefs', prefs)

# 反爬虫特征处理
option.add_argument('--disable-blink-features=AutomationControlled')

# 开启浏览器
driver = webdriver.Chrome(options=option)

# 打开访问地址
driver.get('https://pan.baidu.com/')

sleep(1)

# 读取JSON文件
with open('./Config.json', 'r') as f:
    data = json.load(f)

# 获取people数组
cookies = data['cookies']

# 将多个cookie添加到当前的页面
for cookie in cookies:
    driver.add_cookie(cookie)
# 刷新页面
driver.refresh()

print(driver.get_cookies())

# driver.find_element(By.XPATH, '/html/body/section/main/div/section/main/div/div[1]/div[3]/button').click()
#
# # 显式等待模态框出现
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "passport-login-pop")))
#
# # print(driver.page_source)
# # # 现在获取弹出框
# # alert = Alert(driver)
# # # 或者使用更常见的方法
# # alert = driver.switch_to.alert
#
#
# username = driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]')
# password = driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]')
#
# username.clear()
# username.send_keys(db_user)
# password.clear()
# password.send_keys(db_password)
# agree = driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__isAgree"]').click()
# sleep(0.2)
# loginBtn = driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]').click()


sleep(50)
