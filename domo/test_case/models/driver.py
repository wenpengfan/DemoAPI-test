# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# 启动浏览器

def browser():
    # driver = webdriver.Remote(command_executor="http://192.168.182.97:32768/wd/hub",
    #                           desired_capabilities=DesiredCapabilities.CHROME)
    option = Options()
    option.add_argument('disable-gpu')
    option.add_argument('no-sandbox')
    option.add_argument('disable-dev-shm-usage')
    option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    # driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get("http://zabbix.hz.com/zabbix/index.php")
    dr.quit()