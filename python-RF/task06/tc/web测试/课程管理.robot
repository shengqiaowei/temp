*** Settings ***
Library  pylib/WebOpAdmin.py


*** Test Cases ***
添加课程-tc001
    [Setup]  delete_course
    add_course  语文课001  语文课描述001   2

    ${lessons}=  listCourse

    should be true  $lessons==['语文课001']

    add_course  语文课002  语文课描述002   1

    ${lessons}=  listCourse

    should be true  $lessons==['语文课002', '语文课001']

    [Teardown]  delete course