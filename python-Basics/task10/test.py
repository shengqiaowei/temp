# author: xiaxiang   time:2019/9/9

import traceback
#最常用的几种异常方式
while True:
    num = input('input a number:')
    try:
        print('100 / %s = %s' % (num,100.0/int(num)))

    #第一种比较常用的,遇到错误直接报错,打印代码错误信息
    # except Exception as e:
    #     print('异常了',e)

    #第二种比较常用的,是第一种的简写,但是不打印代码错误信息
    # except:
    #     print('异常了')

    #（最常用）第三种比较常用的,导入traceback,将错误信息打印出来,但是 不是红色报错
    except:
        print('异常了',traceback.format_exc())
