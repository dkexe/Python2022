from multiprocessing.sharedctypes import Value
from sre_constants import FAILURE


class Calculator():
# trong đó có 1 method là is_event(num) (edited) 
# nếu chẵn thì return True, ngược lại return false    

    def is_even(number):

            if number%2 == 0:
                return True    
            else: 
                return False    
