from selenium import webdriver
import config
import time
from pprint import pprint

class WebOpLib:

    #robot调用不同关键字时，都只打开一次浏览器操作,必须要加上

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def open_browser(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)

    def close_browser(self):
        self.wd.quit()

    #登录
    def teacher_login(self,username,password):
        self.wd.get(config.g_teacher_login_url)
        self.wd.find_element_by_id('username').send_keys(username)
        self.wd.find_element_by_id('password').send_keys(password)
        self.wd.find_element_by_id('submit').click()

        #校验主页
        self.wd.find_element_by_css_selector('a[href="#/home"]>li')

    #获取老师主页信息
    def get_teacher_homepage_info(self):
        #点击主页
        self.wd.find_element_by_css_selector('a[href="#/home"]>li').click()

        #页面动态加载，先等待2s
        time.sleep(2)

        #获取老师主页信息
        eles = self.wd.find_elements_by_css_selector('.row .ng-binding')

        #将每个字段信息通过文本的方式打印出来
        eleText = [ele.text for ele in eles]
        pprint(eleText)
        return  eleText

    #查看学生列表
    def get_teacher_class_students_info(self):
        self.wd.find_element_by_css_selector('.main-menu >ul> li:nth-of-type(4)').click()

        self.wd.find_element_by_css_selector('a[href="#/student_group"] span').click()

        time.sleep(2)

        classStudentTab={}

        #获取班级的整个表格信息
        classes= self.wd.find_elements_by_css_selector('div.panel')

        for cla in classes:
            #获取头部信息
            gradeclass=cla.find_element_by_css_selector('div.panel-heading').text.replace(' ','')

            #点击一下，展示表格里的学生信息
            cla.click()

            time.sleep(2)

            self.wd.implicitly_wait(1)
            #获取所有学生信息
            nameEles = cla.find_elements_by_css_selector('tr > td:nth-child(2)')
            self.wd.implicitly_wait(10)

            #返回的是一个webelement对象，所以需要.text
            names = [ nameEle.text for nameEle in nameEles]

            #对空字典进行key和value赋值
            classStudentTab[gradeclass]=names

        pprint(classStudentTab)

        return classStudentTab

if __name__=='__main__':
    webop = WebOpLib()
    webop.open_browser()
    webop.teacher_login('shengqiaowei',888888)
    webop.get_teacher_homepage_info()
    webop.get_teacher_class_students_info()
    webop.close_browser()

