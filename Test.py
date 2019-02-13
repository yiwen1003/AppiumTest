# coding=utf-8

from appium import webdriver
import time
import unittest
# # import os
# import HTMLTestRunner


class Tests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'ios'  # 设备系统
        desired_caps['platformVersion'] = '12.0.1'  # 设备系统版本
        desired_caps['deviceName'] = 'iphone XR'  # 设备名称
        desired_caps['bundleId'] = 'Y.TestProduct'  # 测试app包名
        desired_caps['udid'] = 'B7416A87-6C4A-476E-BF03-4EAD8A272304'
        desired_caps['automationName'] = 'XCUITest'  # 测试appActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 启动app
        # {
        #     "platformName": "ios",
        #     "deviceName": "iphone XR",
        #     "platformVersion": "12",
        #     "bundleId": "Y.TestProduct",
        #     "udid": "B7416A87-6C4A-476E-BF03-4EAD8A272304",
        #     "automationName": "XCUITest"
        # }

    def testCase1_findElements(self):
        driver = self.driver
        textWorld = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="world"]').text
        textaaa = driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="TestProduct"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTextField')
        time.sleep(2)
        assert textWorld=="world", print('no word of world')

    def testCase2_ButtonChange(self):
        driver = self.driver

        # Click the button to change the content of the label and the text
        button = driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Button"]')
        button.click()
        time.sleep(2)
        textWorld = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="world"]').text
        textaaa = driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="TestProduct"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTextField')

        # 添加断言，若label和text没有被改变或正确地被改变，则打印错误信息try:
        assert  textWorld == 'changed label', print('The label has not been changed by button')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Tests('testCase1_findElements'))
    suite.addTest(Tests('testCase2_ButtonChange'))
    unittest.TextTestRunner(verbosity=2).run(suite)
    # filename = 'C:\\Temp\\app.html'
    # fb = file(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='YiwenTestsReports', description='AppiumTestsReports_Yiwen')
    # runner.run(suite)
    # fb.close()