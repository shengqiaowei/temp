# -*- coding:utf-8 -*-
#author: xiaxiang time:2019-10-10
from bs4 import BeautifulSoup

def parse_data():
    with open('test.html','r',encoding='gbk') as r:
        html = r.read()

    bs = BeautifulSoup(html,'html.parser')
    temp = bs.select('script')[7]
    print(temp)

if __name__=='__main__':
    parse_data()