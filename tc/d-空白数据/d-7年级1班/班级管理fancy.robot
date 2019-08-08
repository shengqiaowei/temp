#*** Settings ***
##WITH NAME：c002.py和c003.py里的setup、steps、teardown函数名字都是一样的
##           需要加个别名，区分下面tc002和tc003两条用例使用各自封装好的函数
#Library  cases/c002.py      WITH NAME  C002
#Library  cases/c003.py      WITH NAME  C003
#
#*** Test Cases ***
#添加班级-tc002
#    [Setup]  C002.setup
#    C002.steps
#    [Teardown]  C002.teardown
#
#添加班级-tc003
#    [Setup]  C003.setup
#     C003.steps
#    [Teardown]  C003.teardown