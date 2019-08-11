import requests,json
from pprint import pprint
from config import g_vcode
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
class TeacherLib:
    url = 'http://ci.ytesting.com/api/3school/teachers'
    def __init__(self):
        self.g_vcode = g_vcode

    #列出老师
    def listTeacher(self,subjectid=None):
        if subjectid:
            parmas={
                'vcode':self.g_vcode,
                'action':'search_with_pagenation',
            }
        else:
            parmas={
                'vcode':self.g_vcode,
                'action':'search_with_pagenation',
                'subjectid':subjectid
            }
        response = requests.get(self.url,params=parmas)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict

    #添加老师
    def addTeacher(self,
                   username,
                   realname,
                   subjectid,
                   classlist,
                   phonenumber,
                   email,
                   idcardnumber,
                   isSaveName=None):
        #dumps：将python的数据对象转换成字符串
        #loads：将字符串转换成python的数据对象

        #如果传入的班级号只有1个，强转为字符串，用,分隔
        tempList = str(classlist).split(',')
        #使用列表生成式，将传入的班级号转成列表形式的字典
        newClassList = [{'id':oneid}  for oneid in tempList if oneid!='']

        payload={
            'vcode':self.g_vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'subjectid':int(subjectid),
            'classlist':json.dumps(newClassList),
            'phonenumber':phonenumber,
            'email':email,
            'idcardnumber':idcardnumber
        }
        response = requests.post(self.url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        #如果isSaveName传进来值，就将id保存起来
        if isSaveName!=None:
            BuiltIn().set_global_variable('${%s}'%isSaveName,bodyDict['id'])
        return bodyDict

    #修改老师
    def modifyTeacher(self,teacherid,
                      realname=None,
                      subjectid=None,
                      classlist=None,
                      phonenumber=None,
                      email=None,
                      idcardnumber=None):
        payload={
            'vcode':self.g_vcode,
            'action':'modify'
        }
        if realname is not None:
            payload['realname']=realname
        if subjectid is not None:
            payload['subjectid']=subjectid
        if phonenumber is not None:
            payload['phonenumber']=phonenumber
        if email is not None:
            payload['email']=email
        if idcardnumber is not None:
            payload['idcardnumber']=idcardnumber


        if classlist is not None:
            tempList = str(classlist).split(',')
            newClassList = [{'id': oneid} for oneid in tempList if oneid != '']
            payload['classlist']=json.dumps(newClassList)

        url = '{}/{}'.format(self.url,teacherid)

        response = requests.put(url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict

    #删除老师
    def deleteTeacher(self,teacherid):

        payload = {
            'vcode'  : self.g_vcode,
        }

        url = '{}/{}'.format(self.url,teacherid)
        response = requests.delete(url,data=payload)


        bodyDict = response.json()
        pprint (bodyDict,indent=2)

        return bodyDict


    #删除所有老师
    def deleteAllTeacher(self):
        # 列出所有老师
        rd =  self.listTeacher()
        if rd['retcode'] != 0:
            raise Exception('cannot list teachers!!')

        # 删除列出的所有老师
        for one in rd['retlist']:
            self.deleteTeacher(one['id'])

        #再列出所有老师
        rd =  self.listTeacher()

        # 如果没有删除干净，通过异常报错给RF
        if rd['retlist'] != []:
            raise  Exception("cannot delete allteachers!!")

    #检查点
    def teacherlist_should_not_contain(self,
                                       teacherlist,
                                       username,
                                       realname,
                                       teacherid,
                                       classlist,
                                       phonenumber,
                                       email,
                                       idcardnumber,):
        #如果输入1个classlist，也转成str
        teachclasslist = str(classlist)

        item={
            'username':username,
            'realname': realname,
            'id': int(teacherid),
            'teachclasslist':[int(oneid) for oneid in teachclasslist.split(',')],
            'phonenumber':phonenumber,
            'email':email,
            'idcardnumber':idcardnumber
        }
        pprint(item)
        print('---------')
        pprint(teachclasslist)

        if item not in teacherlist:
            raise Exception('老师列表里面没有该老师')

# if __name__=='__main__':
#     tl = TeacherLib()
#     tl.listTeacher()
