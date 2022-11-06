from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from chaojiying import Chaojiying_Client

web = Chrome()

web.get("http://www.chaojiying.com/user/login/")

# 获取验证码图片
img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('18638659873', 'yc793266', '940344')

dic = chaojiying.PostPic(img, 1902)
print(dic)
verify_code = dic['pic_str']

web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("18638659873")
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("yc793266")
web.find_element(By.XPATH, '//html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
time.sleep(5)
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
