"""
Task:

You have to write a function pattern which creates the following pattern upto n number of rows. If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.

Examples:

pattern(4):

1234
234
34
4
pattern(6):

123456
23456
3456
456
56
6
Note: There are no blank spaces

Hint: Use \n in string to jump to next line
"""

def pattern(n):
    _latter = ""
    _longest = ''
    for i in xrange(1, n+1):
        _longest += str(i)
    _latter += _longest + '\n'
    for i in xrange(1, n):
        _longest = _longest[len(str(i)):]
        _latter += _longest + '\n'
    return _latter[:-1]


if __name__ == '__main__':
    print pattern(5)
    print pattern(1)
    print pattern(12)
