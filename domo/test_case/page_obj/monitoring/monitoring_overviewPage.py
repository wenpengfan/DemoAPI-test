# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from domo.test_case.page_obj.base import Page
from selenium.webdriver.support.select import Select
from time import sleep


class overview(Page):
    '''
    配置界面
    '''
    url = '/domo/domo.php?action=dashboard.view'
    overview_loc = (By.XPATH, '//*[@id="sub_view"]/li[3]/a')
    selectgroup_loc = (By.NAME, "groupid")
    type_loc = (By.ID, "type")
    host_location_loc = (By.ID, "view_style")
    confirm_loc = (By.NAME, "filter_set")
    # 验证页面是否加载
    validation_loc = (By.LINK_TEXT, "5130-7")

    # 点击概览按钮
    def click_overview(self):
        self.find_element(*self.overview_loc).click()

    # 点击选择群组选择SWITCH
    def click_overview_select_group(self):
        self.find_element(*self.selectgroup_loc).click()

    # 选择SWITCH群组
    def click_select_group(self):
        Select(self.find_element(*self.selectgroup_loc)).select_by_visible_text("SWITCH")

    # 选择类型为数据
    def click_type(self):
        Select(self.find_element(*self.type_loc)).select_by_visible_text("数据")

    # 选择主机位置
    def click_host(self):
        Select(self.find_element(*self.host_location_loc)).select_by_visible_text("左侧")

    # 点击应用
    def click_confirm(self):
        self.find_element(*self.confirm_loc).click()

    # click_validation
    def click_validation(self):
        return self.find_element(*self.validation_loc).text

    # 统一入口
    def Unified_landing_entrance(self):
        self.open()
        self.click_overview()
        self.click_overview_select_group()
        self.click_select_group()
        self.click_type()
        self.click_host()
        self.click_confirm()
