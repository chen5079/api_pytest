#fixture为module级别时，在当前.py脚本里面所有用例开始前只执行一次
import pytest
@pytest.fixture(scope="module")
def fixture_module():
    print("这是范围是module的fixture")
    a='yoyo'
    return a

def test_1(fixture_module): #传参fixture_module
    '''用例传fixture'''
    print("测试账号：%s" % fixture_module)
    assert fixture_module == "yoyo"
 
class TestCase():
    def test_2(self, fixture_module): #传参fixture_module
        '''用例传fixture'''
        print("测试账号：%s" % fixture_module)
        assert fixture_module == "yoyo"
 
if __name__ == "__main__":
    pytest.main(["-vs", "/python20190819/api_pytest/testsfixture/test_fixturemodule.py"])