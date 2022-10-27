#2 Tạo class SoHoc
# number1, number2
# init
# inputInfo() - printInfo() - addition() - subtract() - multi() - division()



from logging import exception


class SoHoc():
    number1 = 0
    number2 = 0
    def __init__(self,number1 = 0,number2 = 0):
        self.number1 = number1
        self.number2 = number2
    
    def inputInfo(self):
        while True:
            try:
                self.number1= input("Input the first number: ")
                self.number2= input("Input the second number: ")
                self.check_input()
            except ValueError:
                print("Input is not a value...")
            except TypeError:
                print("Please input again...")
            else:
                print()
                break    
    def check_input(self):
        self.number1 = float(self.number1)
        self.number2 = float(self.number2)
        if self.number1 == 0 or self.number2 == 0:
            raise exception ("Value cannot be zero")
        else:
            print()


    def printInfo(self):
        print("The first value is = ", self.number1)
        print("The second value is = ", self.number2)

    def addition(self):
        print("The Addition value = ", self.number1 + self.number2)
        
    def subtract(self):
        print("The Subtract value = ", self.number1 - self.number2) 
    def multi(self):
        print("The Multiply value = ", self.number1 * self.number2)    
    def division(self):
        print("The Division value = ", self.number1 / self.number2)    

# xy = SoHoc()
# xy.printInfo()
# xy.inputInfo()
# xy.printInfo()
# xy.addition()
# xy.subtract()
# xy.multi()
# xy.division()

