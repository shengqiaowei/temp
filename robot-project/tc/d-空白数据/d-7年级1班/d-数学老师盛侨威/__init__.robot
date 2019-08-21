*** Settings ***
Library  pylib/TeacherLib.py
Variables  config.py

Suite Setup     addTeacher  shengqiaowei  sqw
    ...                     ${g_subject_math_id}
    ...                     ${suite_g7c1_classid}
    ...                     13732327438  123@qq.com   331002199607064918
    ...                     suite_math_teacher_id

Suite Teardown  deleteTeacher  ${suite_math_teacher_id}
