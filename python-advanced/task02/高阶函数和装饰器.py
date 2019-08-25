'''
    高阶函数
'''
#函数名作为参数
# def foo(func):
#     print('foo')
#     return func()
# def bar():
#     print('bar')
# foo(bar)

#函数名作为返回值
def foo():
    print('foo')
    return bar
def bar():
    print('bar')
b = foo()
b()

'''
    闭包 
        概念：调用局部变量,但是 不是全局变量,以下例子：a是全局变量,x是局部变量
    	作用：延长了变量的生命周期
        1、第一种运行方式:outer()()
        先运行outer()函数，会返回innner，注意只是返回，函数后面没加()不会执行函数,
        在outer()后面在加一层()也就是运行inner函数
        2、第二种运行方式:f = outer() f()
        先把outer()赋值给变量，变量在加()也就是运行inner函数
'''
a = 20
def outer():
    x = 10
    def inner():
        print(x)
    return inner

outer()()#10
f = outer()
f()#10



import time

'''
    需求：查看foo()函数的接口的执行时间功能,使用装饰器完成
         以下方式就是使用不改变原先代码,并且同样不改变调用方式增加功能
        1.传入可变长度的参数
'''
def bar1(func):
    def inner(*args,**kwargs):
        begin = time.time()
        print(begin)
        func(*args,**kwargs)
        end = time.time()
        print(end)
        print('响应时间:',end-begin)
        return inner

@bar1 # foo = bar(foo)
def foo(user):
    print('执行者:%s 执行测试用例' % user)
    time.sleep(1)
#foo = bar(foo) #foo == inner
foo('张三')

'''
    高级装饰器：
        1.带参数的装饰器
        2.高级装饰器和上面装饰器的区别：高级装饰器多出了装饰器带参数
'''
def calu(tps):
    def bar(func):
        def inner(*args,**kwargs):
            begin = time.time()
            print(begin)
            func(*args,**kwargs)
            end = time.time()
            print(end)
            print('tps:',tps/(end-begin))
        return inner
    return bar

@calu(100)
def foo(user):
    print('执行者:%s 执行测试用例' % user)
    time.sleep(1)
#foo()


