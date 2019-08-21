*** Settings ***
Library  pylib/StudentLib.py
Variables  config.py

*** Test Cases ***
添加学生2-tc002002
    #利用sleep 1d 停止运行1天来创建学生账号和老师账号
    #sleep  1d
    ${addRet}=  addStudent   xiahoudun2  夏侯惇2   ${g_grade_7_id}
    ...  ${suite_g7c1_classid}  13732327438

    should be true  $addRet['retcode']==0

    #列出学生，检验一下
    ${listRet}=  listStudent
    studentlist should not contain  &{listRet}[retlist]
    ...  ${suite_g7c1_classid}
    ...  xiahoudun2  夏侯惇2  13732327438
    ...  &{addRet}[id]

    [Teardown]  deleteStudent  &{addRet}[id]

删除学生2-tc002081
    #删除之前列出学生
    ${before}=  listStudent

    #添加学生
    ${addRet}=  addStudent   xiahoudun2  夏侯惇2   ${g_grade_7_id}
    ...  ${suite_g7c1_classid}  13732327438
    should be true  $addRet['retcode']==0

    #添加成功，再列出学生
    listStudent

    #删除学生
    deleteStudent  &{addRet}[id]

    #删除成功后再列出学生
    ${after}=  listStudent

    #删除前和删除后进行比较
    should be equal  ${before}  ${after}

