# include uppercases,
# include lowercases,
# len >= 8
# include number
# include special chars

from curses.ascii import isupper
from logging import exception
from optparse import check_builtin


class inputPWD_init:
    def __init__(self,user_input =""):
        self.user_input = user_input
    def inputPWD(self):
        while True:
            try:
                self.user_input = input("Enter password: ")
                self.check_input()
            except TypeError:
                print("Try again.")    
            else:
                print()
                break

    
    def check_input(self):

                if len(str(self.user_input)) < 8:
                    raise exception ("Password should be equal or more than 8 characters long")
                    
                else:
                    # An alphanumeric string is a string that contains only alphabets from a-z, A-Z and some numbers from 0-9
                    # Check chuỗi string có phải là chuỗi alphanumeric hay ko, nếu trả về true, tức là ko chứa kí tự đặc biệt
                    if self.user_input.isalnum() == True:
                        raise exception ("Your password need include at least 1 special character ")
                    elif any(x.isupper() for x in self.user_input) ==False: #Nếu 1 kí tự trong input ko phải là upper case => báo lỗi
                        raise exception ("Your password need contains 1 uppper letter")
                    elif any(y.islower() for y in self.user_input) == False: #Nếu 1 kí tự trong input ko phải là lower case => báo lỗi
                        raise exception ("Your password need contains 1 lower letter")
                    elif any(z.isnumeric() for z in self.user_input) == False: #Nếu 1 kí tự trong input ko phải là number => báo lỗi
                        raise exception ("Your password need contains 1 number")        
                return True        
     





# a = inputPWD_init()
# a.inputPWD()