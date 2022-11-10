from Calculator import Calculator
import pytest
test_Cal = Calculator


data_test = ['aas',2,3,-1,0]
expectation = [False, True, False, False, True]
# đã thử convert sang dictionary nhưng không dùng đc, đành phải nhập bằng tay như bên dưới
# nếu tập input và expect khác nhau như ở trên
test_data = [('aaa',False ),(2,True),(3,False ),(-1,False),(0,True)]
 

@pytest.mark.parametrize(
    "input,expected", test_data)
def test_number_marker(input,expected):
    assert test_Cal.is_even(input) == expected
