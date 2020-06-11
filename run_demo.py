#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os, sys

sys.path.append(os.path.dirname(__file__))
from domo.PathConfig import setting
import unittest, time
from HTMLTestRunnerCN import HTMLTestRunner
from domo.lib.sendmail import send_mail
from domo.lib.newReport import new_report
# from db_fixture import test_data
from domo.package.HTMLTestRunner import HTMLTestRunner

path = os.path.split(os.path.realpath(__file__))[0]
# caseListFile = os.path.join(path, "config/caselist.txt")  # 配置执行哪些测试文件的配置文件路径
# 配置执行哪些测试文件的配置文件路径
caseListFile = setting.TESTCASE_list
# 真正的测试断言文件路径
caseFile = os.path.join(path, "domo/test_case/all_sta")
caseList = []


def set_case_list():
    """
    读取caselist.txt文件中的用例名称，并添加到caselist元素组
    :return:
    """
    fb = open(caseListFile)
    for value in fb.readlines():
        data = str(value)
        # 如果data非空且不以#开头
        if data != '' and not data.startswith("#"):
            # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
            caseList.append(data.replace("\n", ""))
    fb.close()


def add_case():
    """
    :return:
    """
    # 通过set_case_list()拿到caselist元素组
    set_case_list()
    test_suite = unittest.TestSuite()
    suite_module = []
    # 从caselist元素组中循环取出case
    for case in caseList:
        # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
        case_name = case.split("/")[-1]
        # 打印出取出来的名称
        # print(case_name + ".py")
        # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
        discover = unittest.defaultTestLoader.discover(caseFile, pattern=case_name + '.py', top_level_dir=None)
        # 将discover存入suite_module元素组
        suite_module.append(discover)
        # print('suite_module:' + str(suite_module))
    # 判断suite_module元素组是否存在元素
    if len(suite_module) > 0:
        # 如果存在，循环取出元素组内容，命名为suite
        for suite in suite_module:
            # 从discover中取出test_name，使用addTest添加到测试集
            for test_name in suite:
                test_suite.addTest(test_name)
    else:
        print('else:')
        return None
    # 返回测试集
    return test_suite  # 返回测试集


def run_case(all_case, result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""

    # 初始化接口测试数据
    # test_data.init_data()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = result_path + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='发布会系统接口自动化测试报告',
                            description='环境：windows 7 浏览器：chrome',
                            tester='Fan')
    runner.run(all_case)
    fp.close()
    # 调用模块生成最新的报告
    report = new_report(setting.TEST_REPORT)
    # 调用发送邮件模块
    send_mail(report)


if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
