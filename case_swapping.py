"""
Given a string, swap the case for each of the letters.

e.g. CodEwArs --> cODeWaRS


"""
def swap(string_):
    _string = ''.join([i.upper() if i.islower() else i.lower() for i in string_])
    return _string


if __name__ == "__main__":
    print swap('HelloWorld')
    print swap('CodeWars')
