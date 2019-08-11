*** Settings ***
Library  pylib/StudentLib.py
Variables  config.py

*** Test Cases ***
添加学生1-tc002001
    ${addRet}=  addStudent  shengqiaowei100  盛侨威   ${g_grade_7_id}
    ...  ${suite_g7c1_classid}  13732327438

    should be true  $addRet['retcode']==0

    #列出学生，检验一下
    ${listRet}=  listStudent
    studentlist should not contain  &{listRet}[retlist]
    ...  ${suite_g7c1_classid}  shengqiaowei100  盛侨威
    ...  13732327438  &{addRet}[id]

    [Teardown]  deleteStudent  &{addRet}[id]