class PasswordChecker:
    def __init__(self, password= ''):
        self.password = password

    def length(self):
        length = len(self.password) >= 8

        if not length:
            raise Exception("Password must exist and must be at least eight characters long")
        return length

    def lowercase(self):
        lowercase = any(c.islower() for c in self.password)

        if not lowercase:
            raise Exception("Password must have at least one lowercase character")
        return lowercase

    def uppercase(self):
        uppercase = any(c.isupper() for c in self.password)

        if not uppercase:
            raise Exception("Password must have at least one uppercase character")
        return uppercase

    def digit(self):
        digit = any(c.isdigit() for c in self.password)

        if not digit:
            raise Exception("Password must have at least one numeric character")
        return digit

    
    def special(self):
        special_char = "$#@!&~`><'|^*"
        special_char = any(c in special_char for c in self.password)

        if not special_char:
            raise Exception("Password must have at least one special character")
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
    
    password = "ht8)hfh45A*"
    check = PasswordChecker(password)

    if check.password_is_ok(password) == True:
        print("Password is ok")
    else:

        print("Password is not ok")

    if check.validate() == True:
        print("Password is valid")
    else:
        print("Password is not invalid") 
