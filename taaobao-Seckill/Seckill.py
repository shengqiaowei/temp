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
            print('请尽快扫码登录')
            time.sleep(10)
            # 打开购物车页面
            self.wd.get('https://cart.taobao.com/cart.htm')
        time.sleep(2)
        now = datetime.datetime.now()
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

    #选中商品
    def picking(self,ShoppingNumber,times):
        is_buyed = False
        #勾选商品
        self.wd.find_element_by_css_selector("label[for={}]".format(ShoppingNumber)).click()
        time.sleep(0.5)

        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print('现在的时间:',now)
            #对比时间，时间到就结算
            if now>times:
                #结算
                try:
                    #点击结算
                    Settlement = self.wd.find_element_by_css_selector('#J_Go')
                    if Settlement:
                        Settlement.click()
                        print('结算成功,准备提交订单')
                except:
                    pass
                #提交订单
                while True:
                    #提交订单
                    try:
                        #self.wd.refresh()#刷新当前页面
                        order = self.wd.find_element_by_css_selector('.go-btn')
                        if order and is_buyed == False:
                            order.click()
                            print('抢购成功，请尽快付款')
                            now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                            print("抢购成功时间：%s" % now1)
                    except:
                        print('再次尝试提交订单')
                time.sleep(0.005)

if __name__=='__main__':
    sk = Seckill()
    sk.open_browser()
    sk.login()
    sk.picking('J_CheckBox_1513805857037', '2019-09-19 18:37:00.000000')
    sk.close_browser()

