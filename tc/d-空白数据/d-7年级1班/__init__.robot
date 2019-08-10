
#以下是使用rf定义用户关键字
#*** Keywords ***
#suite setup action
#    ${ret}=  add school class  1  1班  60
#    set global variable  ${suite_g7c1_classid}  &{ret}[id]

*** Settings ***
Library  pylib/SchoolClassLib.py
#初始化，默认先添加一个班级
Suite Setup    add_school_class  1  1班  60  suite_g7c1_classid
Suite Teardown  delete_school_class  ${suite_g7c1_classid}