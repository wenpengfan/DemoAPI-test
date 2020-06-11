# -*- coding:utf-8 -*-
import unittest
from domo.test_case.models.driver import browser
import warnings


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        cls.driver = browser()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get_cookies()
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
