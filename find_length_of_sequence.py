"""
As a part of this Kata, you need to find the length of the sequence in an array, between the first and the second occurance of a specified number.

For example, for a given array arr

[0, -3, 7, 4, 0, 3, 7, 9]
Finding length between two 7s like

`lengthOfSequence([0, -3, 7, 4, 0, 3, 7, 9], 7)`
would return 5.

For sake of simplicity, there will only be numbers (positive or negative) in the supplied array.

If there are less or more than two occurances of the number to searched for, return 0.
"""

def length_of_sequence(arr, n):
    if arr.count(n) > 2 or arr.count(n) < 2:
        return 0
    _index = arr.index(n)
    arr[_index] = 'dou'
    _final = arr.index(n)
    return _final - _index + 1


if __name__ == '__main__':
    print length_of_sequence([-7, 5, 0, 2, 9, 5], 5)
    print length_of_sequence([-7, 6, 2, -7, 4], -7)


