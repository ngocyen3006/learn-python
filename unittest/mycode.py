def checkPass(password):
    # password is at least eight characters long
    if len(password) < 8:
        return False
    # password must contains at least one uppercase character
    if not any([c.isupper() for c in password]):
        return False
    # password must contains at least one digit
    if not any([c.isdigit() for c in password]):
        return False
    # password must contains at least one lowercase character
    if not any([c.islower() for c in password]):
        return False
    return True
