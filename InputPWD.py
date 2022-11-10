# include uppercases,
# include lowercases,
# len >= 8
# include number
# include special chars

from curses.ascii import isupper
from logging import exception
from multiprocessing.sharedctypes import Value
from optparse import check_builtin


class inputPWD:
    def inputPWD():
        while True:
            try:
                user_input = input("Enter password: ")
                inputPWD.check_input(user_input)
            except ValueError:
                print("Try again.")
            except TypeError:
                print("Input again.")
            else:
                print()
                break

    def check_input(user_input):
        if len(str(user_input)) < 8:
            return False


        else:
            if user_input.isalnum() == True:
                return False
            elif any(x.isupper() for x in user_input) == False:
                return False

            elif any(y.islower() for y in user_input) == False:
                return False


            elif any(z.isnumeric() for z in user_input) == False:
                return False
            else:

                return True


# a = inputPWD
# a.inputPWD()
