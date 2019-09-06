import pprint
import json

# def func():
#     print('1')
#     print('2')
#     print('3')

fileDir = 'file1.txt'
def putInfoToDict(fileName):
    resDict = {}
    with open(fileName,'r') as f:
        #读所有信息,并且根据\n切
        liens = f.read().splitlines()
        #print(liens)
        #遍历，针对每行进行处理
        for line in liens:
            #根据,号切
            temp = line.split(',')
            #print(temp)

            #获取课程id
            lessonId = int(temp[1].strip())

            #获取学生的id
            studentId = int(temp[2].split(')')[0].strip())

            #获取签到时间
            checkTime = temp[0].split('(')[1].replace("'",'')

            #排版
            toAdd = {'lessonId':lessonId,
                     'checkTime':checkTime}
            #print(toAdd)

            #判断键是否在字典里，不在的话增加键值对
            if studentId not in resDict:
                resDict[studentId] = [toAdd]
            #如果键存在字典里，就增加值
            else:
                resDict[studentId].append(toAdd)
    return resDict

res = putInfoToDict(fileDir)

#print(json.dumps(res,indent=1))

pprint.pprint(res)