from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

class ReGressionTest:
    # robot调用不同关键字时，都只打开一次浏览器操作,必须要加上

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    url = 'https://www.ibaotu.com'

    def open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        #self.driver.implicitly_wait(10)

    def close_browser(self):
        self.driver.quit()

    #广告设计：查询、下载
    def gg_download(self,info):
        self.driver.find_element_by_css_selector('a[data-spot="广告设计"]').click()
        time.sleep(2)

        #获取当前handle
        currentHandle = self.driver.current_window_handle

        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '【原创】广告设计模板免费下载_广告设计图片素材_【包图网】'== handle.title():
                print('广告设计页面')
                break
        time.sleep(2)

        # 输入查询信息
        self.driver.find_element_by_css_selector('input[id="ggtb-so-kw"]').send_keys(info)

        #点击查询
        self.driver.find_element_by_css_selector('#ggtb-search-btn .icon-search').click()
        time.sleep(2)

        #滚动下拉条
        self.scroll_bar()

        #点击下载
        self.driver.find_element_by_css_selector('.gradient-ver-bw .gradient-hor-og').click()
        time.sleep(1)

        #下载确认页点击下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)
        self.driver.switch_to.window(currentHandle)

    #摄影图:查询、下载
    def sy_download(self,info):
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]/nav/ul/li[3]/a').click()
        time.sleep(2)

        #获取当前handle
        currentHandle = self.driver.current_window_handle

        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '高清摄影图片欣赏_正版商业摄影图片下载_【包图网】'== handle.title():
                print('摄影图页面')
                break
        time.sleep(2)

        #输入查询信息
        self.driver.find_element_by_css_selector('input[id="ggtb-so-kw"]').send_keys(info)

        #点击查询
        self.driver.find_element_by_css_selector('#ggtb-search-btn .icon-search').click()
        time.sleep(2)

        #下拉滚动条
        self.scroll_bar()

        #点击下载
        self.driver.find_element_by_css_selector('.gradient-ver-bw .gradient-hor-og').click()
        time.sleep(1)

        #下载确认页点击下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)
        self.driver.switch_to.window(currentHandle)

    #字体:下载
    def zt_download(self):
        self.driver.find_element_by_css_selector('a[href="/Font.html"]').click()
        time.sleep(2)

        #获取当前handle
        currentHandle = self.driver.current_window_handle

        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '【原创】字体设计_字体下载_字体下载大全_【包图网】'== handle.title():
                print('字体页面')
                break
        time.sleep(2)

        #点击 黑体 标签
        self.driver.find_element_by_css_selector('a[class="classifys "]').click()
        time.sleep(1)

        #下拉滚动条
        self.scroll_bar()

        #点击立即下载
        self.driver.find_element_by_css_selector('a[data-font-id="a93e6ced39a04f1d9bb2ad0220ceb3ec"]').click()
        time.sleep(1)

        # 获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '包图网'== handle.title():
                print('字体下载页面')
                break
        time.sleep(2)

        #点击下载确认页下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)
        self.driver.switch_to.window(currentHandle)

    #UI设计:查询、下载
    def ui_download(self,info):
        self.driver.find_element_by_css_selector('a[data-spot="UI设计"]').click()
        time.sleep(2)

        #获取当前handle
        currentHandle = self.driver.current_window_handle

        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '【原创】UI设计图片_UI设计素材_UI设计模板_【包图网】'== handle.title():
                print('UI设计页面')
                break
        time.sleep(2)

        #输入查询信息
        self.driver.find_element_by_css_selector('input[id="ggtb-so-kw"]').send_keys(info)

        #点击查询
        self.driver.find_element_by_css_selector('#ggtb-search-btn .icon-search').click()
        time.sleep(2)

        #下拉滚动条
        self.scroll_bar()

        #点击下载
        self.driver.find_element_by_css_selector('.gradient-ver-bw .gradient-hor-og').click()
        time.sleep(1)

        #下载确认页点击下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)
        self.driver.switch_to.window(currentHandle)

    #电商淘宝:查询、下载
    def ds_download(self,info):
        self.driver.find_element_by_css_selector('a[data-spot="电商淘宝"]').click()
        time.sleep(2)

        #获取当前handle
        currentHandle = self.driver.current_window_handle
        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '【原创】淘宝素材_淘宝装修模板_免费电商淘宝图片素材_【包图网】'== handle.title():
                print('电商淘宝页面')
                break

        time.sleep(2)

        #输入查询信息
        self.driver.find_element_by_css_selector('input[id="ggtb-so-kw"]').send_keys(info)

        #点击查询
        self.driver.find_element_by_css_selector('#ggtb-search-btn .icon-search').click()
        time.sleep(2)

        #下拉滚动条
        self.scroll_bar()

        #点击下载
        self.driver.find_element_by_css_selector('.gradient-ver-bw .gradient-hor-og').click()
        time.sleep(1)

        #下载确认页点击下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)
        self.driver.switch_to.window(currentHandle)

    #多媒体:查询、下载
    def dmt_download(self,Info):
        self.driver.find_element_by_css_selector('a[data-spot="多媒体"]').click()
        time.sleep(2)

        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '【原创】高清视频素材模板免费下载_片头视频素材大全_【包图网】'== handle.title():
                print('视频页面')
                break

        time.sleep(2)

        #输入视频查询信息
        self.driver.find_element_by_css_selector('input[id="ggtb-so-kw"]').send_keys(Info)

        #点击查询视频
        self.driver.find_element_by_css_selector('#ggtb-search-btn .icon-sousuo1').click()
        time.sleep(2)

        #下拉滚动条
        self.scroll_bar()

        #获取查询后的句柄
        spCurrent = self.driver.current_window_handle

        #点击下载视频
        self.driver.find_element_by_css_selector('span.collect-words').click()
        time.sleep(1)

        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '图片编号:' in handle.title():
                print('视频下载确认页')
                break

        time.sleep(2)

        #点击下载确认页 视频
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)


        #切回视频句柄
        self.driver.switch_to.window(spCurrent)

        #将关键词X掉
        self.driver.find_element_by_css_selector('div.pb-mask').click()
        time.sleep(1)

        #点击音效
        self.driver.find_element_by_css_selector('li[data-url="yinxiao"]').click()
        time.sleep(1)

        #点击海外精选
        self.driver.find_element_by_css_selector('a[href="//ibaotu.com/yinxiao/10-0-0-0-3-1.html?so=1"]').click()
        time.sleep(1)

        #点击立即下载 音效
        self.driver.find_element_by_css_selector('div.audio-info .gradient-hor-og').click()
        time.sleep(1)

        # 获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '图片编号:' in handle.title():
                print('音效下载确认页')
                break

        time.sleep(2)

        #下载确认页点击下载 音效
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)

        #切回视频句柄
        self.driver.switch_to.window(spCurrent)

        # 点击配乐
        self.driver.find_element_by_css_selector('li[data-url="peiyue"]').click()
        time.sleep(1)

        # 输入配乐关键词
        self.driver.find_element_by_id('ggtb-so-kw').send_keys(Info)
        time.sleep(1)

        #点击搜索
        self.driver.find_element_by_css_selector('i.icon-sousuo1').click()
        time.sleep(1)

        # 点击立即下载 配乐
        self.driver.find_element_by_css_selector('a[class="free-down gradient-hor-og"]').click()
        time.sleep(1)

        # 获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '图片编号:' in handle.title():
                print('配乐下载确认页')
                break
        time.sleep(2)

        # 下载确认页点击下载 配乐
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)
        self.driver.switch_to.window(spCurrent)

    #翻页
    #点击下一页
    def Page(self):
        self.driver.find_element_by_css_selector('a.next').click()
        time.sleep(1)
        #点击第三页
        self.driver.find_element_by_css_selector('div.pagelist :nth-child(4)').click()
        time.sleep(1)


    #全站搜索
    def search(self,info):
        #输入关键词
        self.driver.find_element_by_id('so-kw').send_keys(info)

        #点击查询
        self.driver.find_element_by_css_selector('a.but-search').click()
        time.sleep(1)

        #循环点击所有分类标签
        for i in range(1,20):
            sum = 1
            sum+=i
            print(sum)
            if sum<=17:
                self.driver.find_element_by_css_selector('div.right-wrap :nth-child(%s)' % sum).click()
                time.sleep(1)

                #点击x号
                self.driver.find_element_by_css_selector('div.pb-mask').click()
                time.sleep(1)
            else:
                break

    #ppt:查询、下载
    def ppt_download(self,info):
        self.driver.find_element_by_css_selector('a[data-spot="办公文档"]').click()
        time.sleep(2)

        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '【ppt模板|excel模板|word模板】' in handle.title():
                break
        time.sleep(2)

        #输入查询信息
        self.driver.find_element_by_css_selector('#ggtb-so-kw').send_keys(info)

        #点击查询
        self.driver.find_element_by_id('ggtb-search-btn').click()
        time.sleep(2)

        #下拉滚动条
        self.scroll_bar()

        #点击下载
        self.driver.find_element_by_css_selector('.gradient-ver-bw .gradient-hor-og').click()
        time.sleep(1)

        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '图片编号:' in handle.title():
                print('ppt下载确认页面')
                break
        time.sleep(2)

        #下载确认页点击下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)

        #点击左上角包图网，切换回首页句柄
        self.driver.find_element_by_css_selector('.head-wrap >a[href="//ibaotu.com"]').click()

    #word:查询、下载
    def word_download(self,info):

        #点击办公文档
        self.driver.find_element_by_css_selector('a[data-spot="办公文档"]').click()
        time.sleep(1)

        #将句柄切换到ppt页面
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '【ppt模板|excel模板|word模板】' in handle.title():
                break
        time.sleep(2)
        #点击word分类
        self.driver.find_element_by_css_selector('a[href="/word/"]').click()
        time.sleep(2)

        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if 'Word模板免费下载' in handle.title():
                break
        time.sleep(2)

        #输入查询信息
        self.driver.find_element_by_css_selector('#ggtb-so-kw').send_keys(info)

        #点击查询
        self.driver.find_element_by_id('ggtb-search-btn').click()
        time.sleep(2)

        #下拉滚动条
        self.scroll_bar()

        #点击下载
        self.driver.find_element_by_css_selector('.gradient-ver-bw .gradient-hor-og').click()
        time.sleep(1)

        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '图片编号:' in handle.title():
                print('word下载确认页面')
                break
        time.sleep(2)

        #下载确认页点击下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)

        # 点击左上角包图网，切换回首页句柄
        self.driver.find_element_by_css_selector('.head-wrap >a[href="//ibaotu.com"]').click()

    #excel:查询、下载
    def excel_download(self,info):

        #点击办公文档
        self.driver.find_element_by_css_selector('a[data-spot="办公文档"]').click()
        time.sleep(1)

        #将句柄切换到ppt页面
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '【ppt模板|excel模板|word模板】' in handle.title():
                break
        time.sleep(2)
        #点击excel分类
        self.driver.find_element_by_css_selector('a[href="/excle/"]').click()
        time.sleep(2)

        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if 'Excel模板免费下载' in handle.title():
                break
        time.sleep(2)

        #输入查询信息
        self.driver.find_element_by_css_selector('#ggtb-so-kw').send_keys(info)

        #点击查询
        self.driver.find_element_by_id('ggtb-search-btn').click()
        time.sleep(2)

        #下拉滚动条
        self.scroll_bar()

        #点击下载
        self.driver.find_element_by_css_selector('.gradient-ver-bw .gradient-hor-og').click()
        time.sleep(1)

        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '图片编号:' in handle.title():
                print('excel下载确认页面')
                break
        time.sleep(2)

        #下载确认页点击下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)

        # 点击左上角包图网，切换回首页句柄
        self.driver.find_element_by_css_selector('.head-wrap >a[href="//ibaotu.com"]').click()


    #装饰装修:查询、下载
    def zs_download(self,info):
        self.driver.find_element_by_css_selector('a[data-spot="装饰·模型"]').click()
        time.sleep(2)

        #获取当前handle
        currentHandle = self.driver.current_window_handle
        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '【原创】装饰装修图片_' in handle.title():
                print('装饰装修页面')
                break

        time.sleep(2)

        #输入查询信息
        self.driver.find_element_by_css_selector('input[id="ggtb-so-kw"]').send_keys(info)

        #点击查询
        self.driver.find_element_by_css_selector('#ggtb-search-btn .icon-search').click()
        time.sleep(2)

        #下拉滚动条
        self.scroll_bar()

        #点击下载
        self.driver.find_element_by_css_selector('.gradient-ver-bw .gradient-hor-og').click()
        time.sleep(1)

        #下载确认页点击下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)
        self.driver.switch_to.window(currentHandle)

    #插画:查询、下载
    def ch_download(self,info):
        self.driver.find_element_by_css_selector('a[data-spot="插画配图"]').click()
        time.sleep(2)

        #获取当前handle
        currentHandle = self.driver.current_window_handle
        #获取所有handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '原创】插画配图图片_' in handle.title():
                print('插画页面')
                break

        time.sleep(2)

        #输入查询信息
        self.driver.find_element_by_css_selector('input[id="ggtb-so-kw"]').send_keys(info)

        #点击查询
        self.driver.find_element_by_css_selector('#ggtb-search-btn .icon-search').click()
        time.sleep(2)

        #下拉滚动条
        self.scroll_bar()

        #点击下载
        self.driver.find_element_by_css_selector('.gradient-ver-bw .gradient-hor-og').click()
        time.sleep(1)

        #下载确认页点击下载
        self.driver.find_element_by_css_selector('#downvip >span').click()
        time.sleep(3)
        self.driver.switch_to.window(currentHandle)

    #控制滚动条
    def scroll_bar(self):
        # 将页面滚动条拖到底部
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.driver.execute_script(js)
        # time.sleep(3)

        #测试用
        #self.open_browser()

        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        time.sleep(2)
        js = "var q=document.documentElement.scrollTop=3000"
        self.driver.execute_script(js)
        time.sleep(2)
        # 将滚动条移动到页面的顶部
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        time.sleep(3)

    #收藏
    def collection(self,info):
        self.driver.find_element_by_id('so-kw').send_keys(info)
        self.driver.find_element_by_css_selector('a.but-search').click()
        time.sleep(1)

        #定位第一个素材
        firstElement = self.driver.find_element_by_css_selector('.hover-pop .sucai-jump')

        #鼠标悬停在第一个素材上
        ActionChains(self.driver).move_to_element(firstElement).perform()
        time.sleep(1)

        #点击收藏图标
        self.driver.find_element_by_css_selector('i.icon-shoucang1').click()
        time.sleep(1)

        #点击收藏
        self.driver.find_element_by_css_selector('.col-md-item-btn :nth-child(1)').click()
        time.sleep(3)

        #点击x
        self.driver.find_element_by_css_selector('.col-md-head >span.icon-danchuang_guanbiicon1').click()
        time.sleep(1)

        # 点击左上角包图网，切换回首页句柄
        self.driver.find_element_by_css_selector('.head-wrap >a[href="//ibaotu.com"]').click()
        time.sleep(1)

if __name__ == '__main__':
    rt = ReGressionTest()
    try:
        rt.open_browser()
        #rt.gg_download('大数据')
        # rt.sy_download('大数据')
        # rt.zt_download()
        # rt.ui_download('全套界面')
        # rt.ds_download('双十一')
        # rt.dmt_download('年会')
        #rt.search('中秋节')
        # rt.ppt_download('国庆节')
        # rt.word_download('简历')
        # rt.excel_download('工资')
        #rt.zs_download('地板')
        #rt.ch_download('卡通')
        rt.collection('人工智能')

    except:
        print('代码错误')
    finally:
        rt.close_browser()