*** Settings ***
Library  pylib/WebOpAdmin.py


*** Test Cases ***
添加培训班期-tc004
    [Setup]  run keywords  delete training course qi
    ...      AND  delete course

    add_course  初中语文  初中语文描述   1

    delete training course

    training course  初中班  初中班1期描述  1  初中语文

    add training course qi  初中班1期  初中班1期描述  2  初中班

    ${listTraining}=  list training course qi
    should be true  $listTraining==['初中班1期']

    [Teardown]  delete training course qi