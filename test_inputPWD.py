from InputPWD import inputPWD
from InputPWD_initVersion import inputPWD_init
import pytest
a = inputPWD
b = inputPWD_init
data_test = ['aas',2,3,-1,0,'',' ',',,,!@#$%$#@@@, ','aaaaaaaa','BBBBBBBB','11111111','11111111$','aaaaaaaa$','BBBBBBBB$','aaaaaaaB','12345678Ba!']
data_expected = []
for i in data_test:
    data_expected.append(True)
print(len(data_expected))
print(data_expected)
input_data = list(zip(data_test,data_expected))

data = [(' ',False),('aaaaaaaa',False),('11111111',False),('AAAAAAAA',False),('$$$$$$$$',False),('aaaaaaaa1',False),('aaaaaaaaA',False),('aaaaaaaaA1',False),('aaaaaaaaA1$',True)]

@pytest.mark.parametrize("input,expect",data)
def test_inputPWD(input,expect):
    assert a.check_input(input) == expect

def test_inputPWD_2():
    assert a.check_input('hhhhh    hhjjiiin') == True
