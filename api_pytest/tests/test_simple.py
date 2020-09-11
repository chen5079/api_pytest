#写一个用例 test_simple.py，获取到对应的host并打印出来
#测试执行前，会自动执行一次，conftest.py文件中fixture标记的函数env()
class Test_simple(object):

    def testMyInfo(self,env):
        host = env["host"]["api"]
        print("api的host地址："+host)
