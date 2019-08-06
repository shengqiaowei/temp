from pylib.SchoolClassLib import SchoolClassLib
sc = SchoolClassLib()

class c002:
    def steps(self):
        print('''\n\n***** step 1 ****  添加 7年级2班 \n''')
        self.ret1 = sc.add_school_class(1,'2班','60')
        assert self.ret1['retcode']==0,'添加失败'

        print('''\n\n***** step 2 ****  列出班级，检验一下\n''')

        ret2 = sc.list_school_class(1)
        sc.classlist_should_contain(ret2['retlist'],
                                    '2班',
                                    '七年级',
                                    self.ret1['invitecode'],
                                    60,
                                    0,
                                    self.ret1['id'])
    #用例自身初始化
    def setup(self):
        pass

    #用例自身结束后删除数据
    def teardown(self):
        sc.delete_school_class(self.ret1['id'])
