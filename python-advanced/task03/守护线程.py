# author: xiaxiang   time:2019/9/10

import threading
import time
'''
    1.如果只使用t1.start t2.start 程序就会等t1和t2这2个线程都结束了,程序才会退出，并且看电影代码随机穿插打印
    2.如果使用t1.join 程序就会等t1这个线程运行结束了才会去运行看电影的代码，因为将t1线程阻塞住了
    3.如果t1和t2这2个线程都使用join,2个线程都阻塞,2个线程都运行结束,才会运行看电影代码
    4.如果t1使用守护线程,会将循环次数用完,t1线程结束,t2线程会继续运行,直到t2线程循环结束
    5.如果t2使用守护线程,t1运行结束了,程序会直接结束,不需要等到t2运行结束
'''
#创建一个线程
def foo(num,numCon):
    for i in range(numCon):
        print('这是第几个线程',num, '这是第几次执行',i+1)
        time.sleep(1)
t1 = threading.Thread(target=foo,args=(1,5))
t2 = threading.Thread(target=foo,args=(2,1000))

#t1.setDaemon(True)
#t2.setDaemon(True)
t1.start()
t2.start()
#t1.join()
#t2.join()

for i in range(5):
    print('看电影')
    time.sleep(1)
print('电影结束')