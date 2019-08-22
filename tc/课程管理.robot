*** Settings ***
Library   pylib/CourseManage.py
Suite Setup  open_browser1
Suite Teardown  close_browser1

*** Test Cases ***
添加课程-tc88888
    login  auto  sdfsdfsdf
    add_course  语文课001  语文课描述001   2
    add_course  语文课002  语文课描述002   1
    listCourse
