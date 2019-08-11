*** Settings ***
Library  pylib/TeacherLib.py
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

