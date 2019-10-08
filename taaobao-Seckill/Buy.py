# author: xiaxiang   time:2019/9/21

import requests
import pprint


class Buy:
    def __init__(self):
        pass

    def logging(self,username,password):
        #
        home = requests.get('https://www.nike.com/cn/zh_cn/c/jordan')

# def shopping():
#
#     print(home)
#
#     shopping_cart = requests.get('https://www.nike.com/cn/cart')
#     print(shopping_cart)
#
#
#
# shopping()