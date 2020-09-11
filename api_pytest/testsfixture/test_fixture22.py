import pytest
 
def test_2(first):
    '''用例传fixture'''
    print("测试账号：%s" % first)
    assert first == "yoyo"
 
if __name__ == "__main__":
    pytest.main(["-s", "/python20190819/api_pytest/testsfixture/test_fixture22.py"])