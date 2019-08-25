*** Settings ***
Library  pylib/WebOpAdmin.py


*** Test Cases ***
添加培训班-tc003
    [Setup]  delete course

    add_course  初中语文  初中语文描述   1
    add_course  初中数学  初中数学描述   2

    delete training course

    training course  初中班1期  初中班1期描述  1  初中语文
    training course  初中班1期  初中班1期描述  1  初中数学

    ${listTraining}=  list training course
    should be true  $listTraining==['初中语文', '初中数学']



    [Teardown]  delete training course