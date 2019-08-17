*** Settings ***
Library  pylib/StudentLib.py
Library  pylib/TeacherLib.py
Library  pylib/WebOpLib.py

Variables  config.py
Suite Setup  open_browser
Suite Teardown  close_browser


*** Test Cases ***
老师发布作业1-tc005101
    teacher login  shengqiaowei  888888

    teacher deliver task  测试作业2

    student login  sqw0706  888888

    student homework

    teacher login  shengqiaowei  888888

    ${check}=  teacher check homework
    should be true  $check==['A', 'A', 'A']