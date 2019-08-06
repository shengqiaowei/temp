*** Settings ***
#导入py写的关键字
Library  pylib/SchoolClassLib.py
#调用删除关键字进行初始化
Suite Setup   delete all school classes