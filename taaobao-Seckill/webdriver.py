# author: xiaxiang   time:2019/9/25
#京东使用cookies绕过登录

from selenium import webdriver
import json
import time
import os
import requests

driver = webdriver.Chrome()
driver.maximize_window()

def get_url_with_cookies():

    #获取cookies信息
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path+'/cookies/'
    cookies_file = file_path+'jd.cookies'

    jd_cookies_file = open(cookies_file,'r')
    jd_cookies_str = jd_cookies_file.readline()

    #加载cookies
    jd_cookies_dict = json.loads(jd_cookies_str)

    #先访问首页 删除已有的cookies
    driver.get('https://www.jd.com')
    driver.delete_all_cookies()

    #将cookies信息添加到driver中
    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)

    #检查是否登录成功
    driver.get('https://order.jd.com/center/list.action')
    time.sleep(2)

def save_cookies(driver):
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + '/cookies/'

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    #从driver中获取cookies
    cookies = driver.get_cookies()

    with open(file_path+'jd.cookies','w') as f:
        json.dump(cookies,f)

    print(cookies)


def login():
    driver.get('https://passport.jd.com/uc/login?ltype=logout')
    driver.find_element_by_link_text('账户登录').click()
    time.sleep(1)
    driver.find_element_by_css_selector('input[id="loginname"]').send_keys('13732327438')
    driver.find_element_by_css_selector('input[type="password"]').send_keys('sqw.5021')
    driver.find_element_by_id('loginsubmit').click()
    time.sleep(1)

    save_cookies(driver)

if __name__=='__main__':
    try:
         login()
        #get_url_with_cookies()
    except Exception as e:
        raise e
    finally:
        driver.quit()