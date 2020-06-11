# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from domo.test_case.page_obj.base import Page


class problem(Page):
    '''
    配置界面
    '''
    url = '/domo/domo.php?action=dashboard.view&ddreset=1'
    problem_loc = (By.XPATH,'//*[@id="sub_view"]/li[2]/a')
    export_csv_loc = (By.XPATH,"//button[@type='button']")

    # 点击问题按钮
    def click_problem(self):
        self.find_element(*self.problem_loc).click()

    # 点击导出csv
    def click_export_csv(self):
        self.find_element(*self.export_csv_loc).click()

    # 统一入口
    def Unified_landing_entrance(self):
        self.open()
        self.click_problem()
        self.click_export_csv()
