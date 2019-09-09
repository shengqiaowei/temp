# author: xiaxiang   time:2019/9/7
import time
from random import randint
#定义老虎类
class Tiger:
    #定义静态属性
    className = '老虎'

    #实例属性,体重
    def __init__(self,inWeight=200):
        self.weight = inWeight

    #老虎叫,每叫1次体重减5斤
    def roar(self):
        print('wow')
        self.weight-=5

    #老虎喂食
    def feed(self,food):
        if food=='肉':
            print('喂食成功')
            self.weight+=10
        else:
            print('喂食错误')
            self.weight-=10

#定义羊类
class Sheep:
    className = '羊'
    def __init__(self,inWeight=100):
        self.weight = inWeight

    def roar(self):
        print('mie')
        self.weight-=5

    def feed(self,food):
        if food=='草':
            print('喂食成功')
            self.weight+=10
        else:
            print('喂食错误')
            self.weight-=10

#定义房间类
class Room:
    def __init__(self,num,animal):
        self.num = num
        self.animal = animal

#需要10个房间,每个房间需要1个编号和一个动物
roomList = []
#one就是房间号,使用0和1 老虎和羊的几率各是百分之50
for one in range(1,11):
    if randint(0,1):
        ani = Tiger()
    else:
        ani = Sheep()
    room = Room(one,ani)
    roomList.append(room)

#rooList是一个房间的实例
print(roomList)

#定义一个游戏开始的时间
startTime = time.time()

#使用while 循环来判断游戏结束时间
while True:
    #定义一个游戏结束时间
    endTime = time.time()
    if endTime-startTime>30:
        print('游戏结束,时间到了！')
        #游戏结束,打印每个房间的动物信息,因为是list,所以用遍历
        for one in roomList:#one是房间实例
            print('当前房间编号:{},动物是:{},体重是{}斤'.format(one.num,one.animal.className,one.animal.weight))
        break

    #获取房间号
    roomNum = randint(1,10)
    #获取房间实例,roomList是一个list,-1是因为使用下标去取值
    roomObject = roomList[roomNum-1]

    #是否需要敲门
    answer = input('当前房间编号是{},您是否需要敲门 (y/n)?'.format(roomNum).strip())
    if answer=='y':#敲门
        #敲门,动物会叫, 房间实例.动物.方法
        roomObject.animal.roar()
    #叫完之后需要喂食,将输入的参数传进来
    food = input('请投喂食物:(肉/草)?')
    roomObject.animal.feed(food)
