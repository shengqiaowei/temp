*** Settings ***
Library  pylib/TeacherLib.py
Variables  config.py

*** Test Cases ***
添加老师1-tc001001
    ${addRet}=  addTeacher  shengqiaowei  sqw
    ...                     ${g_subject_math_id}
    ...                     ${suite_g7c1_classid}
    ...         13732327438  123@qq.com   331002199607064918

    should be true  $addRet['retcode']==0
#列出老师，检验一下
    ${listRet}=  listTeacher

    teacherlist_should_not_contain  &{listRet}[retlist]   shengqiaowei  sqw  &{addRet}[id]
    ...                             ${suite_g7c1_classid}
    ...                             13732327438  123@qq.com   331002199607064918

    [Teardown]  deleteTeacher   &{addRet}[id]


