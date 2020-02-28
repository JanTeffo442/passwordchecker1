class PasswordChecker:
    def __init__(self, password= ''):
        self.password = password

    def lowercase(self):
        lowercase = any(c.islower() for c in self.password)
        return lowercase

    def uppercase(self):
        uppercase = any(c.isupper() for c in self.password)
        return uppercase

    def digit(self):
        digit = any(c.isdigit() for c in self.password)
        return digit

    
    def special(self):
        special_char = "$#@!&~`><'|^*"
        special_char = any(c in special_char for c in self.password)
        return special_char

    def validate(self):
        lowercase = self.lowercase()
        uppercase = self.uppercase()
        digit = self.digit()
        special = self.special()
        
        length = len(self.password)

        report = lowercase and uppercase and digit and special and length >= 8

        if report:
            print("Password meets all requirements")
            return True
        
        elif not lowercase:
            raise Exception("Password must have at least one lowercase character")
            return False
        
        elif not uppercase:
            raise Exception("Password must have at least one uppercase character")
            return False

        elif not digit:
            raise Exception("Password must have at least one numeric character")
            return False
        
        elif not special:
             raise Exception("Password must have at least one special character")
             return False

        elif length <= 8:
            raise Exception("Password should be at least 8 characters long")
            return False

        else:
            pass
    
    def password_is_ok(self, password):
        conditions = 0
        if len(password) == 0:
            return False
        conditions += 1

        if len(password) <= 8:
            return False
        conditions += 1

        if self.lowercase() == True:
            conditions += 1
        
        if self.uppercase() == True:
            conditions += 1
        
        if self.digit() == True:
            conditions += 1
        
        if self.special() == True:
            conditions += 1
        
        if conditions >= 3:
            return True
        else:
            return False

if __name__ == '__main__':
    
    password = "gRen$gkdkj"
    check = PasswordChecker(password)

    if check.password_is_ok(password) == True:
        print("Password is ok")
    else:

        print("Password is not ok")

    if check.validate() == True:
        print("Password is valid")
    else:
        print("Password is not invalid") 
