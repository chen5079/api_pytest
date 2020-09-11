#通常情况下，读取测试数据的函数不会定义在测试用例文件中，而是会放到utils包中，比如放到utils/commonlib.py中

import yaml

def get_test_data(test_data_path):
    case=[]
    #存储测试用例名称
    http=[]
    #存储请求对象
    expected=[]
    #存储预期结果
    with open(test_data_path,encoding = 'utf-8') as f:
        dat=yaml.load(f.read(),Loader=yaml.SafeLoader)
        test=dat['tests']
        print(test)
        print('........................')
        for td in test:
            case.append(td.get("case",''))
            http.append(td.get('http',{}))
            expected.append(td.get('expected',{}))
    # print(http)
    # print(expected)
    # print('XXXXXXXXXXXXXXXXXX')
    # return case,http,expected

    parameters=zip(case,http,expected)
        #把三个列表糅合在一起
    return case,parameters