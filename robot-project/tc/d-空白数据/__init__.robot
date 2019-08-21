*** Settings ***
#导入py写的关键字
Library  pylib/SchoolClassLib.py
Library  pylib/TeacherLib.py
Library  pylib/StudentLib.py
#调用删除关键字进行初始化,先删除依赖关系的，老师是需要依赖班级的，被依赖的后删除，班级是被老师依赖的
Suite Setup   Run Keywords    deleteAllTeacher  AND
              ...  delete all school classes    AND
              ...  delete all student
