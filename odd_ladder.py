"""
Task:

You have to write a function pattern which creates the following pattern (see examples) up to the desired number of rows.

If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
If any even number is passed as argument then the pattern should last upto the largest odd number which is smaller than the passed even number.
Examples:

pattern(9):

1
333
55555
7777777
999999999
pattern(6):

1
333
55555
Note: There are no spaces in the pattern

Hint: Use \n in string to jump to next line
"""


def pattern(n):
    _latter = ""
    if n <= 0:
        return _latter
    else:
        for i in xrange(1, n+1):
            if i % 2 != 0:
                _latter += str(i) * i + '\n'
    return _latter[:-1]

if __name__ == '__main__':
    print pattern(4)
    print pattern(5)
