#*** Settings ***
##WITH NAME：c002.py和c003.py里的setup、steps、teardown函数名字都是一样的
##           需要加个别名，区分下面tc002和tc003两条用例使用各自封装好的函数
#Library  cases/c000002.py      WITH NAME  C000002
#Library  cases/c000003.py      WITH NAME  C000003
#Library  cases/c000051.py      WITH NAME  C000051
#
#*** Test Cases ***
#添加班级-tc000002
#    [Setup]  C000002.setup
#    C000002.steps
#    [Teardown]  C000002.teardown
#
#添加班级-tc000003
#    [Setup]  C000003.setup
#     C000003.steps
#    [Teardown]  C000003.teardown
#
#修改班级-tc000051
#    [Setup]  C000051.setup
#    C000051.steps
#    [Teardown]  C000051.teardown