# name = 'tom'
# data = f"{{'name':{name}}}"
# print(data)


#
# 2. 程序随后将输入的学生信息分行显示，格式如下
# Jack Green :   21;
# Mike Mos   :   09;
# # 学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
studentInput = 'Jack Green ,   21  ;  Mike Mos, 9;'
if ';' in studentInput and studentInput.count(';') == studentInput.count(','):
    temp = studentInput.split(';')#根据;切,返回一个list
    del temp[-1]#删除最后一个空字符
    #print(temp)
    for one in temp:#遍历每个list
        tempList = one.split(',')#按照,切 返回2个元素
        #print(tempList)
        name = tempList[0].strip()
        age = tempList[1].strip()
        print('{:<20}:{:>02};'.format(name,age))

else:
    print('请输入正确的格式')



# 请编写一个程序)，统计出不同类型的 文件的大小总和
# 比如：
# jpeg  9988999
# json   324324
# png   2423233
resList = []#定义一个空列表用来存储最后的结果[[类型1,大小1],[类型2,大小2]
resDict = {}#定义一个空字典 {类型1:值1,类型2:值2}
with open('log.txt','r')as f:
    #获取所有行内容
    readTxt = f.read()
    #使用\n切
    linesList = readTxt.split('\n')
    #删除多余头和尾
    del linesList[0],linesList[-1]

    #对每一行进行处理
    for line in linesList:
        #按照\t切
        temp = line.split('\t')
        #获取第一个元素,只要文件类型,所以按照.再切一刀,获取最后一个元素
        fileType = temp[0].split('.')[-1].strip()
        #获取每一行文件大小,目前返回的是str类型,方便后续累加,需要强转
        fileSize = int(temp[1].strip())
        #print(fileType,fileSize)

        # #统计
        # inFlag = 0 #初始值设置为不在
        # for one in resList: #i是子列表
        #     if one[0]==fileType: #如果获取出来的类型 等于 子列表里的类型,size累加
        #         one[1] += fileSize
        #         inFlag = 1 #定义变量，表明状态
        #         break
        # # 遍历完发现没有一个匹配上，所以需要新增组合
        # if inFlag == 0:
        #     resList.append([fileType,fileSize])
#print(resList)

        if fileType in resDict: #如果键存在,就累积值
            resDict[fileType] += fileSize
        else:#如果键不存在,就创建组合
            resDict[fileType] = fileSize
print(resDict)

#求1到100的和
def get_sum(start=1,end=101):
    sumData = 0
    for i in range(start,end):
        sumData+=i
    return sumData
print(get_sum)





