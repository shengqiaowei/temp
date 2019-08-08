*** Settings ***
Library  pylib/SchoolClassLib.py
#初始化，默认先添加一个班级
Suite Setup    add_school_class   1  1班  60