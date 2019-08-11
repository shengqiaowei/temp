import requests
from pprint import pprint
from config import g_vcode
from robot.libraries.BuiltIn import BuiltIn
#将类名和文件夹定义一样即可
class SchoolClassLib:
    url = 'http://ci.ytesting.com/api/3school/school_classes'
    def __init__(self):
        self.g_vcode = g_vcode


    #列出班级
    def list_school_class(self,gradeid=None):
        if gradeid!=None:
            params = {
                'vcode':self.g_vcode,
                'action':'list_classes_by_schoolgrade',
                'gradeid':int(gradeid)
            }
        else:
            params = {
                'vcode':self.g_vcode,
                'action':'list_classes_by_schoolgrade'
            }
        response = requests.get(self.url,params=params)
        bodyDict = response.json()
        #以json形式打印response，缩进为2
        pprint(bodyDict,indent=2,)
        print('查询接口')
        return bodyDict

    #添加班级
    def add_school_class(self,grade,name,studentlimit,
                         isSaveId=None):
        payload={
            'vcode':self.g_vcode,
            'action':'add',
            'grade':int(grade),
            'name':name,
            'studentlimit':int(studentlimit)
        }
        response = requests.post(self.url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)

        #如果isSaveId传进来值，就将id保存起来
        if isSaveId!=None:
            BuiltIn().set_global_variable('${%s}'%isSaveId,bodyDict['id'])
        return bodyDict


    #删除班级
    def delete_school_class(self,classid):
        payload={
            'vcode':self.g_vcode
        }
        url = '{}/{}'.format(self.url,classid)
        response = requests.delete(url,data=payload)
        return response.json()

    #删除所有班级
    def delete_all_school_classes(self):
        #先列出所有班级
        rd = self.list_school_class()

        #删除所有班级
        for one in rd['retlist']:
            self.delete_school_class(one['id'])

        #再次列出七年级所有班级
        rd = self.list_school_class()
        pprint(rd,indent=2)

        if rd['retlist']!=[]:
            raise Exception('cannot delete all school classes!!')

    #检查点
    def classlist_should_not_contain(self,
                                         classlist,
                                         classname,
                                         gradename,
                                         invitecode,
                                         studentlimit,
                                         studentnumber,
                                         classid
                                         ):
        item = {
                "name": classname,
                "grade__name": gradename,
                "invitecode": invitecode,
                "studentlimit": int(studentlimit),
                "studentnumber": int(studentnumber),
                "id": classid,
                "teacherlist": []
            }
        #assert语法：第一个参数是正确值，第二个参数是否则抛出异常
        if item not in classlist:
            raise Exception('班级列表里面没有该班级')

    #修改班级
    def modifyClass(self,classid,name,studentlimit):
        payload= {
            'vcode':self.g_vcode,
            'action':'modify',
            'name':name,
            'studentlimit':int(studentlimit)
        }
        url = '{}/{}'.format(self.url,classid)
        response = requests.put(url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        pprint('修改班级接口')
        return bodyDict