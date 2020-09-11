#如果其中一个用例出现异常，不影响yield后面的teardown执行,运行结果互不影响，并且在用例全部执行完之后，会呼唤teardown的内容
#如果测试用例中的代码出现异常或者断言失败，并不会影响他的固件中yield后的代码执行；
# 但是如果固件中的yield之前的代码也就是相当于setup部分的带代码，出现错误或断言失败，那么yield后的代码将不会再执行，当然测试用例中的代码也不会执行。
import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")
    yield
    print("执行teardown!")
    print("最后关闭浏览器")
@pytest.mark.xfail()
def test_s1(open):
    print("用例1：搜索python-1")

    # 如果第一个用例异常了，不影响其他的用例执行
    raise NameError  # 模拟异常

def test_s2(open):  # 不传login
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")