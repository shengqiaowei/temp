import os
#print(os.system('ifconfig')) #相当于操作cmd或者shell

print(os.getcwd())#获取当前目录
a = os.path.dirname(os.getcwd())#获取当前目录的上一级目录
print(a)

print(os.listdir()) #列出当前目录下所有文件
#列出baotuwang下所以的文件
print(os.listdir('/Users/shengqiaowei/PycharmProjects/temp/baotuwang'))
#os.remove('11111.txt') #删除一个文件
os.stat('file1.txt') #获取文件的所有属性
os.chmod('file1.txt',777)#修改文件权限
#os.rmdir('task09')#删除目录
#os.removedirs(r'c:\python') 删除多个目录
#os.exit() #结束当前进程
listDir = os.path.split('/Users/shengqiaowei/'
                        'PycharmProjects/temp/python-Basics/task07')
print(listDir)#返回一个路径的目录名和文件名，返回一个元组
print(listDir[:2])

print(os.path.isfile('file1.txt'))#True 检验是否是文件
print(os.path.isdir('task09'))#True 检验是否是文件

#判断文件路径是否存在
if not os.path.exists('task10'):
    os.mkdir('task10')

print(os.curdir)#返回当前目录.

# os.chdir('../')#改变工作目录，切换到上一层目录
# print(os.getcwd())#返回当前工作目录，成功切换到上一层目录

print(os.path.getsize('file1.txt'))#返回文件大小
print(os.path.abspath('file1.txt'))#返回文件的绝对路径
#判断是否为绝对路径
print(os.path.isabs('/Users/shengqiaowei/'
                    'PycharmProjects/temp/python-Basics/task07/file1.txt'))

print(os.path.splitext('file1.txt'))#分离文件名和扩展名，返回元组('file1', '.txt')
#将目录和文件或者文件夹进行拼接
print(os.path.join('/Users/shengqiaowei/'
                    'PycharmProjects/temp/python-Basics','task10'))
#返回文件名 python-Basics
print(os.path.basename('/Users/shengqiaowei/'
                    'PycharmProjects/temp/python-Basics'))

#返回文件路径
print(os.path.dirname('/Users/shengqiaowei/'
                    'PycharmProjects/temp/'))

