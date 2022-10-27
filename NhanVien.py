#3 viết class NhanVien
# + Tên + Tuôi + Địa chỉ + Tiền lương + Tổng số giờ làm
# inputinfo () printinfo() tinhThuong()
# - inputinfo () : Nhâp các thông tin cho nhân viên tùr bàn phím
# - printinfo() : In ra tât cà các thông tin cua nhân viên
# - tinhThuong(): Tinh toán và trà vê sô tiên thuöng cùa nhân viên theo công thúc sau:
# Néu töng só giò làm cua nhân viên >=200 thì thuöng = luong * 20%
# Néu tông sô giò làm cùa nhân viên <200 và >=100 thì thuöng = luong * 10%
# Néu töng sô giò làm cùa nhân viên <100 thi thuöng = 0

from logging import exception
from operator import contains


class NhanVien():
    input_tuoi = 1
    input_tienluong = 0
    input_sogiolam= 0
    def __init__(self, ten = "a",tuoi = 18,diachi = "abc",tienluong = 0,sogiolam = 0):
        self.ten = ten
        self.tuoi = tuoi
        self.diachi = diachi
        self.tienluong = tienluong
        self.sogiolam = sogiolam

    def inputNV(self):
        while True:
            try:

                self.ten = input("Nhập họ và tên: ")
                if self.ten == "" or self.ten == " "or contains(self.ten,"  "):
                    raise exception ("Ten không được để trống")
                self.diachi = input("Nhập dia chi: ")
            except TypeError:
                print("Input cannot be empty")    
            else:
                break 

        while True:
            try:
                self.tuoi = input("Nhập tuổi của nhân viên: ")
                self.tienluong = input("Nhập lương cơ bản: ")
                self.sogiolam = input("Nhập số giờ làm việc: ")
                self.check_input()
            except ValueError:
                print("Hãy nhập số thực tế.")
            except TypeError:
                print("Hãy nhập số.")
            else:
                print()
                break    
    
    def check_input(self):
        self.input_tuoi = int(self.tuoi)
        self.input_tienluong = float(self.tienluong)
        self.input_sogiolam = float(self.sogiolam)
        if self.input_tuoi < 0 or self.input_tienluong <0 or self.input_sogiolam <0:
            raise exception ("Số không thể là âm!")
        elif self.input_tuoi ==0:
            raise exception ("Số tuổi không hợp lý.")    
        else:
            print()
    
    def printInfo(self):
        print("Thông tin nhân viên: ", self.ten)
        print("Tuổi = ",self.input_tuoi)
        print("Địa Chỉ = ", self.diachi)
        print("Lương cơ bản = ",self.input_tienluong)
        print("Số giờ làm = ",self.input_sogiolam)

# Néu töng só giò làm cua nhân viên >=200 thì thuöng = luong * 20%
# Néu tông sô giò làm cùa nhân viên <200 và >=100 thì thuöng = luong * 10%
# Néu töng sô giò làm cùa nhân viên <100 thi thuöng = 0

    def tinhthuongNV(self):
        print("Nhân viên: ", self.ten, "có số giờ làm là: ",self.sogiolam)
        bonus = 0
        if self.input_sogiolam >= 200:
            print("Thuởng 20%")
            bonus = self.input_tienluong/100 * 20
        elif 100 <= self.input_sogiolam < 200:
                print("Thuởng 10%")
                bonus = self.input_tienluong/100 * 10
        else:
            print("Không có thuởng")
        print("Tien thuong NV = ",bonus)    

        
# NhanVien_A = NhanVien()
# NhanVien_A.inputNV()            
# NhanVien_A.printInfo()
# NhanVien_A.tinhthuongNV()

