from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
from time import sleep
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# 现在可以像这样访问配置值
db_user = config['userinfo']['username']
db_password = config['userinfo']['password']

# 设置驱动浏览器配置参数
option = ChromeOptions()
option.add_argument('--start-maximized')  # 最大化窗口
option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 禁用自动化栏
option.add_experimental_option('useAutomationExtension', False)  # 禁用自动化栏的原理：将window.navigator.webdriver改为undefined。
# option.add_argument("--headless")  # 设置无头浏览器属性
# option.add_argument("--disable-gpu")  # 不适用GPU 显卡

# 屏蔽密码提示框
prefs = {
    'credentials_enable_service': False, 'profile.password_manager_enabled': False
}

# 设置chrome操作参数
option.add_experimental_option('prefs', prefs)

# 反爬虫特征处理
option.add_argument('--disable-blink-features=AutomationControlled')

# 开启浏览器
driver = webdriver.Chrome(options=option)

# 打开访问地址
driver.get(
    'https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21bo.jianhua.754894437.1.5af92a89zyJDZq%26pm_id%3D1501036000a02c5c3739')

# 创建动作
action = ActionChains(driver)

# 输入用户名
username = driver.find_element(By.XPATH, '//*[@id="fm-login-id"]')
username.clear()
username.send_keys(db_user)
# 数据密码
password = driver.find_element(By.XPATH, '//*[@id="fm-login-password"]')
password.clear()
password.send_keys(db_password)
# 点击登录
login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/button')
login_button.click()
sleep(2)

driver.find_element(By.XPATH, '//*[@id="bought"]').click()
sleep(2)
goods_elements = driver.find_elements(By.XPATH,
                                      '//*[@id="tp-bought-root"]/div[@class="index-mod__order-container___1ur4- js-order-container"]')

# 创建一个空列表来存储数据
data = []
# 创建一个空的数据框
df = pd.DataFrame(columns=['时间', '订单', '店铺', '商品', '链接', '聊天记录'])

for index, goods_element in enumerate(goods_elements):
    order_time = goods_element.find_element(By.XPATH, './div/table/tbody[1]/tr/td[1]/label/span[2]')
    order_id = goods_element.find_element(By.XPATH, './div/table/tbody[1]/tr/td[1]/span/span[3]')
    business_name = goods_element.find_element(By.XPATH, './div/table/tbody[1]/tr//td[2]/span/a')
    goods_name = goods_element.find_element(By.XPATH, './div/table/tbody[2]/tr[1]/td[1]/div/div[2]/p[1]/a[1]/span[2]')
    goods_link = goods_element.find_element(By.XPATH, './div/table/tbody[2]/tr[1]/td[1]/div/div[2]/p[1]/a[1]')
    print(
        f'时间:{order_time.text},   订单:{order_id.text}, 店铺:{business_name.text},    商品:{goods_name.text},   链接:{goods_link.get_attribute('href')}')

    #   这里要修改判断，日期是指定时间的才处理
    if index < 5:
        msg = []
        # 点击旺旺铺子
        wangwang_xpath = f'.//*[@id="webww{index + 1}"]/span/a'
        wangwang = driver.find_element(By.XPATH, wangwang_xpath).click()
        sleep(2)
        # 切换到浏览器窗口的最后一个页面
        driver.switch_to.window(driver.window_handles[-1])
        sleep(2)
        driver.switch_to.frame(0)
        msg_lines = driver.find_elements(By.XPATH,
                                         '//*[@id="ice-container"]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div[@class="message-item-line"]')
        for line in msg_lines:
            # 这里要匹配消息内容 包含 提取码 网盘地址 才处理
            msg.append(line.text.replace('\n', ' '))

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        sleep(1)
    else:
        msg = []

    # 将数据添加到列表
    data.append({
        '时间': order_time.text,
        '订单': order_id.text,
        '店铺': business_name.text,
        '商品': goods_name.text,
        '链接': goods_link.get_attribute('href'),
        '聊天记录': msg
    })

# 将列表转换为数据框
df = pd.DataFrame(data)

# 将数据框保存到 Excel 文件
df.to_excel('taobao_order_info.xlsx', index=False)

sleep(5)
driver.quit()
