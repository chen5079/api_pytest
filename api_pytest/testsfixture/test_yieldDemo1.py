#使用yield关键字实现teardown_xxx的功能
#如果其中一个用例出现异常，不影响yield后面的teardown执行,运行结果互不影响，并且在用例全部执行完之后，会呼唤teardown的内容
import pytest
 
# 此时，open函数是一个测试固件，相当于实现了setup_xxx&teardown_xxx的功能。
#fixture里面的teardown用yield来唤醒teardown的执行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")
    yield
    print("执行teardown!")
    print("最后关闭浏览器")

def test_s1(open):
    print("用例1：搜索python-1")

def test_s2(open):  # 不传login
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")



