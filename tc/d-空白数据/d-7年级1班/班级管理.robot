*** Settings ***
Library  pylib/SchoolClassLib.py

*** Test Cases ***
添加系统中不存在班级-tc002
    ${ret1}=  add school class  1  2班  60
    should be true  $ret1['retcode']==0

列出班级，检查一下
    ${ret2}=  list school class  1
    ${retlist}=  evaluate  $ret2['retlist']
    classlist should contain  ${retlist}
    ...  2班  七年级  &{ret1}['invitecode']  60  0  &{ret1}['id']
    [Teardown]  delete school class  &{ret1}['id']

添加系统中存在的班级-tc003
    #添加班级前先列出班级
    ${before}=  list school class

    #添加系统存在的班级
    ${ret1}=  add school class  1  1班  60
    should be true  $ret1['retcode']==1
    #添加班级后列出班级
    ${after}=  list school class

    #对比前后是否结果相同
    should be true  $before==$after

