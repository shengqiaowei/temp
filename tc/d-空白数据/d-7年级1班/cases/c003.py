from pylib.SchoolClassLib import SchoolClassLib
sc = SchoolClassLib()

class c003:
    def steps(self):
        print('''\n\n***** step 1 ****  添加 7年级1班 \n''')

        #添加前查询一次
        listBefore = sc.list_school_class()

        #添加系统存在的班级
        self.ret1 = sc.add_school_class(1,'1班',60)
        if self.ret1['retcode']!=1:
            raise Exception('返回值非1')

        #添加后查询一次
        listAfter = sc.list_school_class()

        #判断是否相等
        assert listBefore==listAfter,'添加前后值不相等'



    def setup(self):
        pass

    def teardown(self):
        pass
