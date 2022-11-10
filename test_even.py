from asyncio.windows_events import NULL
from Calculator import Calculator

test_Cal = Calculator

def test_even():
    assert test_Cal.is_even(5) == False
 
def test_odd():
    assert test_Cal.is_even(10) == True

def test_invalid():
    assert test_Cal.is_even('asdsdfg')

def test_zero():
    assert test_Cal.is_even(0) == True

def test_null():
    assert test_Cal.is_even()

def test_negative_even():
    assert test_Cal.is_even(-2)== True

def test_negative_odd():
    assert test_Cal.is_even(-1)== False 

