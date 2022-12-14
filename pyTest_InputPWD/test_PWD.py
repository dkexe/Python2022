from check_PWD import check_PWD
import pytest
data = [(' ',False),('aaaaaaaa',False),('11111111',False),('AAAAAAAA',False),('$$$$$$$$',False),('aaaaaaaa1',False),('aaaaaaaaA',False),('aaaaaaaaA1',False),('aaaaaaaaA1$',True)]

@pytest.mark.parametrize("input,expect",data)
def test_check_pwd(input,expect):
    assert check_PWD.check_input(input) == expect