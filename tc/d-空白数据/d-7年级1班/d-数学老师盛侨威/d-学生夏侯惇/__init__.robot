*** Settings ***
Library  pylib/StudentLib.py
Variables  config.py

Suite Setup  addStudent   xiahoudun111  夏侯惇111   ${g_grade_7_id}
    ...  ${suite_g7c1_classid}  13732327438  suite_student_id


Suite Teardown    deleteStudent     ${suite_student_id}
