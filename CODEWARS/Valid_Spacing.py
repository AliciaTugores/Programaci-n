#Your task is to write a function called valid_spacing() or validSpacing() which checks if a string has valid spacing. 
#The function should return either True or False.

def valid_spacing(s):
    if s == "":
        return True
    elif s.find('  ') == -1 and s[0] != ' ' and s[-1] != ' ':
        return True
    else:
        return False