*** Settings ***
Library  pylib/CourseManage.py

*** Test Cases ***
老师管理-tc002
    [Setup]  run keywords  delete course
    ...      AND  add course  初中语文  初中语文描述  1
    ...      AND  add course  初中数学  初中数学描述  2
    ...      AND  delete taecher

    add teacher  小盛  xiaosheng  小盛描述  2  初中语文
    add teacher  小侨  xiaoqiao  小侨描述  1  初中数学

    ${listTeacher}=  list tacher
    should be true  $listTeacher==['小侨', '小盛']

    [Teardown]  run keywords  delete taecher
    ...         AND  delete course