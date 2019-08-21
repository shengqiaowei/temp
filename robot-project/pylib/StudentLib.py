import requests,json
from pprint import pprint
from config import g_vcode
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
class StudentLib:
    url = 'http://ci.ytesting.com/api/3school/students'
    def __init__(self):
        self.g_vcode = g_vcode

    #列出学生
    def listStudent(self,subjectid=None):
        parmas={
                'vcode':self.g_vcode,
                'action':'search_with_pagenation',
            }

        response = requests.get(self.url,params=parmas)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict

    #添加学生
    def addStudent(self,
                   username,
                   realname,
                   gradeid,
                   classid,
                   phonenumber,
                   isSaveName=None):

        payload={
            'vcode':self.g_vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'gradeid':gradeid,
            'classid':classid,
            'phonenumber':phonenumber
        }
        response = requests.post(self.url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        #如果isSaveName传进来值，就将id保存起来
        if isSaveName!=None:
            BuiltIn().set_global_variable('${%s}'%isSaveName,bodyDict['id'])
        return bodyDict

    #修改学生
    def modifyStudent(self,studentid,
                      realname=None,
                      phonenumber=None,):
        payload={
            'vcode':self.g_vcode,
            'action':'modify'
        }
        if realname is not None:
            payload['realname']=realname

        if phonenumber is not None:
            payload['phonenumber']=phonenumber

        url = '{}/{}'.format(self.url,studentid)

        response = requests.put(url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict

    #删除学生
    def deleteStudent(self,studentid):

        payload = {
            'vcode'  : self.g_vcode,
        }

        url = '{}/{}'.format(self.url,studentid)
        response = requests.delete(url,data=payload)


        bodyDict = response.json()
        pprint (bodyDict,indent=2)

        return bodyDict


    #删除所有学生
    def deleteAllStudent(self):
        # 列出所有学生
        rd =  self.listStudent()
        if rd['retcode'] != 0:
            raise Exception('cannot list teachers!!')

        # 删除列出的所有学生
        for one in rd['retlist']:
            self.deleteStudent(one['id'])

        #再列出所有学生
        rd =  self.listStudent()

        # 如果没有删除干净，通过异常报错给RF
        if rd['retlist'] != []:
            raise  Exception("cannot delete allteachers!!")

    #检查点
    def studentlist_should_not_contain(self,
                                       studentlist,
                                       classid,
                                       username,
                                       realname,
                                       phonenumber,
                                       studentid,):
        #传到rf去会自动转成str，所以要int转换
        item={
            "classid": int(classid),
            "username": username,
            "realname": realname,
            "phonenumber": phonenumber,
            "id": int(studentid)
        }

        if item not in studentlist:
            raise Exception('老师列表里面没有该老师')

# if __name__=='__main__':
#     sl = StudentLib()
#     sl.listStudent()
#     sl.addStudent('sqw','盛侨威',1,199,13732327438)
#     sl.modifyStudent(1)
#     sl.deleteStudent(1)
