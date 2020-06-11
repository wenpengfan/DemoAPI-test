# -*- coding:utf-8 -*-
"""
思路：创建登录页面对象，对用户登录页面上的用户名/密码输入框、登录按钮和
提示信息等元素的定位进行封装。
"""
from selenium.webdriver.common.by import By
from domo.test_case.page_obj.base import Page


class login(Page):
    '''
    用户登录界面
    '''
    url = "/domo/index.php"
    # 登录用户名的定位
    login_username_loc = (By.ID, 'name')
    # 登录密码的定位
    login_password_loc = (By.ID, 'password')
    # 登录按钮的定位
    login_button_loc = (By.ID, 'enter')

    # 登录错误提示的定位
    login_error_loc = (By.CLASS_NAME, 'red')

    # 登录成功用户名信息
    # login_user_success_loc = (By.XPATH, 'html/body/div[3]/div[2]/ul/li[1]/a/strong')

    # 登录用户名
    def login_username(self, username):
        # self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        # self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 统一登录入口
    def user_login(self, username="admin", password="123456!"):
        # 获取用户名和页面登录
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        # time.sleep(5)

    # # 登陆告警提示信息
    # def login_alert_hint(self):
    #     return self.driver.switch_to.alert().text

    # 登录错误提示信息
    def login_error_hint(self):
        return self.find_element(*self.login_error_loc).text

    # 登录成功用户名信息
    def login_user_success(self, username):
        username = username.strip('您好：')
        return username

    # # 登录成功用户名信息
    # def login_user_success(self):
    #     # return self.find_element(*self.login_user_success_loc).text
    #     username = self.find_element(*self.login_user_success_loc).text
    #     username = username.strip('您好：')
    #     return username
