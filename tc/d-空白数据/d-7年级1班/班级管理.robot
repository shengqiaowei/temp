*** Settings ***
Library  pylib/SchoolClassLib.py

*** Test Cases ***

添加班级2 - tc000002
# 添加 7年级2班
    ${ret1}=    add school class    1     2班     60
    should be true     $ret1['retcode']==0

#列出班级，检验一下
    ${ret2}=    list school class    1
    ${retlist}=   evaluate   $ret2['retlist']
    classlist_should_not_contain   ${retlist}
    ...  2班  七年级    &{ret1}[invitecode]   60   0   &{ret1}[id]

    [Teardown]    delete_school_class   &{ret1}[id]


添加系统中存在的班级-tc000003
    #添加班级前先列出班级
    ${before}=  list school class

    #添加系统存在的班级
    ${ret1}=  add school class  1  1班  60
    should be true  $ret1['retcode']==1
    #添加班级后列出班级
    ${after}=  list school class

    #对比前后是否结果相同
    should be true  $before==$after

修改班级1-tc000051

# 添加 7年级2班
    ${ret10}=    add school class    1     2班     60
    should be true     $ret10['retcode']==0
    ${classid}=  evaluate  $ret10['id']
#修改班级名字为22班
    ${modifyClass}=  modifyClass  ${classid}   22班  60
    should be true  $modifyClass['retcode']==0

#列出班级，检验一下
    ${listRet2}=    list school class    1
    ${retlist}=   evaluate   $listRet2['retlist']
    classlist_should_not_contain   ${retlist}
    ...  22班  七年级    &{ret10}[invitecode]   60   0   &{ret10}[id]

    [Teardown]    delete_school_class   &{ret10}[id]

修改班级2-tc000052

#  添加7年级2班
    ${ret1}=    add school class    1     2班     60
    should be true     $ret1['retcode']==0
    ${classid}=    evaluate  $ret1['id']

#  先列出班级
    ${listret1}=    list school class    1

#  修改为7年级1班
    ${modifyRet}=    modifyClass   ${classid}   1班     60
    should be true     $modifyRet['retcode']==10000


#  再次列出班级，检验一下，应该和之前列出的相同
    ${listret2}=    list school class    1
    should be equal    ${listret1}     ${listret2}

    [Teardown]    delete_school_class   ${classid}

修改班级3-tc000053
    ${modifyRet}=  modifyClass  99999999  1班  60
    should be true  $modifyRet['retcode']==404
    #should be true  $modifyRet['reason']=="id为‘99999999’的班级不存在"

删除班级1-tc000081
    ${delRet}=  delete school class  99999999
    should be true  $delRet['retcode']==404
    #should be true  $delRet['reason']=="id为`999999999`的班级不存在"

删除班级2-tc000082

    #先列出班级
    ${listRet1}=  list school class  1

    #添加班级
    ${addRet}=  add school class  1  2班  20
    should be true  $addRet['retcode']==0
    ${classid}=    evaluate  $addRet['id']

    #列出班级，检验一下
    ${listRet2}=    list school class    1
    classlist_should_not_contain   &{listRet2}[retlist]
    ...  2班  七年级    &{addRet}[invitecode]   20   0   &{addRet}[id]

    #删除班级
    ${delRet}=  delete school class   ${classid}
    should be true  $delRet['retcode']==0

    #后列出班级
    ${listRet3}=  list school class  1

    #对比
    should be true   $listRet1==$listRet3





