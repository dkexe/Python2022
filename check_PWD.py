class check_PWD:
    def check_input(pwd):
        list = []
        list.append(check_PWD.is_pass_len(pwd))
        list.append(check_PWD.is_contain_Lower(pwd))
        list.append(check_PWD.is_contain_Upper(pwd))
        list.append(check_PWD.is_contain_Number(pwd))
        list.append(check_PWD.is_contain_SpecialChar(pwd))
        
        # if False in list:
        #     return False
        # else: return True    
        return all(list)



    def is_pass_len(pwd):
        if len(pwd) < 8:
            return False
        else: return True    

    def is_contain_SpecialChar(pwd):
        if pwd.isalnum() == True:
            return False
        else: return True

    def is_contain_Upper(pwd):
        if any(x.isupper() == True for x in pwd):
            return True
        else: return False

    def is_contain_Lower(pwd):
        if any(y.islower() == True for y in pwd):
            return True
        else: return False    
    def is_contain_Number(pwd):
        if any(z.isnumeric() == True for z in pwd):
            return True
        else: return False    


# print(check_PWD.check_input("11111111")    )