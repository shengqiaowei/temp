from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


class  WebOpAdmin:
    url = 'http://localhost:8006/mgr/login/login.html'
    # robot调用不同关键字时，都只打开一次浏览器操作,必须要加上

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def open_browser1(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def close_browser1(self):
        self.driver.quit()

    #删除所有课程
    def delete_course(self):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        time.sleep(1)
        self.driver.implicitly_wait(2)
        while True:
            #点击删除按钮,elements返回的是一个列表,webdriver对象
            deleteButton = self.driver.find_elements_by_css_selector('button[ng-click="delOne(one)"]')
            print(deleteButton)
            #如果是一个空列表,就跳出循环
            if deleteButton==[]:
                break
            #每次循环都从第一行删除按钮进行点击
            deleteButton[0].click()
            #点击确认按钮
            self.driver.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)
        self.driver.implicitly_wait(10)

    #添加课程
    def add_course(self,corseName,courseDesc,courseIdx):
        #点击添加课程
        self.driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()

        self.driver.find_element_by_css_selector('input[ng-model="addData.name"]'
                                                 ).send_keys(corseName)
        self.driver.find_element_by_css_selector('textarea[ng-model="addData.desc"]'
                                                 ).send_keys(courseDesc)
        #由于排序默认显示1,所以先清空一下
        self.driver.find_element_by_css_selector('input[ng-model="addData.display_idx"]'
                                                 ).clear()
        self.driver.find_element_by_css_selector('input[ng-model="addData.display_idx"]'
                                                 ).send_keys(courseIdx)
        self.driver.find_element_by_css_selector('button[ng-click="addOne()"]').click()
        time.sleep(3)

        #创建一门课程后点击老师,再次点击课程，将页面刷新一次
        self.driver.find_element_by_css_selector('a[ui-sref="teacher"]').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()


    #列出课程,检查使用
    def listCourse(self):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()

        eles = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')

        return [ele.text for ele in eles]



    #登录
    def login(self,username,passwd):
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(passwd)
        self.driver.find_element_by_css_selector('button.btn-success').click()
        time.sleep(1)

    #删除所有老师
    def delete_taecher(self):
        #点击老师标签
        self.driver.find_element_by_css_selector('a[ui-sref="teacher"]').click()
        time.sleep(1)
        self.driver.implicitly_wait(2)
        while True:
            #点击删除按钮,elements返回的是一个列表,webdriver对象
            deleteButton = self.driver.find_elements_by_css_selector('button[ng-click="delOne(one)"]')
            print(deleteButton)
            #如果是一个空列表,就跳出循环
            if deleteButton==[]:
                break
            #每次循环都从第一行删除按钮进行点击
            deleteButton[0].click()
            #点击确认按钮
            self.driver.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)
        self.driver.implicitly_wait(10)

    #添加老师
    def add_teacher(self,teacherName,loginName,desc,idx,lesson):
        # 点击老师标签
        self.driver.find_element_by_css_selector('a[ui-sref="teacher"]').click()
        time.sleep(1)
        #点击添加老师
        self.driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()

        ele = self.driver.find_element_by_css_selector('input[ng-model="addEditData.realname"]')
        ele.clear()
        ele.send_keys(teacherName)

        ele = self.driver.find_element_by_css_selector('input[ng-model="addEditData.username"]')
        ele.clear()
        ele.send_keys(loginName)

        ele = self.driver.find_element_by_css_selector('textarea[ng-model="addEditData.desc"]')
        ele.clear()
        ele.send_keys(desc)

        ele = self.driver.find_element_by_css_selector('input[ng-model="addEditData.display_idx"]')
        ele.clear()
        ele.send_keys(idx)

        #选择授课信息
        select = Select(self.driver.find_element_by_css_selector('select[ng-model="$parent.courseSelected"]'))
        select.select_by_visible_text(lesson)

        #点击+号
        self.driver.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()

        #点击确定
        self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()
        time.sleep(2)

        # 增加一个老师后，将页面刷新一次
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        self.driver.find_element_by_css_selector('a[ui-sref="teacher"]').click()


    #列出老师,检查使用
    def list_tacher(self):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()

        eles = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')

        return [ele.text for ele in eles]

    #添加培训班
    def training_course(self,name,desc,idx,lesson):
        #点击培训班
        self.driver.find_element_by_css_selector('a[ui-sref="training"]').click()
        time.sleep(1)
        #点击添加培训班
        self.driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()
        time.sleep(1)

        ele = self.driver.find_element_by_css_selector('input[ng-model="addEditData.name"]')
        ele.clear()
        ele.send_keys(name)

        ele = self.driver.find_element_by_css_selector('textarea[ng-model="addEditData.desc"]')
        ele.clear()
        ele.send_keys(desc)

        ele = self.driver.find_element_by_css_selector('input[ng-model="addEditData.display_idx"]')
        ele.clear()
        ele.send_keys(idx)

        time.sleep(1)
        #选择授课信息
        select = Select(self.driver.find_element_by_css_selector('select[ng-options*="course"]'))
        select.select_by_visible_text(lesson)

        #点击+号
        self.driver.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()
        time.sleep(1)

        #点击确定
        self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()
        time.sleep(2)

        # # 增加一个培训班后，将页面刷新一次
        # self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        # self.driver.find_element_by_css_selector('a[ui-sref="training"]').click()

    #删除所有培训班
    def delete_training_course(self):
        #点击培训班标签
        self.driver.find_element_by_css_selector('a[ui-sref="training"]').click()
        time.sleep(1)
        self.driver.implicitly_wait(2)
        while True:
            #点击删除按钮,elements返回的是一个列表,webdriver对象
            deleteButton = self.driver.find_elements_by_css_selector('button[ng-click="delOne(one)"]')
            print(deleteButton)
            #如果是一个空列表,就跳出循环
            if deleteButton==[]:
                break
            #每次循环都从第一行删除按钮进行点击
            deleteButton[0].click()
            #点击确认按钮
            self.driver.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)
        self.driver.implicitly_wait(10)

    #列出培训班第二条记录，检查用
    def list_training_course(self):
        eles = self.driver.find_elements_by_css_selector('tr:nth-child(2) > td:nth-child(4) span')
        return [ele.text for ele in eles]


if __name__=='__main__':
#     cm = WebOpAdmin()
#     cm.open_browser()
#     try:
#         cm.login('auto','sdfsdfsdf')
#         cm.delete_course()
#         cm.add_course('语文课001','语文课描述001',2)
#         cm.add_course('语文课002', '语文课描述002', 1)
#         cm.listCourse()
#     except:
#         print('代码错误')
#     finally:
#         cm.close_browser()

    # cm = WebOpAdmin()
    # cm.open_browser1()
    # try:
    #     cm.login('auto','sdfsdfsdf')
    #     cm.delete_course()
    #     cm.add_course('初中语文','初中语文描述',1)
    #     cm.add_course('初中数学', '初中数学描述',2)
    #     cm.delete_taecher()
    #     cm.add_teacher('小盛','xiaosheng','小盛描述',2,'初中语文')
    #     cm.add_teacher('小侨', 'xiaoqiao', '小侨描述', 1, '初中数学')
    # except:
    #     print('代码错误')
    # finally:
    #     cm.close_browser1()

    # wa = WebOpAdmin()
    # try:
    #     wa.open_browser1()
    #     wa.login('auto','sdfsdfsdf')
    #     wa.delete_course()
    #     wa.add_course('初中语文','初中语文描述',1)
    #     wa.add_course('初中数学', '初中数学描述',2)
    #     wa.delete_training_course()
    #     wa.training_course('初中班1期','初中班1期描述',1,'初中语文')
    #     wa.training_course('初中班1期', '初中班1期描述', 1, '初中数学')
    # except:
    #     print('代码错误')
    # finally:
    #     wa.close_browser1()
        pass

