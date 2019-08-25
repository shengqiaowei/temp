'''
    阻塞式调用：
        1、只有cmd运行结束了，才会执行下面代码
        2、比如输入ipconfig，会继续执行after call
        3、比如输入mspaint，必须要关掉画板，才会继续执行after call
        4、os.system具有返回值，0：成功、1：失败、2：错误
           作用：可以通过返回值判断命令是否执行成功
'''
import os
# a = os.system('ipconfig')
#如果执行成功，a返回0，失败，a返回1
#print(a)
# os.system('dir /s')#显示当前目录文件
# os.system('mspaint')#阻塞式调用
# os.system('start mspaint')#非阻塞式调用
# os.system('for %i in (1,2,10) do @echo %i')
#os.system('for /d %i in (\'C:\*\') do echo %%i')
print(os.system('cd'))#打印当前路径并且返回是否成功的数字

'''
    判断文件复制是否成功
    ret = os.system('cp /opt/a /home/a')
    if ret == 0:
        print('copy success')
    else:
        print('copy faild')
'''

'''
    subprocess和os的区别在于：
    1、os是以字符串的形式传参，直接把返回打印出来，变量接收的是返回码 0或1
    2、subprocess.check_output：是以列表传参，需要用变量接收返回，以一个字节字符串形式返回，需要解码
    3、shell=True表示是以字符串传参运行，不指定shell，默认是false
    4、check_output阻塞
    5、Popen默认非阻塞，想要阻塞，加上对象.wait()即可
'''
import subprocess
out_bytes = subprocess.check_output('dir',shell=True)
#非阻塞式，需要解码,由于是windows，所以是gbk，mac和linux都是utf8
# ret = subprocess.Popen(['ping','www.baidu.com'])
# print(ret.decode('gbk'))
# ret.wait()
# print('松勤')

#不加.wait()就是非阻塞调用，不关闭画板，python程序继续执行print('done')
#加.wait()就是阻塞调用，只有关闭画板，python程序才会继续执行print('done')
# process = subprocess.Popen(args='mspaint',shell=True).wait()
# print('done')

'''
    1、得到外部程序的输出
    2、stdout=subprocess.PIPE是指标准文件的输出也就是io输出到屏幕
    3、err只有程序出错才会打印错误信息
    4、communicate是阻塞调用
'''
popen = subprocess.Popen(
    'ping www.baidu.com',
    stdout=subprocess.PIPE,
    shell=True,
    encoding='gbk'
)
print('Popen是非阻塞调用，所以会先打印')
output,err = popen.communicate()
#output是输入，err是系统层面的报错，默认为None
print(output,err)
print('communicate是阻塞调用，所以会后打印')

popen1 = subprocess.Popen(
    'python ioTest.py',
    stdin=subprocess.PIPE,#标准输入文件
    stdout=subprocess.PIPE,#标准输出文件
    stderr=subprocess.PIPE,#标准打印对象的错误信息
    encoding='utf8',
)
inputList = ['1','2','3','4']
out1,err1 = popen1.communicate('\n'.join(inputList))#相当于换行增加列表数字进行相加
print(out1,err1)

#只有cmd执行完后才会执行after call
print('after call')