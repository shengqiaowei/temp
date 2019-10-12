# -*- coding:utf-8 -*-
#author: xiaxiang time:2019-10-12

# coding=utf-8
from selenium import webdriver
import time


class zxc:

    username = "dev"
    password = "YulinKey"
    Code = "code"
    VerificationCode = ''

    # 打开浏览器
    def setUp(self):
        self.driver = webdriver.Chrome()

    # 登陆操作
    def test_login(self):
        # 打开url
        self.driver.get("http://121.196.238.132:8099/")
        time.sleep(1)

        # 执行登陆操作
        # 用户名的定位
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(self.username)
        # 密码的定位
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(self.password)
        # 验证码的定位
        self.driver.find_element_by_id("Verification Code").clear()
        self.driver.find_element_by_id("Verification Code").send_keys(self.VerificationCode)
        # 点击登陆
        self.driver.find_element_by_css_selector(".btn.btn-success.btn-block").click()
        time.sleep(1)

        # 登陆成功断言
        login_name = self.driver.find_element_by_xpath('html/body/div[3]/div[2]/ul/li[1]/a/strong').text
        login_name = login_name.strip('您好：')
        assert login_name == self.username

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    test = zxc()
    try:
        test.setUp()
        test.test_login()
    except Exception as e:
        raise e
    finally:
        test.tearDown()

