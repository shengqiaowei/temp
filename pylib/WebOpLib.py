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

    #老师登录
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

    #学生登录
    def student_login(self,username,password):
        self.wd.get(config.g_student_login_url)
        self.wd.find_element_by_id('username').send_keys(username)
        self.wd.find_element_by_id('password').send_keys(password)
        self.wd.find_element_by_id('submit').click()

        #校验主页
        self.wd.find_element_by_css_selector('a[href="#/home"]>li')

    #获取学生主页信息
    def get_student_homepage_info(self):
        #点击主页
        self.wd.find_element_by_css_selector('a[href="#/home"]>li').click()

        #页面动态加载，先等待2s
        time.sleep(2)

        #获取学生主页信息
        eles = self.wd.find_elements_by_css_selector('.row .ng-binding')

        #将每个字段信息通过文本的方式打印出来
        eleText = [ele.text for ele in eles]

        #删除注册码这个字段信息
        eleText.pop(2)
        pprint(eleText)
        return  eleText

    #获取错题库信息
    def student_wrong(self):
        self.wd.find_element_by_css_selector('div.main-menu a[href="#/yj_wrong_questions"] li'
                                             ).click()
        time.sleep(1)
        wrongInfo = self.wd.find_element_by_css_selector('#page-wrapper').text
        pprint(wrongInfo)
        return wrongInfo

    #老师发布作业
    def teacher_deliver_task(self,exam_name):
        self.wd.find_element_by_css_selector('.main-menu ul li:nth-of-type(2)').click()
        self.wd.find_element_by_css_selector('a[ng-click^="show_page_addexam"] span').click()

        time.sleep(2)
        self.wd.find_element_by_id('exam_name_text').send_keys(exam_name)
        self.wd.find_element_by_id('btn_pick_question').click()


        #进入一个弹窗页面，先等待一下
        time.sleep(2)


        # 题目在新的frame中,使用id切换进去
        self.wd.switch_to.frame('pick_questions_frame')

        #选择前3道题目

        #每次选择一道题目，界面都会重新渲染，所以使用循环获取
        for counter in range(3):
            selectButtons=self.wd.find_elements_by_css_selector('.btn_pick_question')
            selectButtons[counter].click()

            # 每次获取完一个后，页面渲染等待一下
            time.sleep(1)

        # 点击确定按钮
        self.wd.find_element_by_css_selector('div.btn-blue').click()


        #切换回主html
        self.wd.switch_to.default_content()

        time.sleep(1)

        # 点击确定添加
        self.wd.find_element_by_id('btn_submit').click()

        #选择发布给学生
        self.wd.find_element_by_css_selector('.bootstrap-dialog-footer-buttons button.btn-primary:nth-child(2)'
                                             ).click()

        time.sleep(1)

        #切换浏览器句柄

        #保留目前浏览器句柄
        currentHandle=self.wd.current_window_handle

        #获取浏览器所有句柄
        handles = self.wd.window_handles

        #循环获取句柄，并且切换到下发学习任务句柄
        for handle in handles:
            #切换到新窗口
            self.wd.switch_to.window(handle)
            #判断是否是我们需要的新窗口
            if '下发学习任务' in self.wd.title:
                print('进入到下发学习任务窗口')
                break

        time.sleep(1)

        #只有1位同学，直接勾选即可
        self.wd.find_element_by_css_selector('label.myCheckbox').click()
        #点击确定下发
        self.wd.find_element_by_css_selector('button[ng-click="openDispatchDlg()"]').click()

        time.sleep(1)

        self.wd.find_element_by_css_selector('button[ng-click="dispatchIt()"]').click()

        self.wd.find_element_by_css_selector('button.btn-default').click()

        #切回主窗口
        self.wd.switch_to.window(currentHandle)

    # 学生写作业
    def student_homework(self):
        self.wd.find_element_by_css_selector('.main-menu ul a[href="#/task_manage"] li').click()

        time.sleep(1)

        # 点击第一个去做，使用element肯定获取的是第一个'去做'
        self.wd.find_element_by_css_selector('button[ng-click="viewTask(taskTrack)"]').click()

        time.sleep(1)

        # 选择题全部选A
        firstChoose = self.wd.find_elements_by_css_selector('.btn-group button:nth-child(1)')
        for choose in firstChoose:
            choose.click()

        # 点击提交
        self.wd.find_element_by_css_selector('button[ng-click="saveMyResult(true)"]').click()

        # 点击确定
        self.wd.find_element_by_css_selector('.bootstrap-dialog-footer-buttons >button.btn-primary').click()

        time.sleep(1)

    # 老师检查作业
    def teacher_check_homework(self):
        # 点击作业
        self.wd.find_element_by_css_selector('.main-menu ul li:nth-of-type(2)').click()

        # 点击已发布作业
        self.wd.find_element_by_css_selector('a[href="#/task_manage?tt=1"] li span').click()

        time.sleep(1)

        # 点击查看作业,只查看第一个即可,使用element
        self.wd.find_element_by_css_selector('a[ng-click="trackTask(task)"]').click()

        time.sleep(1)

        # 点击第一个学生查看,使用*号 包含即可
        self.wd.find_element_by_css_selector('button[ng-click*=viewTaskTrack]').click()

        time.sleep(1)

        #获取当前句柄
        currentHandle = self.wd.current_window_handle

        #获取浏览器所有的句柄
        handles = self.wd.window_handles

        #切换查看作业句柄
        for handle in handles:
            self.wd.switch_to.window(handle)
            #判断是否在查看作业html页面上
            if '查看作业' in self.wd.title:
                print('进入到查看作业窗口下')
                break

        # 勾选的选项会有 .myCheckbox input:checked  风格修饰，
        # 但是这个不出现在 元素html里面
        eles = self.wd.find_elements_by_css_selector('.myCheckbox input:checked')

        selectedchoices = [ele.find_element_by_xpath('./..').text.strip() for ele in eles]

        print(selectedchoices)

        # 切回主窗口
        self.wd.switch_to.window(currentHandle)
        return selectedchoices






if __name__=='__main__':
    webop = WebOpLib()
    webop.open_browser()

    #测试学生

    # webop.teacher_login('shengqiaowei',888888)
    # webop.get_teacher_homepage_info()
    # webop.get_teacher_class_students_info()
    #webop.close_browser()

    #测试老师

    # webop.student_login('shengqiaowei100',888888)
    # webop.get_student_homepage_info()
    # webop.student_wrong()
    # webop.close_browser()

    #测试老师发布作业

    # webop.teacher_login('shengqiaowei',888888)
    # webop.teacher_deliver_task('测试作业1')
    # #webop.close_browser()
    #
    # #测试学生提交作业
    # webop.student_login('sqw0706',888888)
    # webop.student_homework()
    # #webop.close_browser()
    #
    # #测试老师检查作业
    # webop.teacher_login('shengqiaowei',888888)
    # webop.teacher_check_homework()
    # webop.close_browser()

