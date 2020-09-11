#使用yield关键字实现teardown_xxx的功能

import pytest
 
# 此时，login函数是一个测试固件，相当于实现了setup_xxx&teardown_xxx的功能。
@pytest.fixture()
def login():
    ############# 以下的代码相当于setup部分 ###########
    print('登录系统')
    token = 'a1b23c'
    yield token
    ############# 以下的代码相当于teardown部分 ###########
    print('退出登录')
 
# 在测试函数里, 通过形参声明要使用的测试固件
def test1(login):
    # login参数的值是测试固件函数的返回值
    print('in test1: ', login)
    print('测试1')
 
def test2(login):
    print('in test2: ', login)
    print('测试2')