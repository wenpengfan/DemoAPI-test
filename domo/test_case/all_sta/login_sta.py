# -*- coding:utf-8 -*-
import unittest
from domo.test_case.models import myunit, screenshots
from domo.test_case.page_obj.login.loginPage import login


class loginTest(myunit.MyTest):
    '''
    测试用户登录
    '''

    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        '''用户名、密码为空登录'''
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(), 'Login name or password is incorrect.')
        screenshots.insert_img(self.driver, "user_pawd_empty.png")

    def test_login2(self):
        '''用户名正确，密码为空登录验证'''
        self.user_login_verify(username="admin", password="")
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(), "Login name or password is incorrect.")
        # screenshots.insert_img(self.driver, "pawd_empty.png")

    def test_login3(self):
        '''用户名为空，密码正确'''
        self.user_login_verify(password="111111!")
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(), "Login name or password is incorrect.")
        # screenshots.insert_img(self.driver, "user_empty.png")

    def test_login4(self):
        '''用户名和密码不匹配'''
        self.user_login_verify(username="admin", password="2sdfd")
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(), "Login name or password is incorrect.")
        # screenshots.insert_img(self.driver, "user_pass_error.png")

    def test_login5(self):
        '''用户名、密码正确'''
        self.user_login_verify(username="admin", password="111111!")
        po = login(self.driver)
        self.assertEqual(po.login_user_success(username="admin"), "admin")
        # screenshots.insert_img(self.driver, "user_pwd_true.png")


if __name__ == '__main__':
    unittest.main()
