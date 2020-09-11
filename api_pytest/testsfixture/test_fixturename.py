#使用装饰器@pytest.fixture()的name参数，指定测试固件的名字。
#fixture(scope="function", params=None, autouse=False, ids=None, name=None):
import pytest
 
# 给装饰的测试函数重新命名为driver，如果不命名，默认login
@pytest.fixture(name = "driver")
def login():
    print('登录系统')
    token = 'a1b23c'
    yield token
    print('退出登录')
 
def test1(driver): #driver代替了login
    print('in test1: ', driver)
    print('测试1')
 
def test2(driver):
    print('in test2: ', driver)
    print('测试2')

#通过装饰器@pytest.fixture()的参数params，实现测试固件的参数化。
@pytest.fixture(params=['tom', 'jack'])
def login1(request):
    print('%s登录' % request.param)
 
def test_1(login1):
    print('执行测试1')
 
 
# 执行结果：
# setup_demo.py::test1[tom] tom登录
# 执行测试1
# PASSED
# setup_demo.py::test1[jack] jack登录
# 执行测试1
# PASSED

 
@pytest.fixture(params=[('tom', '123'), ('jack', '1234')])
def login2(request):
    user = request.param[0]
    passwd = request.param[1]
    print('登录系统: 用户名%s, 密码%s' %(user, passwd))
 
def test_2(login2):
    print('test 2')

# 执行结果：
# test_fixturename.py::test_1[tom] tom登录  # 测试用例的id是tom
# 执行测试1
# PASSED
# test_fixturename.py::test_1[jack] jack登录
# 执行测试1
# PASSED
# test_fixturename.py::test_2[login20] 登录系统: 用户名tom, 密码123   # 测试用例的id是login20
# test 2
# PASSED
# test_fixturename.py::test_2[login21] 登录系统: 用户名jack, 密码1234
# test 2

# 可以通过装饰器@pytest.fixture()的参数ids，设置测试用例的id。
@pytest.fixture(params=[('tom', '123'), ('jack', '1234')],
                ids=['user_a', 'user_b'])  # 这两个列表里，元素的数目要匹配
def login3(request):
    user = request.param[0]
    passwd = request.param[1]
    print('登录系统: 用户名%s, 密码%s' %(user, passwd))
 
def test3(login3):
    print('test 3')

#执行结果：
# test_fixturename.py::test3[user_a] 登录系统: 用户名tom, 密码123  #测试用例的id是user_a
# test 3
# PASSED
# test_fixturename.py::test3[user_b] 登录系统: 用户名jack, 密码1234
# test 3
# PASSED