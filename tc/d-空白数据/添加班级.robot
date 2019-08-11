*** Settings ***
Library  pylib/SchoolClassLib.py

*** Test Cases ***
添加班级1-tc000001
    ${ret1}=  add school class  1  语文一班  50
    should be true  $ret1['retcode']==0



#列出班级，检验一下
    ${ret2}=  list school class   1
    #evaluate将response里的retlist里的第一个字典获取出来
    ${fc}=  evaluate  $ret2['retlist'][0]
    #retlist第一个字典里的id和ret1里的id是否相等
    should be true  $fc['id']==$ret1['id']
    #retlist第一个字典里的id和ret1里的invitecode相等
    should be true  $fc['invitecode']==$ret1['invitecode']

    #为了保证下次再运行数据环境都为空，运行结束需要加一个清除操作
    #返回的是一个字典，所以使用&符号
    [Teardown]  delete school class  &{ret1}[id]