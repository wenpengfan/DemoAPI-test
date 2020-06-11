# -*- coding:utf-8 -*-
import unittest
from domo.test_case.models import myunit, screenshots
from domo.test_case.page_obj.login.loginPage import login
from domo.test_case.page_obj.monitoring.monitoring_problemPage import problem


class actionTest(myunit.MyTest):
    '''
    测试动作添加
    '''
    def user_login_verify(self):
        login(self.driver).user_login()

    def test_mproblem(self):
        self.user_login_verify()
        ho = problem(self.driver)
        ho.Unified_landing_entrance()
        # screenshots.insert_img(self.driver, "problem_action.png")


if __name__ == '__main__':
    unittest.main()