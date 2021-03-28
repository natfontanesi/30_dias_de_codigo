def alphanumeric(password):
    if(password.isalnum()):
        for char in password:
            if(char == " ")or(char == "_"):
                return False
        else:
            return True
    else:
        return False