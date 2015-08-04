"""
Write this function



for i from 1 to n, do i % m and return the sum

f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)
You'll need to get a little clever with performance, since n can be a very large number
"""


def f(n, m):
    # I thought the Python version on codewars is broken
    q = 0
    for i in range(1, n+1):
        q += i % m
    return q



if __name__ == '__main__':
    print f(10, 5)
    print f(20, 20)
    print f(15, 10)
    print f(94291773, 54278150)
