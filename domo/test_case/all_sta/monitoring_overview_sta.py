# -*- coding:utf-8 -*-
import unittest
from domo.test_case.models import myunit, screenshots
from domo.test_case.page_obj.login.loginPage import login
from domo.test_case.page_obj.monitoring.monitoring_overviewPage import overview


class actionTest(myunit.MyTest):
    '''
    测试动作添加
    '''
    # def user_login_verify(self):
    #      login(self.driver).user_login()

    def test_action(self):
        # self.user_login_verify()
        po = login(self.driver)
        po.user_login()
        ho = overview(self.driver)
        ho.Unified_landing_entrance()
        self.assertEqual(ho.click_validation(), "5130-7")
        # screenshots.insert_img(self.driver, "validation.png")


if __name__ == '__main__':
    unittest.main()