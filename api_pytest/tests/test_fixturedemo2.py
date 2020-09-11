#fixture使用案例scope="function"
import pytest

#fixture(scope="function", params=None, autouse=False, ids=None, name=None):
#@pytest.fixture()如果不写参数，默认就是scope="function"，它的作用范围是每个测试用例来之前运行一次
#如果autouse为True，则为所有测试直接激活fixture， 无需往每个函数传入fixture就可以调用它。 如果为False（默认值），则需要往测试函数传入fixture标记的函数名
@pytest.fixture(autouse=True)
def fixture_for_func():
    print('这是fixture装饰器标记的函数')


def test_1():
    print('执行了测试用例test_1')

def test_2():
    print('执行了测试用例test_2')

def test_3(fixture_for_func):
    print('执行了测试用例test_3')

if __name__ == "__main__":
    pytest.main(["-s","-v","/python20190819/api_pytest/tests/test_fixturedemo2.py"])
    #pytest.main(["-s","-v","test_fixturedemo.py"])