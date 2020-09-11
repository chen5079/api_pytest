#使用request.addfinalizer()注册清理函数
#我们也可以通过request.addfinalizer()的方式实现“teardown”。它和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，
# 它都会执行（关于这一点我还没有演示出来，感觉setup中如果有异常addfinalizer依然不会执行，希望大佬指导）；此外它还支持传入多个函数。
#上例子：我们在固件中传入request参数；又在固件中定义了一个内置函数；最后将定义的内置函数添加到request的addfinalizer中。
import pytest
 
# login函数是一个测试固件，相当于实现了setup_xxx&teardown_xxx的功能
@pytest.fixture()
# 声明使用request测试固件
def login(request):
    print('登录系统')
    token = 'a1b23c'
    # 定义一个清理函数, 清理函数向相当于teardown_xxx
    def fin():
        print('退出登录')
        assert 1==2 #teardown部分报异常也不影响，request.addfinalizer(fin)还是会执行这个函数
    # 注册一个清理函数
    request.addfinalizer(fin)
    # 注册完清理函数后，如果在测试固件里抛出异常,只有清理函数照常执行
    # 1 / 0
    return token
@pytest.mark.xfail() 
def test_1(login):
    print('in test1: ', login)
    print('测试1')
@pytest.mark.xfail()
def test_2(login):
    print('in test2: ', login)
    print('测试2')