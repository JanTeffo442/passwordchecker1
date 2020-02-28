from passwordchecker.password_check import PasswordChecker

password = "Gjgj&hfrfh7g"
ensure = PasswordChecker(password)

'''def test_validate():
    assert ensure.lowercase() == True
    assert ensure.uppercase() == True
    assert ensure.digit() == True
    assert ensure.special() == True

def test_password_is_ok():
    assert ensure.password_is_ok(password) == True'''

def test_lowercase():
    assert ensure.lowercase() == True

def test_uppercase():
    assert ensure.uppercase() == True

def test_digit():
    assert ensure.digit() == True

def test_special():
    assert ensure.special() == True
    

def test_validate():
    assert ensure.lowercase() == True
    assert ensure.uppercase() == True
    assert ensure.digit() == True
    assert ensure.special() == True

def test_password_is_ok():
    assert ensure.password_is_ok(password) == True