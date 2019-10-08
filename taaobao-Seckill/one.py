
import re
import os
import json
import time
import requests
from cfg import *
import pprint


s = requests.Session()
# cookies序列化文件
COOKIES_FILE_PATH = 'taobao_login_cookies.txt'


class UsernameLogin:

    def __init__(self, username, ua, TPL_password2):
        """
        账号登录对象
        :param username: 用户名
        :param ua: 淘宝的ua参数
        :param TPL_password2: 加密后的密码
        """
        # 检测是否需要验证码的URL
        self.user_check_url = 'https://login.taobao.com/member/request_nick_check.do?_input_charset=utf-8'
        # 验证淘宝用户名密码URL
        self.verify_password_url = "https://login.taobao.com/member/login.jhtml"
        # 访问st码URL
        self.vst_url = 'https://login.taobao.com/member/vst.htm?st={}'
        # 淘宝个人 主页
        self.my_taobao_url = 'http://i.taobao.com/my_taobao.htm'

        # 淘宝用户名
        self.username = username
        # 淘宝关键参数，包含用户浏览器等一些信息，很多地方会使用，从浏览器或抓包工具中复制，可重复使用
        self.ua = ua
        # 加密后的密码，从浏览器或抓包工具中复制，可重复使用
        self.TPL_password2 = TPL_password2

        # 请求超时时间
        self.timeout = 3

    def _user_check(self):
        """
        检测账号是否需要验证码
        :return:
        """
        data = {
            'username': self.username,
            'ua': self.ua
        }
        try:
            response = s.post(self.user_check_url, data=data, timeout=self.timeout)
            response.raise_for_status()
        except Exception as e:
            print('检测是否需要验证码请求失败，原因：')
            raise e
        needcode = response.json()['needcode']
        print('是否需要滑块验证：{}'.format(needcode))
        return needcode

    def _verify_password(self):
        """
        验证用户名密码，并获取st码申请URL
        :return: 验证成功返回st码申请地址
        """
        verify_password_headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': 'https://login.taobao.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F',
        }
        # 登录taobao.com提交的数据，如果登录失败，可以从浏览器复制你的form data
        verify_password_data = {
            'TPL_username': self.username,
            'ncoToken': '80b1f5bfffb4233cd5edf4522dfed1b3a7474b50',
            'slideCodeShow': 'false',
            'useMobile': 'false',
            'lang': 'zh_CN',
            'loginsite': 0,
            'newlogin': 0,
            'TPL_redirect_url': 'https://www.taobao.com/',
            'from': 'tb',
            'fc': 'default',
            'style': 'default',
            'keyLogin': 'false',
            'qrLogin': 'true',
            'newMini': 'false',
            'newMini2': 'false',
            'loginType': '3',
            'gvfdcname': '10',
            'gvfdcre': '68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D613231626F2E323031372E3735343839343433372E372E3561663931316439314A49336A4326663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246',
            'TPL_password_2': self.TPL_password2,
            'loginASR': '1',
            'loginASRSuc': '1',
            'oslanguage': 'zh-CN',
            'sr': '1440*900',
            'osVer': 'macos|10.141',
            'naviVer': 'chrome|77.038659',
            'osACN': 'Mozilla',
            'osAV': '5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'osPF': 'MacIntel',
            'appkey': '00000000',
            'mobileLoginLink': 'https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true',
            'showAssistantLink': 'true',
            'um_token': 'T407AB99E89DCC473074CB3AC7B65B94942F933C31EA6B872920E7A38CE',
            'ua': self.ua
        }
        try:
            response = s.post(self.verify_password_url, headers=verify_password_headers, data=verify_password_data,
                              timeout=self.timeout)
            response.raise_for_status()
            # 从返回的页面中提取申请st码地址
        except Exception as e:
            print('验证用户名和密码请求失败，原因：')
            raise e
        # 提取申请st码url
        apply_st_url_match = re.search(r'<script src="(.*?)"></script>', response.text)
        # 存在则返回
        if apply_st_url_match:
            print('验证用户名密码成功，st码申请地址：{}'.format(apply_st_url_match.group(1)))
            return apply_st_url_match.group(1)
        else:
            raise RuntimeError('用户名密码验证失败！response：{}'.format(response.text))

    def _apply_st(self):
        """
        申请st码
        :return: st码
        """
        apply_st_url = self._verify_password()
        try:
            response = s.get(apply_st_url)
            response.raise_for_status()
        except Exception as e:
            print('申请st码请求失败，原因：')
            raise e
        st_match = re.search(r'"data":{"st":"(.*?)"}', response.text)
        if st_match:
            print('获取st码成功，st码：{}'.format(st_match.group(1)))
            return st_match.group(1)
        else:
            raise RuntimeError('获取st码失败！response：{}'.format(response.text))

    def login(self):
        """
        使用st码登录
        :return:
        """
        # 加载cookies文件
        if self._load_cookies():
            return True
        # 判断是否需要滑块验证
        self._user_check()
        st = self._apply_st()
        headers = {
            'Host': 'login.taobao.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        try:
            response = s.get(self.vst_url.format(st), headers=headers)
            response.raise_for_status()
        except Exception as e:
            print('st码登录请求，原因：')
            raise e
        # 登录成功，提取跳转淘宝用户主页url
        my_taobao_match = re.search(r'top.location.href = "(.*?)"', response.text)
        if my_taobao_match:
            print('登录淘宝成功，跳转链接：{}'.format(my_taobao_match.group(1)))
            self._serialization_cookies()
            return True
        else:
            raise RuntimeError('登录失败！response：{}'.format(response.text))

    def _load_cookies(self):
        # 1、判断cookies序列化文件是否存在
        if not os.path.exists(COOKIES_FILE_PATH):
            return False
        # 2、加载cookies
        s.cookies = self._deserialization_cookies()
        # 3、判断cookies是否过期
        try:
            self.get_taobao_nick_name()
            #self.shopping_cart()
        except Exception as e:
            os.remove(COOKIES_FILE_PATH)
            print('cookies过期，删除cookies文件！')
            return False
        print('加载淘宝登录cookies成功!!!')
        return True

    def _serialization_cookies(self):
        """
        序列化cookies
        :return:
        """
        cookies_dict = requests.utils.dict_from_cookiejar(s.cookies)
        with open(COOKIES_FILE_PATH, 'w+', encoding='utf-8') as file:
            json.dump(cookies_dict, file)
            print('保存cookies文件成功！')

    def _deserialization_cookies(self):
        """
        反序列化cookies
        :return:
        """
        with open(COOKIES_FILE_PATH, 'r+', encoding='utf-8') as file:
            cookies_dict = json.load(file)
            cookies = requests.utils.cookiejar_from_dict(cookies_dict)
            return cookies

    def get_taobao_nick_name(self):
        """
        获取淘宝昵称
        :return: 淘宝昵称
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        try:
            response = s.get(self.my_taobao_url, headers=headers)
            response.raise_for_status()
        except Exception as e:
            print('获取淘宝主页请求失败！原因：')
            raise e
        # 提取淘宝昵称
        nick_name_match = re.search(r'<input id="mtb-nickname" type="hidden" value="(.*?)"/>', response.text)
        if nick_name_match:
            print('登录淘宝成功，你的用户名是：{}'.format(nick_name_match.group(1)))
            return nick_name_match.group(1)
        else:
            raise RuntimeError('获取淘宝昵称失败！response：{}'.format(response.text))

    #全选商品
    def check_list(self):
        try:
            response = s.post(check_list_url,data=check_list_payload,headers=check_list_headers)
            resDict = response.json()
            resMessage = resDict['success']
            print('商品勾选成功:', resMessage)
        except Exception as e:
            print('全选失败,原因:')
            raise e

    #结算
    def place_order(self):
        try:
            response = s.post(place_order_url,data=place_order_payload,headers=place_order_headers,allow_redirects=True)
            response.raise_for_status()
            print(response)
            print(response.text)
        except Exception as e:
            print('结算失败，原因：')
            raise e

    #提交订单
    def order(self):
        try:
            response = s.post(order_url,data=order_payload,headers=order_headers,allow_redirects=True)
            response.raise_for_status()
            print(response)
            print(response.text)
        except Exception as e:
            print('提交订单失败，原因：')
            raise e


if __name__ == '__main__':
    # 淘宝用户名
    username = 'shengqiaowei@126.com'
    # 淘宝重要参数，从浏览器或抓包工具中复制，可重复使用
    ua = '120#bX1bS7uVqYD52qNyFvYfcMxfbco/dByPYVvSnCboZ16+xhW27VrTM7n0+8Xen48q5g8EU6TAlP+yACIh64ZX5lm9Zse/tACYp93lSqXHSEgQ7Uck6/ycaSVjSziBfZ11mwhp3SqV0MWExjbWquSxneD5CsnLmTEpDOwJ72AvIEeW4kaBNWH3nDig4alNTc5s75qBaV438I05kvgo6kcV3J286xwgrrnUWW4SbZqYZvxeFAYCbOLyknLFlAPslqaHHtsogyZr84g/bb51EQfPNpT9bbvp7aMPZXIYb5bmNtl/P7bx+jQ21Xq/bbbtke/mba/YT5+PNcID3Ybb1FBPEPc/bbSfk5MPHiltb5HpmQePPbbb7v0PyWl/bbYt7aPyGkeL9Np5Q52D4bxYg6ikMx38v60rY8s5yNJz308KoyuXg0r77ORF/3SRpNkgilemAApfQbqthqEHicQdwCxIQrk3QCwQT0yYkIii9KcvBojKhDfqRZpPBVvwbQqA3Jgm/AiE92lE5/ztnFyJPLEclAeKBab4hOLZCWXkh6VPaD7F0Mt0wZ0lU4ZCGz9bkASIlL0ImqpyF9W9CIehf1yOuDEZov7FX+GaufeSLMAfacls2M15XMB+YuxRa1mLlWJfAcp1l0IkTR4pXDQTlAfMMWHDD15w0y5d8656u60IYD0oF0EHRdO4OtWp8TzBp0lL0gJMjsFr4TKLdv+zChIKS7KZiqGr9yQvEMdT/AKgMj0IwGe5lCY1K+TG7dH8PN2gXNXjyQe4NjXOUhhPV3gYAn2Sut5XL6w1OWO8a0PwhYpLITmlQSscAu+ufQsheYEER4SA7RVqIEInf0UBTa/3NC9S3iG8KHFN9THMjG3btYztBpEY149ecHA082OTYTPyqFobzUDZceAvbGnwpvvCQy22MKCVBvL/5dyQnZ7mbf/VdYI4zVq47EGa5c5Il1OrcXlWoubOfkPqpYF9EBFJx2xqWppwXYQuYz1e+EljXn2JiejHhMd54JoovplvQFgOGHPsm7vu49FzJZjCXa+R+G0Hok9mfZPl47TCu2U8gnzlN0b='
    # 加密后的密码，从浏览器或抓包工具中复制，可重复使用
    TPL_password2 = '52116fcb3a5bbda1a767eafce4cd99c8618a096d7fe52f65f9239ff364ff091c60fa7503559744cd869322404b570d34e6bef9111835360a9885663d6d88f941d457977d84e2776783c96e76dfa89fc4db95ef1666a667672ceb84ec1ba75f6e7800f1e1a82d35ce21a00dddcb112a1bf63b2337cc55082a31e10bade266eca9'
    ul = UsernameLogin(username, ua, TPL_password2)
    ul.login()
    #ul.check_list()
    #ul.place_order()
    ul.order()