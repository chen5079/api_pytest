#fixture使用案例scope="session"
import pytest

# 1.上面的案例是在同一个.py文件中，多个测试用例调用一个fixture功能，如果有多个.py的文件都需要调用这个fixture功能的话，那就不能把fixture写到用例里面去了。
# 此时应该要有一个配置文件，单独管理一些预置的操作场景，pytest里面默认读取conftest.py里面的配置
# conftest.py配置需要注意以下点：
# conftest.py配置脚本名称是固定的，不能改名称
# conftest.py与运行的用例要在同一个pakage下，并且有__init__.py文件
# 不需要import导入 conftest.py，pytest用例会自动查找

# @pytest.fixture(scope="session",autouse=True)
# def fixture_for_session():
#     print('这是session的fixture')
#当加上scope="session"时，不要像function,class,module一样，和编写的测试case放在一起，我们一般放在另一个文件conftest.py下


def test_s1(): #不传
        print("用例1")
    
def test_s2(fixture_for_session):  #session在整个测试活动中开始前执行，只会被执行一次，此处传参也不会调用
        print("用例2")
    
def test_s3(fixture_for_session):
        print("用例3")

if __name__ == "__main__":
    pytest.main(["-s","-v","/python20190819/api_pytest/tests/test_fixturedemo4.py"])