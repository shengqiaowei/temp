userInput = input('请输入您的手机号码:')

phone1 = [131,132,133]#移动
phone2 = [141,142,143]#联通
phone3 = [151,152,153]#电信

if  len(userInput) == 11:
    if userInput.isdigit():
        temp = int(userInput[:3])
        if temp in phone1:
            print('移动号码')
        elif temp in phone2:
            print('联通号码')
        elif temp in phone3:
            print('电信号码')
        else:
            print('手机号输入错误')
    else:
        print('非法字符')
else:
    print('手机号位数错误')





