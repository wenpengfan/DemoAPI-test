# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from domo.test_case.page_obj.base import Page


class confaction(Page):
    '''
    配置界面
    '''
    url = '/domo/actionconf.php?ddreset=1'
    configuration_loc = (By.XPATH, '//*[@id="PathConfig"]/a')
    action_loc = (By.XPATH, '//*[@id="sub_config"]/li[5]/a')
    entry_loc = (By.XPATH, '//*[@class="list-table"]/tbody/tr/td[2]/a')
    name_loc = (By.XPATH, '//*[@id="name"]')
    cancel_loc = (By.ID, "cancel")

    # 点击配置
    def click_configuration(self):
        self.find_element(*self.configuration_loc).click()

    # 点击动作
    def click_action(self):
        self.find_element(*self.action_loc).click()

    # 点击指定动作名称
    def click_entry(self):
        self.find_element(*self.entry_loc).click()

    # 修改动作内指定的内容
    def add_name(self, hotel_name):
        self.find_element(*self.name_loc).clear()
        self.find_element(*self.name_loc).send_keys(hotel_name)

    # 点击取消按钮
    def cancel(self):
        self.find_element(*self.cancel_loc).click()

    # 统一入口
    def Unified_landing_entrance(self, action_name='Auto discovery. Linux servers'):
        self.open()
        self.click_configuration()
        self.click_action()
        self.click_entry()
        self.add_name(action_name)
        self.cancel()
