# -*- coding: utf-8 -*-
"""
Task

The dot product is usually encountered in linear algebra or scientific computing. It's also called scalar product or inner product sometimes:

In mathematics, the dot product, or scalar product (or sometimes inner product in the context of Euclidean space), is an algebraic operation that takes two equal-length sequences of numbers (usually coordinate vectors) and returns a single number.
Wikipedia
In our case, we define the dot product algebraically for two vectors a = [a1, a2, …, an], b = [b1, b2, …, bn] as

dot a b = a1 * b1 + a2 * b2 + … + an * bn.
Your task is to find permutations of a and b, such that dot a b is minimal, and return that value. For example, the dot product of [1,2,3] and [4,0,1] is minimal if we switch 0 and 1 in the second vector.

Examples

min_dot([1,2,3,4,5], [0,1,1,1,0] ) = 6
min_dot([1,2,3,4,5], [0,0,1,1,-4]) = -17
min_dot([1,3,5]    , [4,-2,1]    ) = -3
Remarks

If the list or array is empty, minDot should return 0. All arrays or lists will have the same length. Also, for the dynamically typed languages, all inputs will be valid lists or arrays, you don't need to check for undefined, null etc.

Note: This kata is inspired by GCJ 2008.
"""

"""
best answer, 我觉得我想复杂了, 区分了正负数
def min_dot(a, b):
    return sum(x * y for (x, y) in zip(sorted(a), sorted(b, reverse = True)))
"""

def min_dot(a, b):
    if not a or not b:
        return 0
    a1 = [i for i in a if i<0]
    a2 = [i for i in a if i>=0]
    b1 = [i for i in b if i<0]
    b2 = [i for i in b if i>=0]
    if not a1 and not b1:
        a2.sort()
        b2.sort()
        b2.reverse()
        result = 0
        for i in a2:
            result += i * b2[0]
            b2 = b2[1:]
        return result
    elif not a2 and not b2:
        a1.sort()
        b1.sort()
        b1.reverse()
        result = 0
        for i in a1:
            result += i * b1[0]
            b1 = b1[1:]
        return result
    else:
        a1.sort()
        a2.sort()
        b1.sort()
        b2.sort()
        a2.reverse()
        b2.reverse()
        result = 0

        for i in a2:
            if b1:
                result += i * b1[0]
                b1 = b1[1:]
            else:
                result += i * b2[-1]
                b2 = b2[:-1]

        for i in a1:
            if b2:
                result += i * b2[0]
                b2 = b2[1:]
            else:
                result += i * b1[-1]
                b1 = b1[:-1]

        return result


if __name__ == '__main__':
    print(min_dot([1,2,3,4,5], [0,1,1,1,0]))
    print(min_dot([1,2,3,4,5], [0,0,1,1,-4]))
    print(min_dot([1,3,5], [4,-2,1]))
    print(min_dot([-1,-2,-5], [-2,-5,-2]))
