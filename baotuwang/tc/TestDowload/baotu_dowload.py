# -*- coding:utf-8 -*-
#author: xiaxiang time:2019-09-29

from selenium import webdriver
import time
from dowload_cfg import *

class BaotuDowload:


    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def login(self):
        self.driver.get('https://ibaotu.com/')
        print('请先手动登录')
        time.sleep(15)

    def test_dowload(self,id):
        for id in dowload_id:
            print(id)
            self.driver.get('https://ibaotu.com/?m=download&id={}'.format(id))
            # 下载确认页点击下载
            time.sleep(0.5)
            self.driver.refresh()
            self.driver.find_element_by_css_selector('#downvip >span').click()
            time.sleep(2)

if __name__=='__main__':
    try:
        bd = BaotuDowload()
        bd.login()
        bd.test_dowload(dowload_id)
    except Exception as e:
        raise e
