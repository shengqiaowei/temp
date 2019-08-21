*** Settings ***
Library  pylib/TeacherLib.py
Library  pylib/SchoolClassLib.py
Variables  config.py

*** Test Cases ***
添加老师2-tc001002
#添加一个老师教7年级1班 科学，一个班级不能同时存在2个老师
    ${addRet}=  addTeacher  shengqiaowei002  sqw002
    ...                     ${g_subject_science_id}
    ...                     ${suite_g7c1_classid}
    ...         13732327439  1234@qq.com   331002199607064919

    should be true  $addRet['retcode']==0

#列出老师，检验一下
    ${listRet}=  listTeacher

    teacherlist_should_not_contain  &{listRet}[retlist]   shengqiaowei002  sqw002
    ...                             &{addRet}[id]
    ...                             ${suite_g7c1_classid}
    ...                             13732327439  1234@qq.com   331002199607064919

    [Teardown]  deleteTeacher   &{addRet}[id]

添加老师3-tc001003

    #添加之前列出
    ${before}=  listTeacher

    #创建同名老师
    ${addRet}=  addTeacher  shengqiaowei  sqw
    ...                     ${g_subject_math_id}
    ...                     ${suite_g7c1_classid}
    ...                     13732327438  123@qq.com   331002199607064918

    should be true  $addRet['retcode']==1
    should be true  $addRet['reason']=='登录名 shengqiaowei 已经存在'

    #添加之后列出
    ${after}=  listTeacher

    #前后对比
    should be equal  ${before}   ${after}


修改老师1-tc001051
    #添加之前列出
    ${before}=  listTeacher

    ${modifyRet}=  modifyTeacher  999999
    should be true  $modifyRet['retcode']==1
    should be true  $modifyRet['reason']=='id 为`999999`的老师不存在'

    #添加之后列出
    ${after}=  listTeacher

    should be equal  ${before}  ${after}

修改老师2-tc001052
    #这条用例存在系统bug
    #添加1个科学老师
    ${addRet}=  addTeacher  shengqiaowei002  sqw002
    ...                     ${g_subject_science_id}
    ...                     ${suite_g7c1_classid}
    ...         13732327439  1234@qq.com   331002199607064919

    should be true  $addRet['retcode']==0

    #添加7年级2班
    ${addClass}=  add_school_class  1  2班  60
    should be true  $addClass['retcode']==0

    #修改老师真实姓名和授课班级
    ${modifyRet}=  modifyTeacher  &{addRet}[id]  sqw003
    ...   classlist=${suite_g7c1_classid},&{addClass}[id]

    should be true  $modifyRet['retcode']==0

    #列出老师检验一下
    ${listRet}=  listTeacher
    ${listRet}=  evaluate  $listRet['retlist']
    teacherlist should not contain  ${listRet}  shengqiaowei002
    ...  sqw003  &{addRet}[id]   ${suite_g7c1_classid},&{addClass}[id]
    ...  13732327439  1234@qq.com   331002199607064919

    [Teardown]  Run Keywords  deleteTeacher  &{addRet}[id]  AND
    ...  delete school class  &{addClass}[id]


    #

删除老师1-tc001081
    #删除之前列出
    ${before}=  listTeacher

    ${delRet}=  deleteTeacher  999999
    should be true  $delRet['retcode']==404
    should be true  $delRet['reason']=='id 为`999999`的老师不存在'

    #删除之后列出
    ${after}=  listTeacher

    should be equal  ${before}  ${after}

删除老师2-tc001082

    #删除之前列出
    ${before}=  listTeacher

    #先添加1个科学老师
    ${addRet}=  addTeacher  shengqiaowei002  sqw002
    ...                     ${g_subject_science_id}
    ...                     ${suite_g7c1_classid}
    ...         13732327439  1234@qq.com   331002199607064919

    should be true  $addRet['retcode']==0

    #列出老师，检验一下
    ${listRet}=  listTeacher
    ${listRet}=  evaluate  $listRet['retlist']
    teacherlist should not contain  ${listRet}  shengqiaowei002
    ...  sqw002  &{addRet}[id]   ${suite_g7c1_classid}
    ...  13732327439  1234@qq.com   331002199607064919

    #删除老师
    deleteTeacher  &{addRet}[id]

    #删除之后列出
    ${after}=  listTeacher

    should be equal  ${before}  ${after}


