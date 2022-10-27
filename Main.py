from HinhHoc import Rectangle
from SoHoc import SoHoc
from NhanVien import NhanVien

def main():

    choice = selector()
    # print("Value of choice =",choice)
    execute_Assignment(choice)
def selector():
    while True:
        print ("Select your assignment: ")
        print(" 1. Rectangle")
        print(" 2. Numbers")
        print(" 3. Staff")
        try:
            choice = ()
            choice = input("Please enter: ")   
            if choice[0] >= "1" and choice[0] <= "3" and len(choice) == 1 :
                break
            print("Please select your choice again, current choice = ", choice)
            print()
        except IndexError:
            print("Invalid input")
    return choice
def execute_Assignment(x):

    for i in x:
        if i == "1": # Value is String not int, so it should be compared with string text

            target = Rectangle()
            target.inputLW()
            target.get_Area_Perimeter_Value()
            break
        elif i == "2":
            target = SoHoc()
            target.inputInfo()
            # target.printInfo()
            while True:
                try:
                    print("Select method: ")
                    print ("#1 addition() - #2 subtract() - #3 multi() - #4 division() - #0 exit")
                    # choice = ()
                    choice = input("=> ")
                    if choice[0] >= "0" and choice[0] <= "4" and len(choice) == 1:
                        if choice[0] == "0":
                            break
                        elif choice[0] == "1":
                            target.addition()
                            
                        elif choice[0] == "2":
                            target.subtract()
                            
                        elif choice[0] == "3":
                            target.multi()
                            
                        elif choice[0] == "4":
                            target.division()    
                    else: 
                        print("Choice must be, between 0-4, not ", choice + ".")
                        print ()

                    print()
                except IndexError:
                    print("Try again")
                except KeyboardInterrupt:
                    break
        elif i == "3":
            target = NhanVien()
            target.inputNV()
            while True:
                try:
                    print("Select options:  #1 - printinfo() - #2 tinhThuong() #3 - exit")
                    choice = input("=> ")
                    if choice[0] >="1" and choice[0] <= "3" and len(choice[0])==1:
                        if choice[0] =="1":
                            print("Print info: ")
                            target.printInfo()
                        elif choice[0] =="2":
                            print("Tính Thuởng: ")
                            target.tinhthuongNV()     
                        elif choice[0] =="3":
                            print("Exit.")
                            break  
                    print("Please select a valid option...")    
                    print()
                except IndexError:
                    print("Try again.")    

    print()




main() 