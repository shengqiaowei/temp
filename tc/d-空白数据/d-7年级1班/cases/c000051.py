from SchoolClassLib import SchoolClassLib
sc = SchoolClassLib()

class c000051:
    def steps(self):
        print('''\n\n***** step 1 ****  修改班级名字，不重名 \n''')

        #添加一个班级
        self.ret = sc.add_school_class(1,'2班',60)
        assert self.ret['retcode']==0,'添加失败'
        classid = self.ret['id']

        #修改班级名字
        modifyRet = sc.modifyClass(classid,'22班',60)
        assert modifyRet['retcode'] == 0, '添加失败'

        print('''\n\n***** step 2 ****  列出班级，检验一下\n''')

        listRet2 = sc.list_school_class(1)
        sc.classlist_should_not_contain(listRet2['retlist'],
                                        '22班',
                                        '七年级',
                                        self.ret['invitecode'],
                                        60,
                                        0,
                                        self.ret['id'])






    def setup(self):
        pass
    def teardown(self):
        sc.delete_school_class(self.ret['id'])