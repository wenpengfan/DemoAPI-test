# -*- coding:utf-8 -*-
from selenium import webdriver
import os

# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('test_case')[0]
    file_path = base + "image/" + file_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://zabbix.hz.com/zabbix/index.php")
    insert_img(driver, 'login.png')
    driver.quit()
