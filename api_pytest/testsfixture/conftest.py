import pytest
 
@pytest.fixture(scope="session")
def first():
    print("\n获取用户名,scope为session级别多个.py模块只运行一次")
    a = "yoyo"
    return a


@pytest.fixture(scope="module")
def fixture_module():
    print("这是范围是module的fixture")
    a='yoyo'
    return a

# scope="session"
# fixture为session级别是可以跨.py模块调用的,也就是当我们有多个.py文件的用例时候，如果多个用例只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里
# conftest.py文件名称是固定的，pytest会自动识别该文件。放到工程的根目录下，就可以全局调用了，如果放到某个package包下，那就只在该package内有效