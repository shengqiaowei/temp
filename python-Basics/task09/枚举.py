# author: xiaxiang   time:2019/9/9

'''
    枚举的作用：
        1.可以获取一个列表的值,并且打印它的下标,使用元组的形式展示
'''
alist = [1,2,3,4,'a','b']
#获取 元组, 下标和值, 使用一个变量接收
for one in enumerate(alist):
    print(one)

#使用2个变量接收
for idx,value in enumerate(alist):
    print('下标为{},  值为{}'.format(idx,value))
    #print(type(idx),type(value))