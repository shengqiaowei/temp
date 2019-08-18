*** Settings ***
Library  pylib/WebOpLib.py
Library  pylib/TeacherLib.py
Library  pylib/StudentLib.py
Variables  config.py

*** Test Cases ***
老师登录1-tc005001

    #添加老师
    ${addRet}=  addTeacher  shengqiaowei001  sqw001
    ...                     ${g_subject_math_id}
    ...                     ${suite_g7c1_classid}
    ...                     13732327438  123@qq.com   331002199607064918

    teacher login  shengqiaowei001  888888

    ${teacherInformation}=  get_teacher_homepage_info

    should be true  $teacherInformation==['松勤学院00602', 'sqw001', '初中数学', '0', '0', '0']

    ${classStudent}=  get_teacher_class_students_info

    should be true  $classStudent=={'七年级1班': []}

    [Teardown]   deleteTeacher  &{addRet}[id]

学生登录1-tc005081
    #添加学生
        ${addRet}=  addStudent   xiahoudun2  夏侯惇2   ${g_grade_7_id}
    ...  ${suite_g7c1_classid}  13732327438

    should be true  $addRet['retcode']==0

    #学生登录
    student login  xiahoudun2  888888

    #获取学生主页信息
    ${studentInfo}=  get_student_homepage_info
    should be true  $studentInfo==['夏侯惇2', '松勤学院00602', '0', '0']

    #获取错题库信息
    ${studentWrong}=  student_wrong
    should be true  $studentWrong=='您尚未有错题入库哦'
    [Teardown]   deleteStudent  &{addRet}[id]



