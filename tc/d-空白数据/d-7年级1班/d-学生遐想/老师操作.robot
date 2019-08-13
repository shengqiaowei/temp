*** Settings ***
Library  pylib/TeacherLib.py
Library  pylib/WebOpLib.py
Variables  config.py

Suite Setup  open_browser
Suite Teardown  close_browser

*** Test Cases ***
老师登录2-tc005002


    #添加老师
    ${addRet}=  addTeacher  shengqiaowei001  sqw001
    ...                     ${g_subject_math_id}
    ...                     ${suite_g7c1_classid}
    ...                     13732327438  123@qq.com   331002199607064918

    teacher login  shengqiaowei001  888888

    ${teacherInformation}=  get_teacher_homepage_info

    should be true  $teacherInformation==['松勤学院00602', 'sqw001', '初中数学', '0', '0', '0']

    ${classStudent}=  get_teacher_class_students_info
        should be true     $classStudent=={'七年级1班':['遐想']}

    [Teardown]   deleteTeacher  &{addRet}[id]