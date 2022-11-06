import webbrowser

from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
from chaojiying import Chaojiying_Client

# 初始化超级鹰
chaojiying = Chaojiying_Client('18638659873', 'yc793266', '940344')

web = Chrome()

web.get('https://kyfw.12306.cn/otn/resources/login.html')

# 获取验证码
verify_img_ele = web.find_element(By.XPATH, '//*[@id="J-loginImg"]')
dic = chaojiying.PostPic(verify_img_ele.screenshot_as_png, 9004)

# 获取的是坐标 x1,y1|x2,y2
result = dic['pic_str']

res_list = result.split("|")
for rs in res_list:
    p_temp = rs.split(",")
    x = int(p_temp[0])
    y = int(p_temp[1])
    # 使用事件链 作用在web页面上，根据xy偏移量进行点击
    ActionChains(web).move_to_element_with_offset(verify_img_ele, x, y).click()

# 拖拽框  向右滑动小框
btn = web.find_element(By.XPATH, '//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()
