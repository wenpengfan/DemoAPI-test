#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Fan'

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 配置文件
TEST_CONFIG = os.path.join(BASE_DIR + "/" + "config/config.ini")

# 测试用例报告
TEST_REPORT = os.path.join(BASE_DIR + "/" + "report")
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR + "/" + "test_case/all_sta")
# 控制测试用例文件
TESTCASE_list = os.path.join(BASE_DIR + "/" + "config/caselist.txt")
# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR,"config","DemoAPITestCase.xlsx")
# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR,"report","excelReport","DemoAPITestCase.xlsx")