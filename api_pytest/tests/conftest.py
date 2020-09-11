# 获取参数化数据的函数，模块下的用例执行时，会自动读取conftest.py文件中的数据
import pytest
import yaml
import os
#定义一个fixture标记的函数env，scope="session" 表示这个fixture函数的作用域是session级别的，在整个测试活动中开始前执行，并且只会被执行一次
#conftest.py文件中的函数只在conftest.py所在目录及其子目录中的测试活动生效
@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir, 
                               "config", 
                               "test", 
                               "config.yaml")
    #os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径,D:\python20190819\api_pytest\config\test\config.yaml
    #request.config.rootdir属性，这个属性表示的是pytest.ini这个配置文件所在的目录,D:\python20190819\api_pytest\
    #注意：当根目录下没有pytest.ini配置文件时，会默认指向conftest.py所在目录；此时要指向项目根目录，则在项目目录下新建一个 pytest.ini 空文件即可
    with open(config_path,encoding='utf-8') as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
        #读取路径中的config.yaml文件中的数据
    return env_config

@pytest.fixture(scope="session",autouse=True)
def fixture_for_session():
    print('这是session的fixture')
#当加上scope="session"时，不要像function,class,module一样，和编写的测试case放在一起，我们一般放在文件conftest.py下
