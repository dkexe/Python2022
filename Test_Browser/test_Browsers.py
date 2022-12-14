import pytest
from Browsers import start_Browser

data = [("https://www.google.com","appium"),("https://www.google.com","automation"),("https://www.google.com","ajdhalkdj")]

data_Chrome = [("https://www.programiz.com/","a@gmail.com","Thank you for subscribing!"),("https://www.programiz.com/","a","Thank you for subscribing!"),("https://www.programiz.com/","@gmail.com","Thank you for subscribing!"),("https://www.programiz.com/","a@gmail","Thank you for subscribing!")]
@pytest.mark.parametrize("input,expect",data)
def test_FireFox(input,expect):
    assert expect in start_Browser.start_FireFox(input)


@pytest.mark.parametrize("input,email,expect",data_Chrome)
def test_Chrome(input,email,expect):
    assert start_Browser.start_Chrome(input,email) == expect