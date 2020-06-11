# -*- coding:utf-8 -*-
import unittest
from domo.test_case.models import myunit, screenshots
from domo.test_case.page_obj.login.loginPage import login
from domo.test_case.page_obj.config.confactionPage import confaction


class actionTest(myunit.MyTest):
    '''
    测试动作添加
    '''

    def user_login_verify(self):
        login(self.driver).user_login()

    def test_confaction(self):
        self.user_login_verify()
        hotel_name = "Report problems to Zabbix administratorss"
        ho = confaction(self.driver)
        ho.Unified_landing_entrance(hotel_name)
        # screenshots.insert_img(self.driver, "action.png")


if __name__ == '__main__':
    unittest.main()