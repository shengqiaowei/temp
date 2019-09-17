# -*- coding:utf-8 -*-
#author: xiaxiang time:2019-09-16

from selenium import webdriver
import time
import datetime


class Seckill:

    def open_browser(self):
        self.wd = webdriver.Chrome()
        #self.wd.implicitly_wait(10)

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
            time.sleep(5)
            # self.wd.find_element_by_css_selector('#TPL_username_1').send_keys('盛侨威')
            # time.sleep(3)
            # self.wd.find_element_by_css_selector('#TPL_password_1').send_keys('qiao.0706')
            # time.sleep(3)
            # self.wd.find_element_by_id('J_SubmitStatic').click()


    #选中商品
    def picking(self,times):
        # #打开购物车页面
        # self.wd.get('https://cart.taobao.com/cart.htm')
        # time.sleep(2)
        # #勾选商品
        # self.wd.find_element_by_css_selector("label[for={}]".format(ShoppingNumber)).click()
        # time.sleep(0.5)

        #进入牛排详情页
        self.wd.get('https://detail.tmall.com/item.htm?id=582302039775&spm=a21bz.7725273.1998564503.1.c8c33db8Tz0MAp&umpChannel=qianggou&u_channel=qianggou')
        time.sleep(2)

        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print(now)
            #对比时间，时间到就结算
            if now>times:
                while True:
                    # 点击立即购买
                    try:
                        buy = self.wd.find_element_by_id('J_LinkBuy')
                        if buy:
                            print('购买成功')
                            buy.click()
                            #time.sleep(1)
                            break
                    except:
                        print('再次进行购买')

                # #结算
                # while True:
                #     try:
                #         #点击结算
                #         Settlement = self.wd.find_element_by_css_selector('#J_Go')
                #         if Settlement:
                #             Settlement.click()
                #             print('结算成功,准备提交订单')
                #             time.sleep(1)
                #             break
                #     except:
                #         print('再次尝试结算')
                #提交订单
                while True:
                    #提交订单
                    try:
                        #self.wd.refresh()#刷新当前页面
                        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                        order = self.wd.find_element_by_css_selector('.go-btn')
                        if order:
                            print('抢购成功，请尽快付款')
                            order.click()
                            break
                    except:
                        print('再次尝试提交订单')
                time.sleep(0.01)

try:

    sk = Seckill()
    sk.open_browser()
    sk.login()
    sk.picking('2019-09-18 00:00')

except Exception as e:
    print(e)
finally:
    sk.close_browser()

