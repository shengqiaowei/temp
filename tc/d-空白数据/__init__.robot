*** Settings ***
#导入py写的关键字
Library  pylib/SchoolClassLib.py
Library  pylib/TeacherLib.py
#调用删除关键字进行初始化,先删除依赖关系，后删除被依赖关系
Suite Setup   Run Keywords    deleteAllTeacher  AND
              ...  delete all school classes
