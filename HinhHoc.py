#1 Dựng lớp Rectangle - dài, rộng, tính diện tích, chu vi
# Length, Width
# The Area A = L x W
# The Perimeter P = (L+W)X2




from logging import exception



class Rectangle():
    input_1 = 0
    input_2 = 0
    def __init__(self,Length = 0,Width = 0):
        self.Length = Length
        self.Width = Width
    def inputLW(self):
        while True:
            try:
                self.Length = input("Please provide the Length = ")
                self.Width = input("Please provide the Width = ")
                self.check_input()
            except ValueError:      
                print("Input is not a value...")
            except TypeError:
                print("Please input again")
            else:
                print("User inputted Length =",self.Length,", Width =",self.Width)
                break
            
        

    def check_input(self):
        self.input_1 = float(self.Length)
        self.input_2 = float(self.Width)
        if self.input_1 < 0 or self.input_2 < 0:
            raise exception ("Number cannot be a negative value...")
        else: 
            if self.input_1 == 0 or self.input_2 == 0:
                raise exception ("Number cannot be zero...")        

        
    def get_Area_Perimeter_Value(self):

        A = self.input_1 * self.input_2
        P =  2 * (self.input_1 + self.input_2)
        print("The Area value calculate by the given input = ", A)
        print("The Perimeter value calculate by the given input = ", P)    

# hinhhoc = Rectangle()
# hinhhoc.inputLW()
# hinhhoc.get_Area_Perimeter_Value()