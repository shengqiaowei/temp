with open('utf8编码.txt','r',encoding='utf8') as f1,open('gbk编码.txt','r',encoding='gbk') as f2:
    utf8Red = f1.read()
    gbkRed = f2.read()

    #合并到新的字符串
    newStr = utf8Red + '\t'  +  gbkRed
    print(newStr)

output = input('请输入新的文件夹名称：')
with open(output,'w',encoding='utf8') as w1:
    w1.write(newStr)