*** Settings ***
#对这个测试文件下的所有测试用例都打上标签
Force Tags  login  冒烟测试
#如果用例自身有标签则使用自身标签，如果没有，则使用默认标签
Default Tags   notag

*** Test Cases ***
测试用例-10001
    [Tags]  正确用户名  正确密码  10001
    log to console  用例10001主体部分

测试用例-10002
    [Tags]  正确用户名  正确密码  10002
    log to console  用例10002主体部分

测试用例-10003
    [Tags]  正确用户名  错误密码  10003
    log to console  用例10003主体部分

测试用例-10004
    log to console  用例10004主体部分
    #fail是指这条用例会执行失败
    Fail