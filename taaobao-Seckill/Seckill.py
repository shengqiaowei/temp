# -*- coding:utf-8 -*-
#author: xiaxiang time:2019-09-16

from selenium import webdriver
import time
import datetime


class Seckill:

    def open_browser(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)

    def close_browser(self):
        self.wd.quit()

    #登录淘宝
    def login(self):
        self.wd.get('https://www.taobao.com/')
        self.wd.maximize_window()
        time.sleep(1)
        if self.wd.find_element_by_link_text('亲，请登录'):
            self.wd.find_element_by_link_text('亲，请登录').click()
            print(f'请尽快扫码登录')
            # self.wd.find_element_by_css_selector('#TPL_username_1').send_keys('盛侨威')
            # time.sleep(3)
            # self.wd.find_element_by_css_selector('#TPL_password_1').send_keys('qiao.0706')
            # time.sleep(3)
            # self.wd.find_element_by_id('J_SubmitStatic').click()


    #选中商品
    def picking(self,ShoppingNumber,times):
        #打开购物车页面
        self.wd.get('https://cart.taobao.com/cart.htm')
        time.sleep(2)
        #勾选商品
        self.wd.find_element_by_css_selector("label[for={}]".format(ShoppingNumber)).click()
        time.sleep(0.5)

        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print(now)
            #对比时间，时间到就结算
            if now>times:
                #结算
                while True:
                    try:
                        #点击结算
                        Settlement = self.wd.find_element_by_css_selector('#J_Go')
                        if Settlement:
                            Settlement.click()
                            print('结算成功,准备提交订单')
                            time.sleep(1)
                            break
                    except:
                        print('再次尝试结算')
                #提交订单
                while True:
                    #提交订单
                    try:
                        self.wd.refresh()#刷新当前页面
                        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                        order = self.wd.find_element_by_css_selector('.go-btn')
                        if order:
                            order.click()
                            print('抢购成功，请尽快付款')
                            break
                    except:
                        print('再次尝试提交订单')
                time.sleep(0.01)

try:

    sk = Seckill()
    sk.open_browser()
    sk.login()
    sk.picking('J_CheckBox_1506156096178','2019-09-17 18:10')

except Exception as e:
    print(e)
finally:
    sk.close_browser()

