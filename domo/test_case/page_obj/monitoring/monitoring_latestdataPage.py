# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from domo.test_case.page_obj.base import Page


class latest(Page):
    url = "/domo/latest.php?ddreset=1"
    # 最新数据按钮
    latest_loc = (By.LINK_TEXT, u"最新数据")
    # 主机群组选择按钮
    hostGroupchoose_loc = (By.XPATH, "(//button[@type='button'])[2]")
    # 选择DELL
    hostGroupdetails_loc = (By.ID, "spanid15")
    # 点击主机选择按钮
    hostchoose_loc = (By.XPATH, "(//button[@type='button'])[3]")
    # 选择主机内群组选择
    host_group_loc = (By.NAME, "groupid")
    # 具体主机
    host_loc = (By.ID, "spanid10286")
    # 应用按钮
    confirm_loc = (By.NAME, "filter_set")
    # 验证页面元素
    validation_loc = (By.LINK_TEXT, "10.30.30.12")

    def click_latest(self):
        self.find_element(*self.latest_loc).click()

    def click_hostGroupchoose(self):
        self.find_element(*self.hostGroupchoose_loc).click()

    def click_hostGroupdetails(self):
        self.find_element(*self.hostGroupdetails_loc).click()

    def click_hostchoose(self):
        self.find_element(*self.hostchoose_loc).click()

    def click_host_group(self):
        Select(self.find_element(*self.host_group_loc)).select_by_visible_text("DELL")

    def click_host(self):
        self.find_element(*self.host_loc).click()

    def click_confirm(self):
        self.find_element(*self.confirm_loc).click()

    def click_validation(self):
        return self.find_element(*self.validation_loc).text

    def Unified_landing_entrance(self):
        self.open()
        self.click_latest()
        self.click_hostGroupchoose()
        self.click_hostGroupdetails()
        self.click_hostchoose()
        self.click_host_group()
        self.click_host()
        self.click_confirm()
