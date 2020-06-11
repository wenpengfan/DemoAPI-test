# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    '''
    页面基础类，用于所有页面的继承
    '''

    base_url = "http://zabbix.hz.com"

    def __init__(self, selenium_driver, base_url=base_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url_ = self.base_url + url
        print(url_)
        self.driver.get(url_)
        # time.sleep(2)
        assert self.driver.current_url == url_, 'Did not land on %s' % url_

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保所有元素是可见的
            # 注意：以下入参为元组的元素，需要加*。python存在这种特性，就是将入参放在元组里。
            #(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc)).is_displayed()
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def script(self, src):
        return self.driver.execute_script(src)

    def swtich_frame(self, loc):
        return self.driver.swith_to_frame(loc)

    def attribute(self, loc):
        return self.driver.get_attribute(loc)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            # getattr相当于self.loc
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except ArithmeticError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))